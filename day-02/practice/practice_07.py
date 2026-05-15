import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

data = response.json()

index = 0
while index <= len(data)-1:
    print(data[index])
    index += 1
    print("*"*50)

# print(len(data[0]))
# print(data[0])
# print("*"*50)
# print(data[1])
# print("*"*50)

# print(data[2])
# print("*"*50)

# print(data[3])
# print("*"*50)

# print(data[4])
# print("*"*50)

# print(data[5])
# print("*"*50)

# print(data[6])
# print("*"*50)

# print(data[7])
for user in data:
    print(user)