from tools.github_tool import search_github_repos
from tools.weather_tool import get_weather

def executor_agent(plan):
    results = []

    for step in plan.steps:
        try:
            if step.tool == "github_search":
                output = search_github_repos(step.input)
            elif step.tool == "weather_lookup":
                output = get_weather(step.input)
            else:
                output = {"error": f"Unknown tool requested: '{step.tool}'"}
        except Exception as e:
            output = {"error": f"Tool execution failed: {str(e)}"}

        results.append({
            "step": step.step,
            "tool": step.tool,
            "output": output
        })

    return results

