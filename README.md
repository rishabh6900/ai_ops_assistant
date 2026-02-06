# AI Operations Assistant 
A local, multi-agent AI Operations Assistant that accepts a natural-language task, plans steps, calls real APIs, and returns a validated, structured answer.

This project demonstrates agent-based reasoning, LLM orchestration, and real-world API integrations using Streamlit, LangChain, LangGraph, and Gemini LLM.

# Key Features
1. Planner Agent – Converts user tasks into a structured execution plan
2. Executor Agent – Executes each step using real APIs
3. Verifier Agent – Validates, fixes, and formats final output
4. Real API Integrations 
    1. GitHub Repository Search 
    2. OpenWeather Current Weather 

5. Streamlit UI – Runs locally on localhost
6. Structured Outputs – JSON schema validation using Pydantic


# Architecture Overview
User (Streamlit UI) ----> Planner Agent (LLM → JSON Plan)-----> Executor Agent (API Calls)-------->Verifier Agent (LLM Validation)------->Final Structured Answer


# Technologies Used 
Streamlit – Local
LangChain – LLM workflows
LangGraph – Agent orchestration
Google Gemini – Reasoning & planning
GitHub API – Repository search
OpenWeather API – Weather data
Python 3.10 – Runtime environment
Pydantic – Schema validation