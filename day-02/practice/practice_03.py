import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

data = response.json()

for user in data:
    print("Name:", user['name'], "Email:", user['email'])
    print("Email:", user['email'])
    print("Company:", user['company']['city'])
    print("Address:", user['address']['street'], user['address']['suite'], user['address']['city'], user['address']['zipcode'])