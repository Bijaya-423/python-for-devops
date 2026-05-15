import requests

url = "https://jsonplaceholder.typicode.com/posts"


response = requests.get(url)

print("Status Code:", response.status_code)

if response.status_code == 200:
    print("API Working Fine.")
else:
    print("API Not Working.")