import requests
from time import sleep

url = "https://jsonplaceholder.typicode.com/users"

attempt = 1

while attempt <= 3:
    try:
        response = requests.get(url, timeout=5)
        print("API Working")
        break
    # except requests.exceptions.Timeout:
    #     print("API Not Working, Retrying...")
    #     attempt += 1
    except Exception as e:
        print("Retrying...", attempt)
        attempt += 1
        sleep(2)