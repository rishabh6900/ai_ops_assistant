from llm.gemini import get_llm

def verifier_agent(task: str, execution_results: list) -> str:
    llm = get_llm()

    prompt = f"""
You are a Verifier Agent for an AI Operations Assistant.
Your job is to synthesize the execution results into a clear, professional, and well-formatted markdown response that directly answers the user's task.

Guidelines:
- Present GitHub repositories with names, star counts, URLs, and descriptions clearly formatted.
- Present weather information clearly with temperatures and conditions.
- If any tool encountered an error or missing information, explain it constructively.
- Use clean Markdown headers, bullet points, and formatting.

Original Task:
{task}

Execution Results:
{execution_results}
"""

    response = llm.invoke(prompt)
    return response.content if hasattr(response, "content") else str(response)
