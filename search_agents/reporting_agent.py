from agents import Agent
from configs.llm_configs import llm_model

instructions = """
You are a citation and report generation agent your task is to 
generate final report based on search results with mentioning resources
"""
# synthesis_agent and  report_writer


reporting_agent = Agent(
    name="Reporting Agent",
    instructions=instructions,
    model=llm_model,
)
