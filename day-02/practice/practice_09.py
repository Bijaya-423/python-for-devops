import requests
from time import sleep


url = "https://jsonplaceholder.typicode.com/users"

while True:
    try:
        response = requests.get(url)

        print("API Status:", response.status_code)
    except :
        print("API Down")
    sleep(10)