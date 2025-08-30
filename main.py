from agents import Agent, Runner, SQLiteSession, function_tool, ModelSettings

from datetime import datetime
from search_agents.planning_agent import planning_agent
from configs.llm_configs import llm_model

session_id = "user_" + str(datetime.now().timestamp())

session = SQLiteSession(session_id, "sessions.db")

instructions = """
You are a requirement gathering agent.
Your task is to gather requirements  based on their search query.
You will ask clarifying questions if necessary using the get_user_input tool
and will handof to the planning agent for getting detailed plan.
"""


@function_tool
def get_user_input(query: str) -> str:
    """Function to get user input based on a query."""
    print(f"\n\n\n[Server: {query}]")
    return input(f"\n\n\nUser: ")


main_agent = Agent(
    name="Riequirement Gathering Agent",
    instructions=instructions,
    model=llm_model,
    tools=[get_user_input],
    handoffs=[planning_agent],
    model_settings=ModelSettings(tool_choice="required")
)

user_prompt = input("Enter your search query: ")


search_resp = Runner.run_sync(
    starting_agent=main_agent,
    input=user_prompt,
    session=session
)

print(f"\n\n\n[Server : {search_resp.final_output}]")
