import json
import faiss
import numpy as np
import pickle
from pathlib import Path

# Existing FAISS files
FAISS_INDEX_PATH = "faiss_index.bin"
METADATA_PATH = "faiss_metadata.pkl"

# New embeddings
NEW_EMBEDDINGS_PATH = (
    "processed/new_downloaded_embeddings.json"
)

# -----------------------------
# Load Existing Index
# -----------------------------

index = faiss.read_index(
    FAISS_INDEX_PATH
)

with open(
    METADATA_PATH,
    "rb"
) as file:

    metadata = pickle.load(file)

# -----------------------------
# Load New Embeddings
# -----------------------------

with open(
    NEW_EMBEDDINGS_PATH,
    "r",
    encoding="utf-8"
) as file:

    new_records = json.load(file)

vectors = []

for record in new_records:

    vectors.append(
        record["embedding"]
    )

    metadata.append(
        {
            "document_name":
                record["document_name"],

            "document_type":
                record["document_type"],

            "source_file":
                record["source_file"],

            "chunk_id":
                record["chunk_id"],

            "chunk_text":
                record["chunk_text"]
        }
    )

# -----------------------------
# Add To Existing FAISS
# -----------------------------

vectors = np.array(
    vectors,
    dtype="float32"
)

index.add(vectors)

# -----------------------------
# Save Updated Index
# -----------------------------

faiss.write_index(
    index,
    FAISS_INDEX_PATH
)

with open(
    METADATA_PATH,
    "wb"
) as file:

    pickle.dump(
        metadata,
        file
    )

print(
    f"Added {len(vectors)} new chunks."
)

print(
    f"Total FAISS vectors: {index.ntotal}"
)