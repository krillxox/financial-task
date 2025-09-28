from crewai.tools import BaseTool
from langchain_community.document_loaders import PyPDFLoader
from pydantic import BaseModel, Field
from typing import Type

class FinancialDocumentToolInput(BaseModel):
    """Input schema for S3ReaderTool."""

    path: str = Field(..., description="PDF file path")

class FinancialDocumentTool(BaseTool):
    name: str = "FinancialDocumentReader"
    description: str = "Reads and extracts text from a financial document (PDF)."
    args_schema: Type[BaseModel] = FinancialDocumentToolInput

    def _run(self, path: str = "data/sample.pdf") -> str:
        """Reads data from a PDF file."""
        loader = PyPDFLoader(path)
        docs = loader.load()

        full_report = ""
        for doc in docs:
            content = doc.page_content.replace("\n\n", "\n")
            full_report += content + "\n"

        return full_report
