import requests

url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url=url)
# print(response.status_code)
# print(dir(response))
print(response.text)
# print(response.json())