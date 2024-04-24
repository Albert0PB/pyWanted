import requests
import json
import pandas

URL = 'https://api.fbi.gov/wanted/v1/list'
target_data = 'field_offices'
total_suspects = json.loads(requests.get(URL).content)['total']

TOTAL_PAGES = 50  # CUIDADO, ESTO PUEDE VARIAR Y HAY QUE CONTROLARLO EN LAS ITERACIONES SOBRE LA REQUEST
SUSPECTS_PER_PAGE = 20  # ESTO TAMBIÉN PODRÍA LLEGAR A VARIAR. SIEMPRE CAUSARÁ ERROR EN LA ÚLTIMA PÁGINA


def fbiwanted_request_by_page(url, page):
    return requests.get(url, params={'page': page})


def fbiwanted_full_request():
    responses = dict()





data = json.loads(response.content)

sus_list = []

for suspect in range(SUSPECTS_PER_PAGE):
    current = data['items'][suspect][target_data]
    print(current)
    sus_list.append(current)

