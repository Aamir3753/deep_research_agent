from agents import Agent, function_tool, ModelSettings
from configs.llm_configs import llm_model
from configs.tavily_client import tavily_client
from search_agents.reporting_agent import reporting_agent
import requests

instructions = """
You are a search agent.
You are tasks are as follows 
1) Perform Web Search Using web search tool
2) Handof the request to the reporting agent to generate reports.
"""
# synthesis_agent and  report_writer


@function_tool
def web_search(query: str) -> str:
    """Function to perform web search based on a query."""
    search_results = tavily_client.search(query=query, num_results=3)
    return search_results


@function_tool
def explore_search_urls(url: str) -> str:
    """Explore Urls gethered from web search"""
    url_resp = requests.get(url)
    return url_resp.text


search_agent = Agent(
    name="Search Agent",
    instructions=instructions,
    model=llm_model,
    tools=[web_search],
    handoffs=[reporting_agent],
    model_settings=ModelSettings(tool_choice="required")
)
