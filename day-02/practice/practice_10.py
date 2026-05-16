import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

data = response.json()

for user in data:
    print("Username:", user["username"])
    print("Latitude:", user["address"]["geo"]["lat"])
    print("Longitude:", user["address"]["geo"]['lng'])
    print("*"*50)