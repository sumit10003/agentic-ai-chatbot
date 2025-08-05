# app/agent.py

import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType
from langchain.utilities import SerpAPIWrapper
from langchain.prompts import PromptTemplate

load_dotenv()  # Load your .env variables

openai_api_key = os.getenv("OPENAI_API_KEY")

# Setup Chat Model
llm = ChatOpenAI(temperature=0.5, openai_api_key=openai_api_key)

# Example Tool (can replace this with your custom tool later)
def hello_tool_func(input_text):
    return f"Hello! You said: {input_text}"

tools = [
    Tool(
        name="EchoTool",
        func=hello_tool_func,
        description="Repeats what the user said."
    )
]

# Initialize Agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

def ask_agent(query: str):
    return agent.run(query)