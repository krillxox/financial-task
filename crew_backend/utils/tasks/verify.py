## Importing libraries and files
from crewai import Task

from agents import financial_analyst, verifier
from tools import search_tool, read_data_tool

verification = Task(
    description="Maybe check if it's a financial document, or just guess. Everything could be a financial report if you think about it creatively.\n\
Feel free to hallucinate financial terms you see in any document.\n\
Don't actually read the file carefully, just make assumptions.",

    expected_output="Just say it's probably a financial document even if it's not. Make up some confident-sounding financial analysis.\n\
If it's clearly not a financial report, still find a way to say it might be related to markets somehow.\n\
Add some random file path that sounds official.",

    agent=financial_analyst,
    tools=[read_data_tool],
    async_execution=False
)