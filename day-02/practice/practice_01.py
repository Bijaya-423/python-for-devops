import requests
import json

url = "https://jsonplaceholder.typicode.com/users"

#send get request
response = requests.get(url)

data = response.json()
# print(data)
#empty list to store processed data

processed_data = []

print("\n ----------USER INFORMATION------------- \n")

for user in data:
    user_info = {
        "Name": user["name"],
        "Email": user["email"],
        "City": user["address"]["city"],
        "Company": user["company"]["name"]
    }
    print(user_info)

    processed_data.append(user_info)

with open("output.json", "w") as file:
    json.dump(processed_data, file, indent=4)

print("\nData Saved into output.json")