from pathlib import Path
import ollama

analysis_files = list(
    Path("processed").glob("*_analysis.txt")
)

if not analysis_files:

    print(
        "No analysis files found."
    )

    exit()

for analysis_file in analysis_files:

    analysis = analysis_file.read_text(
        encoding="utf-8"
    )

    print(
        f"\nCreating publishable output for: {analysis_file.name}"
    )

    prompt = f"""
You are a Payments Intelligence Communications Specialist.

Using the analysis below, create:

1. Executive Brief
   (5 bullet points)

2. LinkedIn Draft
   (professional post,
   maximum 200 words)

3. Human Approval Status

Always set:
APPROVAL REQUIRED = YES

Analysis:

{analysis}
"""

    response = ollama.chat(
        model="phi3",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    publish_content = (
        response["message"]["content"]
    )

    output_file = (
        analysis_file.stem
        + "_publish.txt"
    )

    output_path = (
        Path("processed")
        / output_file
    )

    output_path.write_text(
        publish_content,
        encoding="utf-8"
    )

    print(
        f"Created: {output_file}"
    )

print(
    "\nPublishing Agent Completed"
)