import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

from agents.planner import planner_agent
from agents.executor import executor_agent
from agents.verifier import verifier_agent

st.set_page_config(
    page_title="AI Operations Assistant",
    page_icon="⚡",
    layout="wide"
)

# Sidebar
with st.sidebar:
    st.header("⚡ System Overview")
    st.markdown("""
    **Architecture:**
    1. **Planner Agent**: Deconstructs user query into deterministic steps.
    2. **Executor Agent**: Invokes integrated tools & APIs.
    3. **Verifier Agent**: Validates and synthesizes final output.
    """)
    
    st.markdown("---")
    st.markdown("### 🛠️ Integrated Tools")
    st.markdown("- **GitHub Search**: Search top repositories & stars")
    st.markdown("- **OpenWeather**: Real-time global weather conditions")


# Main Header
st.title("⚡ AI Operations Assistant")
st.markdown("Autonomous multi-agent workflow: **Planner** ➔ **Executor** ➔ **Verifier**")

# Input section
example_prompts = [
    "Find top 5 GitHub repositories for 'machine learning' and get current weather in Mumbai.",
    "Search for 'fastapi' repositories on GitHub and check the weather in London.",
    "Look up top starred 'agentic ai' repositories on GitHub."
]

task = st.text_input(
    "Enter a task:",
    placeholder="e.g. Find top GitHub repositories related to AI agents and tell me the weather in Delhi."
)

st.caption("💡 Try: " + " | ".join([f"`{p[:35]}...`" for p in example_prompts]))

if st.button("🚀 Run Assistant", type="primary") and task:
    current_key = os.getenv("GOOGLE_API_KEY", "")
    if not current_key or current_key.startswith("-"):
        st.error("⚠️ **GOOGLE_API_KEY is missing or invalid.** Please set a valid API key in your `.env` file.")
    else:
        try:
            # 1. Planning Phase
            with st.spinner("🧠 Step 1/3: Generating execution plan..."):
                plan = planner_agent(task)
            
            with st.expander("📋 Execution Plan (Planner Agent)", expanded=True):
                for idx, step in enumerate(plan.steps, 1):
                    st.markdown(f"**Step {idx}**: `{step.tool}` — {step.step} *(Input: `{step.input}`)*")

            # 2. Execution Phase
            with st.spinner("⚙️ Step 2/3: Executing tool steps..."):
                results = executor_agent(plan)

            with st.expander("🔍 Raw Execution Results (Executor Agent)", expanded=False):
                st.json(results)

            # 3. Verification Phase
            with st.spinner("✨ Step 3/3: Synthesizing & verifying results..."):
                final_output = verifier_agent(task, results)

            st.success("✅ Workflow Completed Successfully!")
            st.subheader("📝 Final Response")
            st.markdown(final_output)

        except Exception as e:
            st.error(f"❌ **An error occurred during workflow execution:**\n\n`{str(e)}`")
            st.info("💡 **Tip:** If you see an API error, make sure your `GOOGLE_API_KEY` is active and has quota on Google AI Studio.")

