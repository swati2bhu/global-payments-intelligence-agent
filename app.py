import sys
import streamlit as st
import subprocess
from pathlib import Path


st.set_page_config(
    page_title="Global Payments Intelligence Platform",
    layout="wide"
)

st.title("🌍 Global Payments Intelligence Platform")

st.markdown("""
Monitor RBI, NPCI, SWIFT and BIS publications,
analyse business impact and query knowledge.
""")



import json
from pathlib import Path

st.header("📡 Source Monitoring Dashboard")

new_pub_file = Path(
    "inventory/new_publications.json"
)

if new_pub_file.exists():

    with open(
        new_pub_file,
        "r",
        encoding="utf-8"
    ) as file:

        new_publications = json.load(file)

    total_new = len(new_publications)

    st.metric(
        "New Publications Detected",
        total_new
    )

    if total_new > 0:

        dashboard_data = []

        for item in new_publications:

            content_type = "HTML"

            if ".pdf" in item["url"].lower():

                content_type = "PDF"

            dashboard_data.append(
                {
                    "Source": item["source"],
                    "Title": item["title"],
                    "Type": content_type,
                    "URL": item["url"]
                }
            )

        st.dataframe(
            dashboard_data,
            use_container_width=True
        )

    else:

        st.success(
            "No new content detected."
        )

else:

    st.info(
        "No monitoring results available yet. Run Monitor Sources."
    )

# ===================================
# OBSERVE AGENT
# ===================================

st.header("🔍 Observe Agent")

if st.button("Monitor Sources"):

    with st.spinner("Building inventory..."):

        subprocess.run(
            [sys.executable, "src/agents/build_inventory.py"]
        )

        subprocess.run(
            [sys.executable, "src/agents/find_new_inventory.py"]
        )

        subprocess.run(
            [sys.executable, "src/agents/download_new_content.py"]
        )

    st.success("Monitoring completed.")

# ===================================
# KNOWLEDGE AGENT
# ===================================

st.header("🧠 Knowledge Agent")

if st.button("Process Downloads"):

    with st.spinner("Building knowledge..."):

        subprocess.run(
            [
                sys.executable,
                "src/worksflows/ingest_new_downloaded.py"
            ]
        )

        subprocess.run(
            [
                sys.executable,
                "src/worksflows/chunk_downloaded_content.py"
            ]
        )

    st.success("Knowledge processing completed.")

# ===================================
# PAYMENTS ANALYST AGENT
# ===================================

st.header("📊 Payments Analyst Agent")

if st.button("Analyse Publications"):

    with st.spinner("Analysing publications..."):

        subprocess.run(
            [
                sys.executable,
                "src/agents/payments_analyst_agent.py"
            ]
        )

    st.success("Analysis complete.")

# ===================================
# PUBLISHING AGENT
# ===================================

st.header("📰 Publishing Agent")

if st.button("Generate Executive Content"):

    with st.spinner("Generating executive content..."):

        subprocess.run(
            [
                sys.executable,
                "src/agents/publishing_agent.py"
            ]
        )

    st.success("Publishing content generated.")

# ===================================
# QUERY AGENT
# ===================================

st.header("❓ Query Agent")

question = st.text_input(
    "Ask a question"
)

if st.button("Ask"):

    if question:

        st.info(
            "Query Agent integration is next."
        )

# ===================================
# OUTPUT VIEWER
# ===================================

st.header("📁 Generated Outputs")

processed_folder = Path("processed")

if processed_folder.exists():

    files = list(processed_folder.glob("*"))

    if files:

        selected_file = st.selectbox(
            "View Output",
            [file.name for file in files]
        )

        selected_path = (
            processed_folder / selected_file
        )

        try:

            content = selected_path.read_text(
                encoding="utf-8",
                errors="ignore"
            )

            st.text_area(
                "Content",
                value=content,
                height=400
            )

        except Exception:

            st.warning(
                "Unable to display file."
            )

    else:

        st.info(
            "No generated files yet."
        )

else:

    st.info(
        "Processed folder not found."
    )