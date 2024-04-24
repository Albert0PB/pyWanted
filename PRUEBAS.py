import requests
import json

response = requests.get('https://api.fbi.gov/wanted/v1/list', params={'pages': 1})


print(response.status_code)
