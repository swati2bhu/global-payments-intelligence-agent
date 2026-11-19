import json
from pathlib import Path

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

# -----------------------------------
# Load Documents
# -----------------------------------

with open(
    "processed/new_downloaded_content.json",
    "r",
    encoding="utf-8"
) as file:

    documents = json.load(file)

all_chunks = []

# -----------------------------------
# Chunk Every Document Separately
# -----------------------------------

for document in documents:

    content = document["content"]

    start = 0
    chunk_id = 1

    while start < len(content):

        end = start + CHUNK_SIZE

        chunk_text = content[start:end]

        all_chunks.append(
            {
                "document_name":
                    document["document_name"],

                "document_type":
                    document["document_type"],

                "source_file":
                    document["source_file"],

                "chunk_id":
                    chunk_id,

                "chunk_text":
                    chunk_text
            }
        )

        start += (
            CHUNK_SIZE
            - CHUNK_OVERLAP
        )

        chunk_id += 1

# -----------------------------------
# Save Chunks
# -----------------------------------

Path(
    "processed"
).mkdir(
    exist_ok=True
)

with open(
    "processed/new_downloaded_chunks.json",
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        all_chunks,
        file,
        indent=4,
        ensure_ascii=False
    )

print(
    f"Chunks Created: {len(all_chunks)}"
)