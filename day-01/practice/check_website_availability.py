import requests
from time import sleep

url = "https://www.google.com"
while True:
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Website is running fine!")
    except:
        print("website is down")

    sleep(60)
    