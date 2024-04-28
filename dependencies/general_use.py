from utils.connection_utils import check_ok_conn
import requests
import json

url = 'https://api.fbi.gov/wanted/v1/list'


def get_page_info(desired_info: str, page: int = 1):

    check_ok_conn(url)
    response = requests.get(url, params={'page': page})
    data = json.loads(response.content.decode())['items']

    return [suspect[desired_info] for suspect in data]
