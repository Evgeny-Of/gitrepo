# https://www.worldweatheronline.com/

import requests
import json
from pprint import pprint

appid = '015d89a8bf4a4ff88f2153406222502'
# url = 'http://api.worldweatheronline.com/premium/v1/weather.ashx?key=015d89a8bf4a4ff88f2153406222502&q=London&format=json&num_of_days=5'
url = 'http://api.worldweatheronline.com/premium/v1/weather.ashx'

city = 'London'
file_format = 'json'
num_of_days_need = 5

params = {'q': city, 'key': appid, 'format': file_format, 'num_of_days': num_of_days_need}
response = requests.get(url, params=params)

with open('weather.json', 'w') as file:
    json.dump(response.json(), file)

pprint(response.json())
