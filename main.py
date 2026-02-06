import streamlit as st
from dotenv import load_dotenv
from agents.planner import planner_agent
from agents.executor import executor_agent
from agents.verifier import verifier_agent

load_dotenv()

st.set_page_config(page_title="AI Operations Assistant", layout="wide")
st.title("AI Operations Assistant")

task = st.text_input("Enter a task:")

if st.button("Run Assistant") and task:
    with st.spinner("Planning..."):
        plan = planner_agent(task)
        st.subheader("Plan")
        st.json(plan.model_dump())

    with st.spinner("Executing..."):
        results = executor_agent(plan)
        st.subheader("Execution Results")
        st.json(results)

    with st.spinner("Verifying..."):
        final_output = verifier_agent(task, results)
        st.subheader("Final Answer")
        st.write(final_output)
