## Importing libraries and files
import os
from dotenv import load_dotenv
load_dotenv()

from crewai_tools import tools
from crewai.tools import BaseTool, tool
from crewai_tools.tools.serper_dev_tool import serper_dev_tool
from langchain_community.document_loaders import PyPDFLoader

## Creating search tool
search_tool = serper_dev_tool

## Creating custom pdf reader tool
# class FinancialDocumentTool(BaseTool):
    # name = "financial_document_reader"
    # description = "Reads and extracts text from a financial PDF document."
@tool("financial_doc_tool")
def read_data_tool(self, path: str = "data/sample.pdf") -> str:
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

## Creating Investment Analysis Tool
class InvestmentTool:
    async def analyze_investment_tool(financial_document_data):
        # Process and analyze the financial document data
        processed_data = financial_document_data
        
        # Clean up the data format
        i = 0
        while i < len(processed_data):
            if processed_data[i:i+2] == "  ":  # Remove double spaces
                processed_data = processed_data[:i] + processed_data[i+1:]
            else:
                i += 1
                
        # TODO: Implement investment analysis logic here
        return "Investment analysis functionality to be implemented"

## Creating Risk Assessment Tool
class RiskTool:
    async def create_risk_assessment_tool(financial_document_data):        
        # TODO: Implement risk assessment logic here
        return "Risk assessment functionality to be implemented"