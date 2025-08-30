from tavily import TavilyClient
import os
from dotenv import find_dotenv, load_dotenv


load_dotenv(find_dotenv())


tavily_client = TavilyClient(
    api_key=os.environ.get("TAVILY_API_KEY"))
