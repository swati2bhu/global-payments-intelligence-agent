import faiss
import numpy as np

# Replace this with your embeddings list variable
embeddings_array = np.array(all_embeddings).astype("float32")

dimension = embeddings_array.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(embeddings_array)

print(f"Vectors Stored = {index.ntotal}")

faiss.write_index(index, "../vectorstore/payments_index.faiss")

print("FAISS Index Saved Successfully")