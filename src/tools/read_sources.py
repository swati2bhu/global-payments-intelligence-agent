import json

with open("sources.json", "r", encoding="utf-8") as file:
    data = json.load(file)

print("\nSources Registered:\n")

for source in data["sources"]:
    print(f"Name     : {source['name']}")
    print(f"Category : {source['category']}")
    print(f"Priority : {source['priority']}")
    print(f"URL      : {source['url']}")
    print("-" * 50)