import json
from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

with open(
    "processed/new_downloaded_chunks.json",
    "r",
    encoding="utf-8"
) as file:

    chunks = json.load(file)

embedded_chunks = []

for item in chunks:

    embedding = model.encode(
        item["chunk_text"]
    ).tolist()

    embedded_chunks.append(
        {
            **item,
            "embedding": embedding
        }
    )

with open(
    "processed/new_downloaded_embeddings.json",
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        embedded_chunks,
        file,
        indent=4,
        ensure_ascii=False
    )

print(
    f"Embeddings Created: {len(embedded_chunks)}"
)