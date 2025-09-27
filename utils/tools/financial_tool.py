from crewai.tools import tool
from langchain_community.document_loaders import PyPDFLoader

@tool("financial_doc_tool")
def read_data_tool(path: str = "data/sample.pdf") -> str:
    """Synchronous execution of the tool."""
    docs = PyPDFLoader(path).load()

    full_report = ""
    for data in docs:
        content = data.page_content

        # Clean and format the financial document data
        while "\n\n" in content:
            content = content.replace("\n\n", "\n")

        full_report += content + "\n"

    return full_report
