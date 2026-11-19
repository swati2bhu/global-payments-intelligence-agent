import json
import requests
from bs4 import BeautifulSoup


with open(
    "sources.json",
    "r",
    encoding="utf-8"
) as file:

    data = json.load(file)


for source in data["sources"]:

    print("\n" + "=" * 60)
    print("SOURCE:", source["name"])
    print("URL:", source["url"])

    try:

        response = requests.get(
            source["url"],
            timeout=20
        )

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        links = []

        for link in soup.find_all("a"):

            href = link.get("href")

            if href:

                links.append(href)

        print(
            f"Links Found: {len(links)}"
        )

    except Exception as e:

        print(
            f"Error: {e}"
        )