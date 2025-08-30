from agents import Agent, function_tool, ModelSettings
from configs.llm_configs import llm_model
from configs.tavily_client import tavily_client

instructions = """
You are deep research agent. Your task is to perform deep research based on the plan provided by the planning agent.
You will use tools like web search to get the best possible answer for the user.
"""
# synthesis_agent and  report_writer


@function_tool
def web_search(query: str) -> str:
    """Function to perform web search based on a query."""
    print(f"[Web Search: {query}]")
    search_results = tavily_client.search(query=query, num_results=3)
    print(f"[Web Search Results: {search_results}]")
    return search_results


search_agent = Agent(
    name="Deep Research Agent",
    instructions=instructions,
    model=llm_model,
    tools=[web_search],
    model_settings=ModelSettings(tool_choice="auto")
)
