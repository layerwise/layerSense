import os
import openai
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel

from prompts import manim_prompt
from models import ManimCodeOutput

parser = PydanticOutputParser(pydantic_object=ManimCodeOutput)


prompt = PromptTemplate(
    template=manim_prompt,
    input_variables=["vector_json", "user_prompt"],
    partial_variables={"format_instructions": parser.get_format_instructions}
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

chain = prompt | llm | parser
