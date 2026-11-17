import faiss
import json
import numpy as np
import ollama


# ====================================
# Load Resources Once
# ====================================

index = faiss.read_index(
    "vectorstore/payments_index.faiss"
)

with open(
    "vectorstore/chunk_metadata.json",
    "r",
    encoding="utf-8"
) as file:

    metadata = json.load(file)


# ====================================
# Main RAG Function
# ====================================

def ask_question(question, k=3):

    # -------------------------
    # Question Embedding
    # -------------------------

    response = ollama.embed(
        model="nomic-embed-text",
        input=question
    )

    question_embedding = response["embeddings"][0]

    query_vector = np.array(
        [question_embedding],
        dtype="float32"
    )

    # -------------------------
    # Search FAISS
    # -------------------------

    distances, indices = index.search(
        query_vector,
        k
    )

    # -------------------------
    # Collect Chunks
    # -------------------------

    retrieved_chunks = []

    for chunk_index in indices[0]:

        retrieved_chunks.append(
            metadata[chunk_index]["text"]
        )

    context = "\n\n".join(
        retrieved_chunks
    )

    # -------------------------
    # Agent Prompt
    # -------------------------

    prompt = f"""
You are a senior payments and regulatory intelligence analyst.

Use ONLY the supplied context.

First determine the user's intent.

Possible intents include:
- General Information
- Summary
- Opportunity Analysis
- Risk Analysis
- Recommendation Request
- Comparison

Provide a structured and concise response.

Question:
{question}

Context:
{context}
"""

    # -------------------------
    # Phi3
    # -------------------------

    response = ollama.chat(
        model="phi3",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    answer = response["message"]["content"]

    return {
        "answer": answer,
        "indices": indices.tolist(),
        "distances": distances.tolist(),
        "context": context
    }