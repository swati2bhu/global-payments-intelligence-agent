import requests
from bs4 import BeautifulSoup

url = "https://www.rbi.org.in/Scripts/NotificationUser.aspx"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

text = soup.get_text()

print(text[:5000])
