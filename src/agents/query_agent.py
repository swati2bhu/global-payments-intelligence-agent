import json
import ollama

QUESTION = input(
    "\nAsk a question: "
)

with open(
    "processed/new_downloaded_content.json",
    "r",
    encoding="utf-8"
) as file:

    documents = json.load(file)

context = ""

for document in documents:

    context += "\n\n"
    context += (
        f"DOCUMENT: "
        f"{document['document_name']}\n"
    )

    context += (
        document["content"][:3000]
    )

prompt = f"""
You are a Payments Intelligence Assistant.

Answer the user's question
using ONLY the content provided.

If the answer is not present,
say:

'Information not found in the
available publications.'

PUBLICATIONS:

{context}

QUESTION:

{QUESTION}
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

print("\n")
print(response["message"]["content"])