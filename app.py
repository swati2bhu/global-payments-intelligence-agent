import streamlit as st
from src.rag_engine import ask_question

# ====================================
# Page Config
# ====================================

st.set_page_config(
    page_title="Payments Regulatory Intelligence Copilot",
    layout="wide"
)

# ====================================
# Header
# ====================================

st.title("🏦 Payments Regulatory Intelligence Copilot")

st.markdown(
    """
Ask questions about regulatory documents, circulars,
DPI, payments, settlement cycles, risk, opportunities,
and adoption challenges.
"""
)

# ====================================
# Question Input
# ====================================

question = st.text_area(
    "Enter your question",
    height=120,
    placeholder="Example: What are the adoption challenges?"
)

# ====================================
# Analyze
# ====================================

if st.button("Analyze"):

    if question.strip() == "":
        st.warning("Please enter a question.")
    else:

        with st.spinner("Analyzing..."):

            result = ask_question(question)

        # ====================================
        # Main Answer
        # ====================================

        st.subheader("Answer")

        st.write(result["answer"])

        # ====================================
        # Retrieval Diagnostics
        # ====================================

        with st.expander("Retrieved Context"):

            st.write(result["context"])

        with st.expander("Retrieval Details"):

            st.write("Distances")

            st.write(result["distances"])

            st.write("Indices")

            st.write(result["indices"])