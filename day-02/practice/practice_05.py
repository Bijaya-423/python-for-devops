import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url=url)


data = response.json()

with open("posts.json", "w") as file:
    json.dump(data, file, indent=8)

with open("posts.json", "r") as file:
    data = json.load(file)
for post in data:
    print("Title:", post['title'])
    print("Body:", post['body'])
    print("User ID:", post['userId'])
    print("Post ID:", post['id'])
    