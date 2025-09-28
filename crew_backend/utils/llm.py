from crewai import LLM
from config import OPENAI_API_KEY, OPENAI_MODEL, LLM_BASE_URL

llm = LLM(
    model=OPENAI_MODEL,
    temperature=0.7,
    base_url=LLM_BASE_URL,
    api_key=OPENAI_API_KEY
)