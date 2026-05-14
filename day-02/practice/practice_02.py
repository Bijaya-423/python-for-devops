import requests
import json

url = "https://api.github.com/users"
try:
    response = requests.get(url)
    if response.status_code == 200:

        data = response.json()

        github_users = []

        print("\n----GitHub Users----")

        for user in data:
            user_info = {
                "Username": user["login"],
                "Profile url": user["html_url"],
                "User Type": user["type"],
                "Admin Status": user["site_admin"]
            }
            print(user_info)

            github_users.append(user_info)

        with open("github_users.json", "w") as file:
            json.dump(github_users, file, indent=8)

        print("\n Data saved into github_users.json")
    else:
        print(f"APi Failed with status code: {response.status_code}")
except requests.exceptions.Timeout:
    print("Connection Error: Check internet connection.")

except Exception as e:
    print("Error:", e)