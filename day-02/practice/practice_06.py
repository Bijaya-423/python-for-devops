import requests
import json

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

data = response.json()

for user in data:
    if user["address"]['city'] == "South Christy":
        print(user["name"])
        print(user["email"])
    # print("Address:", user["address"]["city"])

    with open("user1.json", "w") as file:
        json.dump(user, file, indent=8)
    print("Data saved to user.json")