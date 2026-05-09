import requests

api_key="4vvqs7nqu43c"

regionCode = "US-NV-001"

# US-NV-001
# US-NV-003
# US-NV-005
# US-NV-007
# US-NV-033

api_url = f"https://api.ebird.org/v2/data/obs/{regionCode}/recent"


def api_bird():
    headers = {
        "X-eBirdApiToken" : api_key
    }
    response = requests.get(api_url, headers=headers)
    print(response.status_code)
    # print(response.text)
    indexfor = int(input("Enter index:-"))
    final_hello = response.json()[indexfor]["comName"]
    print(final_hello)

    if response.status_code == 200:
        bird_name = response.json()

        for bird in bird_name:
            print(bird["comName"])
    else:
        print(response.text)


api_bird()





