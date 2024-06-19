import requests
import json 
response_api = requests.get('https://fakestoreapi.com/products/1')
print(response_api.status_code)
data = response_api.text
print(data)
# json_format=json.loads(data)
# print(json_format)