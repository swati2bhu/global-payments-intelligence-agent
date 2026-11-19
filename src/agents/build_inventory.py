import json
import requests
from bs4 import BeautifulSoup

inventory = []

with open(
    "sources.json",
    "r",
    encoding="utf-8"
) as file:

    data = json.load(file)

for source in data["sources"]:

    try:

        response = requests.get(
            source["url"],
            timeout=20
        )

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        for link in soup.find_all("a"):

            href = link.get("href")

            title = link.get_text(
                strip=True
            )

            if href and title:

                inventory.append(
                    {
                        "source": source["name"],
                        "title": title,
                        "url": href
                    }
                )

    except Exception as e:

        print(
            f"Error in {source['name']}: {e}"
        )

with open(
    "inventory/current_inventory.json",
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        inventory,
        file,
        indent=4,
        ensure_ascii=False
    )

print(
    f"Inventory Created: {len(inventory)} items"
)