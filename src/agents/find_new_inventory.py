import json

# Load current inventory
with open(
    "inventory/current_inventory.json",
    "r",
    encoding="utf-8"
) as file:

    current_inventory = json.load(file)

# Load previous inventory
with open(
    "inventory/previous_inventory.json",
    "r",
    encoding="utf-8"
) as file:

    previous_inventory = json.load(file)

# Create lookup sets
previous_urls = {
    item["url"]
    for item in previous_inventory
}

new_publications = []

for item in current_inventory:

    if item["url"] not in previous_urls:

        new_publications.append(item)

print(
    f"\nNew Publications Found: {len(new_publications)}"
)

for publication in new_publications:

    print("\n--------------------------------")
    print("SOURCE :", publication["source"])
    print("TITLE  :", publication["title"])
    print("URL    :", publication["url"])

# Save results
with open(
    "inventory/new_publications.json",
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        new_publications,
        file,
        indent=4,
        ensure_ascii=False
    )