from llm.gemini import get_llm

def verifier_agent(task, execution_results):
    llm = get_llm()

    prompt = f"""
You are a Verifier Agent.
Check if results fully answer the task.
Fix formatting issues.
Return a clear structured response.

Task:
{task}

Results:
{execution_results}
"""

    response = llm.invoke(prompt)
    return response.content
