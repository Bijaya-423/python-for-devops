# api_key="pub_9f6825f4532f43d684a1dcc3baa5b8a8"
# base_url = "https://newsdata.io"
# end_point = "/api/1/latest?apikey=pub_9f6825f4532f43d684a1dcc3baa5b8a8&q=petrol"

# url = base_url + end_point



# import requests
# import json
# from time import sleep



# url = "https://newsdata.io/api/1/latest?apikey=pub_e5b7d5ea71c14f789a5ca5484e2888ea&q=petrol"

# def public_api():
#     headers = {
#         "User-Agent": "Mozilla/5.0"
#     }

#     try:
#         response = requests.get(url=url, headers=headers, timeout=15)
#         print("Status code:", response.status_code)

#         if response.status_code == 200:
#             print("Apis Working")
#             data = response.json()
#             print(data)

#         else:
#             print("Check code and api key or url.!")
#             print("Status code:", response.status_code)

#     except requests.exceptions.Timeout:
#         print("Request Timeout: Server not responding.")

#     except requests.exceptions.ConnectionError:
#         print("Connection Error: Chech Internet/DNS")

#     except Exception as e:
#         print("Error:", e)



# public_api()


import requests

response = requests.get(
    "https://google.com",
    timeout=10
)

print(response.status_code)