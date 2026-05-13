import requests
import time


url = "https://api.github.com/2"

attempt = 1

while attempt <= 5:
    try:
        response = requests.get(url)

        if response.status_code == 200:
            print("API is up and running!")
            break
    except Exception as e:
        # print(f"Attempt {attempt} failed: {e}")
        # attempt += 1
        # time.sleep(2)
        print("Error:", e)

        print("Retrying in 2 seconds...")

        attempt += 1
        time.sleep(2)