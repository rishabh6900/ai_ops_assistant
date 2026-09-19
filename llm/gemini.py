from langchain_google_genai import ChatGoogleGenerativeAI
import os

def get_llm(api_key: str = None, model: str = "gemini-2.5-flash"):
    key = api_key or os.getenv("GOOGLE_API_KEY")
    if not key or key.startswith("-"):
        raise ValueError(
            "Valid GOOGLE_API_KEY is required. Please set it in your .env file or in the app sidebar."
        )
    return ChatGoogleGenerativeAI(
        model=model,
        temperature=0,
        google_api_key=key
    )

