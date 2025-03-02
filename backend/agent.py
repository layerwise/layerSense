import os
import openai
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
from langchain_core.prompts import PromptTemplate


prompt_template = PromptTemplate.from_template(
    
)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(
    model="o1-mini", #model="gpt-4o-mini",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    api_key=OPENAI_API_KEY,
    # base_url="...",
    # organization="...",
    # other params...
)
