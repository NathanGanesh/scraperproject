import requests as requests

val = input("Input the URL:")

response = requests.get(val)

if response.status_code != 200 or not ("content" in response.json()):
    print("Invalid quote resource!")
else:
    print(response.json()["content"])