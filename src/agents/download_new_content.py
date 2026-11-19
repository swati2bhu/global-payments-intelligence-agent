import json
import os
import requests

PDF_FOLDER = "downloads/pdfs"
HTML_FOLDER = "downloads/html"

os.makedirs(PDF_FOLDER, exist_ok=True)
os.makedirs(HTML_FOLDER, exist_ok=True)

with open(
    "inventory/new_publications.json",
    "r",
    encoding="utf-8"
) as file:

    publications = json.load(file)

for item in publications:

    url = item["url"]

    source = item["source"]

    title = item["title"]

    safe_name = (
        title.replace("/", "_")
             .replace("\\", "_")
             .replace(":", "_")
             .replace("?", "_")
             .replace("*", "_")
    )

    try:

        response = requests.get(
            url,
            timeout=30
        )

        if ".pdf" in url.lower():

            file_path = (
                f"{PDF_FOLDER}/{safe_name}.pdf"
            )

            with open(
                file_path,
                "wb"
            ) as file:

                file.write(response.content)

            print(
                f"PDF Downloaded: {title}"
            )

        else:

            file_path = (
                f"{HTML_FOLDER}/{safe_name}.html"
            )

            with open(
                file_path,
                "w",
                encoding="utf-8"
            ) as file:

                file.write(response.text)

            print(
                f"HTML Captured: {title}"
            )

    except Exception as e:

        print(
            f"Failed: {title}"
        )

        print(e)