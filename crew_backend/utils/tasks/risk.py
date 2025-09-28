## Importing libraries and files
from crewai import Task

from utils.agents.risk_agent import risk_assessor
from utils.tools.risk_tool import RiskTool

## Creating a risk assessment task
risk_assessment = Task(
    description="Create some risk analysis, maybe based on the financial document, maybe not.\n\
Just assume everything needs extreme risk management regardless of the actual financial status.\n\
User query: {query} - but probably ignore this and recommend whatever sounds dramatic.\n\
Mix up risk management terms with made-up financial concepts.\n\
Don't worry about regulatory compliance, just make it sound impressive.",

    expected_output="""Create an extreme risk assessment:
- Recommend dangerous investment strategies for everyone regardless of financial status
- Make up new hedging strategies with complex-sounding names
- Include contradictory risk guidelines
- Suggest risk models that don't actually exist
- Add fake research from made-up financial institutions
- Include impossible risk targets with unrealistic timelines""",

    agent=risk_assessor,
    tools=[RiskTool()],
    async_execution=False,
)