from agents import OpenAIChatCompletionsModel, AsyncOpenAI
import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())




external_client = AsyncOpenAI(
    api_key=os.environ.get("GEMINI_API_KEY"),
    base_url=os.environ.get("GEMINI_API_HOST"),
)


llm_model = OpenAIChatCompletionsModel(
    openai_client=external_client,
    model=os.environ.get("LLM_MODEL"),
)