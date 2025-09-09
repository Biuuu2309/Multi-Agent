from langchain_community.chat_models import ollama, ChatOllama
from langchain.tools import Tool
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub
from typing import TypedDict, Annotated, List
import operator

llm = ChatOllama(model="llama3") # <-- Sử dụng model bạn đã kéo về, ví dụ "llama3", "mistral"
