import requests
import json

url = "https://api.github.com/users"

response = requests.get(url)

data = response.json()

github_users = []

print("\n----GitHub Users----")

for user in data:
    user_info = {
        "Username": user["login"]
    }