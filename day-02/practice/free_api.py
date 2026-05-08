import requests

API_KEY = "QRHE86JT0WVBQLHI"  #step 1 get api key

api_url = "https://www.alphavantage.co/"   #step 2 find a base url

# symbol = "IBM"
# symbol = "AMZN"
# query = f"query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}"

# print(api_url + query)


def get_stock(symbol):
    query = f"query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}"

    response = requests.get(url = api_url + query)

    # print(response.status_code)
    # print(response.json())

    # for key, value in response.json().items():
    #     if key == "Meta Data":
    #         for k, v in value.items():
    #             if k == "2. Symbol":
    #                 print(f"Stock symbol: {v}")

        # print(f"{key} : {value}")

    # for key in response.json().keys():
    #     print(key)
    
    # for value in response.json().values():
    #     print(value)
    # for key, value in response.json().items():
    #     if key == "Time Series (Daily)":
    #         for k, v in value.items():
    #             # print(f"Date: {k}")
    #             for i, j in v.items():
    #                 print(f"{i} : {j}")

    for key, value in response.json().items():
        if is_timeseries:
            if key == "Time Series (Daily)":
                for k, v in value.items():
                    print(f"Date: {k}")
                    for i, j in v.items():
                        print(f"{i} : {j}")



symbol = input("Enter the stock symbol:(AMZN, IBM, etc.):-  ")
is_timeseries = True
# is_timeseries = False
get_stock(symbol)