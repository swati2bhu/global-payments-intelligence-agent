import requests

url = "https://www.rbi.org.in/Scripts/NotificationUser.aspx"

response = requests.get(url)

print("Status Code:", response.status_code)
print("Page Length:", len(response.text))
