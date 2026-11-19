import requests
from bs4 import BeautifulSoup

url = "https://www.rbi.org.in/Scripts/NotificationUser.aspx"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

text = soup.get_text()

with open(
    "snapshots/rbi_snapshot.txt",
    "w",
    encoding="utf-8"
) as file:
    file.write(text)

print("Snapshot Saved Successfully")