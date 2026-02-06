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


# Example Task 
Find the top GitHub repositories related to AI agents
and tell me the current weather in Delhi.


{
    "steps":[
        0:{
            "step":"Search GitHub for repositories related to AI agents."
            "tool":"github_search"
            "input":"AI agents"
        }
        1:{
            "step":"Look up the current weather in Delhi."
            "tool":"weather_lookup"
            "input":"Delhi"
        }
    ]
}


# More Example Task  

1. Find the top 5 Python repositories related to machine learning on GitHub
and tell me the current weather in Mumbai.

2. Show me popular data science GitHub repositories and the current weather in Delhi.

3. Find highly starred Python repositories for beginners
and give me the current weather in Pune.

4.  Find the top GitHub repositories related to LangChain and LLM agents,
summarize what they are used for,
and tell me the current weather in Chennai.


# Set Up Setup Instructions

1. Clone Repository
   1. git clone
   2. cd ai_ops_assistant 
2. Create Virtual Environment
   1. conda create -n ai_ops_assistant python=3.10 
   2. conda activate ai_ops_assistant

3. Install Dependencies 
   pip install -r requirements.txt 

4. Configure Environment Variables
   
   GOOGLE_API_KEY="------------"
   GITHUB_TOKEN="-----------"
   OPENWEATHER_API_KEY='---------'

6. Run the Application  
   python -m streamlit run main.py 

7. Open browser at: 
   http://localhost:8501  
   If http://localhost:8501 does not open, check where Streamlit is running.
   When you run python -m streamlit run main.py, it shows a link after a few seconds—just click that link.
