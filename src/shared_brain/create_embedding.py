from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import ollama
import faiss
import numpy as np
import json

# =====================================
# Read PDF
# =====================================

pdf_path = r"D:\paymentsCopilot\docs\1794363534901.pdf"

reader = PdfReader(pdf_path)

all_text = ""

for page in reader.pages:
    text = page.extract_text()

    if text:
        all_text += text

print(f"Document Length = {len(all_text)}")

# =====================================
# Chunking
# =====================================

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = splitter.split_text(all_text)

print(f"Total Chunks = {len(chunks)}")

# =====================================
# Embedding Generation
# =====================================

all_embeddings = []

for i, chunk in enumerate(chunks):

    response = ollama.embed(
        model="nomic-embed-text",
        input=chunk
    )

    embedding = response["embeddings"][0]

    all_embeddings.append(
        {
            "chunk_id": i,
            "text": chunk,
            "embedding": embedding
        }
    )

    if i % 20 == 0:
        print(f"Completed Chunk {i}")

print("\nEmbedding Generation Complete")

print(
    f"Total Embeddings Created = "
    f"{len(all_embeddings)}"
)

print(
    f"Embedding Dimension = "
    f"{len(all_embeddings[0]['embedding'])}"
)

# =====================================
# Prepare vectors for FAISS
# =====================================

embedding_vectors = [
    item["embedding"]
    for item in all_embeddings
]

embeddings_array = np.array(
    embedding_vectors,
    dtype="float32"
)

# =====================================
# Create FAISS Index
# =====================================

dimension = embeddings_array.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(embeddings_array)

print(f"Vectors Stored = {index.ntotal}")

# =====================================
# Save FAISS Index
# =====================================

faiss.write_index(
    index,
    "../vectorstore/payments_index.faiss"
)

print("FAISS Index Saved Successfully")

# =====================================
# Save Metadata
# =====================================

metadata = [
    {
        "chunk_id": item["chunk_id"],
        "text": item["text"]
    }
    for item in all_embeddings
]

with open(
    "../vectorstore/chunk_metadata.json",
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        metadata,
        file,
        ensure_ascii=False,
        indent=4
    )

print("Chunk Metadata Saved Successfully")
