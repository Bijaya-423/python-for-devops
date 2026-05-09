import requests
import os
"""As a devops engineer , you will have to navigate through multiple external endpoints, and you should know how to switch them python."""


pj_url = "https://official-joke-api.appspot.com/random_joke"
dad_joke_url = "https://icanhazdadjoke.com/"

def joke_random(url_type, mood):
    headers = {
        "Accept": "application/json"
    }
    response = requests.get(url = url_type, headers=headers)

    if mood == "dad":
        final_joke = response.json()["joke"]
    if mood == "pj":
        final_joke = response.json()["setup"] + " " + response.json()["punchline"]
    # return final_joke
    # final_joke = response.json()
    return final_joke


mood = input("Which joke would you like to hear?  - ")

if mood == "dad":
    url_type = dad_joke_url
elif mood == "pj":
    url_type = pj_url
else:
    url_type = dad_joke_url

joke = joke_random(url_type, mood)
print(joke)