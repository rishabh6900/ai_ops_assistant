from tools.github_tool import search_github_repos
from tools.weather_tool import get_weather

def executor_agent(plan):
    results = []

    for step in plan.steps:
        if step.tool == "github_search":
            output = search_github_repos(step.input)
        elif step.tool == "weather_lookup":
            output = get_weather(step.input)
        else:
            output = {"error": "Unknown tool"}

        results.append({
            "step": step.step,
            "tool": step.tool,
            "output": output
        })

    return results
