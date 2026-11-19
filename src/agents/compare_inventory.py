import json

with open(
    "inventory/current_inventory.json",
    "r",
    encoding="utf-8"
) as file:

    current_inventory = json.load(file)

with open(
    "inventory/previous_inventory.json",
    "r",
    encoding="utf-8"
) as file:

    previous_inventory = json.load(file)

current_urls = {
    item["url"]
    for item in current_inventory
}

previous_urls = {
    item["url"]
    for item in previous_inventory
}

new_urls = current_urls - previous_urls

print(
    f"New Publications Found: {len(new_urls)}"
)

for url in list(new_urls)[:20]:

    print(url)