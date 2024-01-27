import requests
import json


class GetRequester:

    def __init__(self, url):
        self.url = url
       

    def get_response_body(self):
        response = requests.get(self.url)
        print(response.text)
        return response
       

    def load_json(self):
        response = self.get_response_body()
        data = (json.loads(response.text))
        print(data)
        return data
       

url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
response  = GetRequester(url)
response.get_response_body()
response.load_json()
       
    

       
    