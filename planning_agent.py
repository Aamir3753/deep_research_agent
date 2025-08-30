from agents import Agent, ModelSettings
from configs.llm_configs import llm_model
from research_agents import search_agent


instructions = """
You are a planning agent.
Your task is to breakdown user search query and create research plans and handoff 
to the deep research agent to search as per the plan. 
"""


planning_agent = Agent(
    name="Planning Agent",
    instructions=instructions,
    model=llm_model,
    handoffs=[search_agent],
    model_settings=ModelSettings(tool_choice="auto")

)
