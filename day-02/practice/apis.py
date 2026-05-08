import requests

url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url=url)
# print(response.status_code)
# print(dir(response))
# print(response.text)
# print(type(response.json()))

# for key , value in response.json().items():
#     print(f"{key} : {value}")

for key, value in response.json().items():
    if key == "userId":
        if value == 1:
            print("Task is not completed yet.")

# for i in response.json().keys():
#     print(i)

# for i in response.json().values():
#     print(i)
