from langchain_community.chat_models import ollama
from langchain.tools import Tool
from langchain.agents import create_react_agent, AgentExecutor

def get_weather_lc(city: str) -> str:
    return f"It's always sunny in {city}!"

weather_agent_lc = create_react_agent(
    model="anthropic:claude-3-7-sonnet-latest",
    tools=[get_weather_lc],
    prompt="You are a helpful assistant"
)