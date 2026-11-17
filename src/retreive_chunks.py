import faiss
import json
import numpy as np
import ollama

# =====================================
# Load FAISS Index
# =====================================

index = faiss.read_index(
    "../vectorstore/payments_index.faiss"
)

print("FAISS Index Loaded Successfully")
print(f"Vectors In Index = {index.ntotal}")

# =====================================
# Load Metadata
# =====================================

with open(
    "../vectorstore/chunk_metadata.json",
    "r",
    encoding="utf-8"
) as file:

    metadata = json.load(file)

print(f"Metadata Records = {len(metadata)}")

# =====================================
# User Question
# =====================================

question = "Tell m eopportunities dosucssed."

print(f"\nQuestion: {question}")

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

print(f"Question Vector Shape = {query_vector.shape}")

# =====================================
# Search FAISS
# =====================================

k = 3

distances, indices = index.search(
    query_vector,
    k
)

print("\nDistances:")
print(distances)

print("\nIndices:")
print(indices)

# =====================================
# Display Matching Chunks
# =====================================

print("\n==============================")
print("TOP MATCHING CHUNKS")
print("==============================")

for rank, chunk_index in enumerate(indices[0]):

    print(f"\nMatch {rank + 1}")
    print(f"Chunk ID: {chunk_index}")

    print("\nChunk Text:\n")

    print(
        metadata[chunk_index]["text"][:1000]
    )

    print("\n-----------------------------------")