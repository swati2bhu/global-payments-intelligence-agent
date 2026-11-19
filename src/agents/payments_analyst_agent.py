import json
from pathlib import Path
import ollama

# Load downloaded content

with open(
    "processed/new_downloaded_content.json",
    "r",
    encoding="utf-8"
) as file:

    documents = json.load(file)

# Analyse each document

for document in documents:

    print("\n" + "=" * 80)

    print(
        f"ANALYSING: {document['document_name']}"
    )

    content = document["content"][:6000]

    prompt = f"""
You are a Senior Payments Domain Analyst.

Analyse the following payments-related publication.

Document:
{document['document_name']}

Content:
{content}

Provide:

1. Executive Summary

2. Key Changes

3. Business Impact

4. Who Is Affected

5. Priority
(High / Medium / Low)

6. Recommended Actions

Be concise and business-focused.
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

    analysis = (
        response["message"]["content"]
    )

    print("\n")
    print(analysis)

    # Ensure processed folder exists

    Path("processed").mkdir(
        exist_ok=True
    )

    # Save analysis

    output_file = (
        Path("processed")
        / f"{document['document_name']}_analysis.txt"
    )

    output_file.write_text(
        analysis,
        encoding="utf-8"
    )

    print(
        f"\nAnalysis Saved: {output_file.name}"
    )

print(
    "\nPayments Analyst Agent Completed"
)