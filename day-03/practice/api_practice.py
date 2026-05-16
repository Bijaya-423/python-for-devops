import requests

url = "https://jsonplaceholder.typicode.com/users"

def get_users_info():
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        # print(data)
        for user in data:
            print(
                "Name:" , user["name"],
                "Username:", user["username"],
                "Email:", user["email"]
                                  
            )

get_users_info()
