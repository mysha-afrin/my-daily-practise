import requests
import json


url = "https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow"

response = requests.get(url)



for data in response.json()['items']:
    if data['answer_count'] == 0:
        print(data['title'])
        print(data['link'])
    else:
        print("Skipped")