from llm.gemini import get_llm
from pydantic import BaseModel
from typing import List
import json
import re

class PlanStep(BaseModel):
    step: str
    tool: str
    input: str

class Plan(BaseModel):
    steps: List[PlanStep]


def extract_json(text: str) -> str:
    """
    Extract JSON object from LLM response.
    Handles ```json fences and extra text.
    """
    text = text.strip()

    # Remove ```json ``` fences if present
    text = re.sub(r"^```json\s*", "", text)
    text = re.sub(r"\s*```$", "", text)

    return text


def planner_agent(user_task: str) -> Plan:
    llm = get_llm()

    prompt = f"""
You are a Planner Agent.

RULES (VERY IMPORTANT):
- Return ONLY valid JSON
- Do NOT use markdown
- Do NOT use ```json
- Do NOT add explanations
- JSON must follow this schema exactly:

{{
  "steps": [
    {{
      "step": "description",
      "tool": "github_search | weather_lookup",
      "input": "string"
    }}
  ]
}}

Task:
{user_task}
"""

    response = llm.invoke(prompt)

    raw_text = response.content
    clean_json = extract_json(raw_text)

    return Plan.model_validate_json(clean_json)
