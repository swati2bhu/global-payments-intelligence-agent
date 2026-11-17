import faiss
import numpy as np

# Extract only the embeddings

embedding_vectors = [
    item["embedding"]
    for item in all_embeddings
]

# Convert to numpy array

embeddings_array = np.array(
    embedding_vectors,
    dtype="float32"
)

dimension = len(embedding_vectors[0])

print(f"Dimension = {dimension}")

# Create index

index = faiss.IndexFlatL2(dimension)

# Add vectors

index.add(embeddings_array)

print(f"Vectors Stored = {index.ntotal}")
