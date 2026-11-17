import faiss
import json
import numpy as np
import ollama

# =====================================
# Load FAISS
# =====================================

index = faiss.read_index(
    "vectorstore/payments_index.faiss"
)

# =====================================
# Load Metadata
# =====================================

with open(
    "vectorstore/chunk_metadata.json",
    "r",
    encoding="utf-8"
) as file:

    metadata = json.load(file)

# =====================================
# User Question
# =====================================

question = input("Ask a question: ")

# =====================================
# Create Question Embedding
# =====================================

response = ollama.embed(
    model="nomic-embed-text",
    input=question
)

question_embedding = response["embeddings"][0]

query_vector = np.array(
    [question_embedding],
    dtype="float32"
)

# =====================================
# Search FAISS
# =====================================

k = 3

distances, indices = index.search(
    query_vector,
    k
)

# =====================================
# Build Context
# =====================================

retrieved_chunks = []

for chunk_index in indices[0]:

    retrieved_chunks.append(
        metadata[chunk_index]["text"]
    )

context = "\n\n".join(retrieved_chunks)

# =====================================
# Create Prompt
# =====================================

prompt = f"""
You are a senior payments and regulatory analyst.

Use ONLY the supplied context.

First understand the user's intent.

Possible intents include:
- General Question
- Summary
- Change Analysis
- Opportunity Analysis
- Risk Analysis
- Recommendation Request

Answer according to the intent.

Question:
{question}

Context:
{context}
"""

# =====================================
# Ask phi3
# =====================================

response = ollama.chat(
    model="phi3",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

print("\n====================")
print("FINAL ANSWER")
print("====================\n")

print(
    response["message"]["content"]
)