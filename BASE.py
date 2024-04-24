import requests
import json

offices_list = []
suspects_offices = []

URL = 'https://api.fbi.gov/wanted/v1/list'
PAGES_NUM = 49  # +1
SUSPECTS_PER_PAGE = 20

for page in range(PAGES_NUM):
    response = requests.get(URL, params={'page': page})
    data = json.loads(response.content)

    for suspect in range(SUSPECTS_PER_PAGE):
        suspects_offices.append(data['items'][suspect]['field_offices'])

for i in suspects_offices:
    print(i)

# aaa
