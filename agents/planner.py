from llm.gemini import get_llm
from pydantic import BaseModel, Field
from typing import List
import json
import re

class PlanStep(BaseModel):
    step: str = Field(description="Description of the action to take")
    tool: str = Field(description="Tool to use: 'github_search' or 'weather_lookup'")
    input: str = Field(description="Input parameter for the tool (e.g. search query or city name)")

class Plan(BaseModel):
    steps: List[PlanStep]


def extract_json(text: str) -> str:
    """
    Robustly extract JSON object from LLM response text.
    Handles ```json code fences, preamble commentary, and trailing text.
    """
    text = text.strip()

    # Match JSON inside markdown code block
    json_block = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", text, re.DOTALL)
    if json_block:
        return json_block.group(1).strip()

    # Match raw JSON object from outermost braces
    brace_match = re.search(r"\{.*\}", text, re.DOTALL)
    if brace_match:
        return brace_match.group(0).strip()

    return text


def planner_agent(user_task: str) -> Plan:
    llm = get_llm()

    prompt = f"""
You are a Planner Agent.
Break down the user's task into sequential steps using the available tools:
1. 'github_search': for finding repositories, projects, or code on GitHub.
2. 'weather_lookup': for fetching current weather conditions for a city.

RULES:
- Return ONLY valid JSON matching this schema:
{{
  "steps": [
    {{
      "step": "step description",
      "tool": "github_search" | "weather_lookup",
      "input": "parameter string"
    }}
  ]
}}

Task:
{user_task}
"""

    response = llm.invoke(prompt)
    raw_text = response.content if hasattr(response, "content") else str(response)
    clean_json = extract_json(raw_text)

    try:
        return Plan.model_validate_json(clean_json)
    except Exception as e:
        # Fallback to direct json.loads and dict validation
        parsed = json.loads(clean_json)
        return Plan.model_validate(parsed)

