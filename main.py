from agents import Agent, OpenAIChatCompletionsModel, AsyncOpenAI, Runner, function_tool
from dotenv import find_dotenv, load_dotenv
from tavily import TavilyClient
import os

load_dotenv(find_dotenv())

external_client = AsyncOpenAI(
    api_key=os.environ.get("GEMINI_API_KEY"),
    base_url=os.environ.get("GEMINI_API_HOST"),
)


llm_model = OpenAIChatCompletionsModel(
    openai_client=external_client,
    model="gemini-1.5-flash",
)


@function_tool
def search_internet(search_query: str):
    tavily_client = TavilyClient(api_key=os.environ.get("TAVILY_API_KEY"))
    response = tavily_client.search(query=search_query, max_results=5)
    print(response)
    return response


search_agent = Agent(
    name="Search Agent",
    instructions="An agent that can search the web for realtime information",
    model=llm_model,
    tools=[search_internet]
)


search_resp = Runner.run_sync(
    starting_agent=search_agent, input="What is the dollar to PKR rate?",)

print(search_resp.final_output)
