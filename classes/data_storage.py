from utils.connection_utils import check_ok_conn
from time import sleep
import pandas as pd
import datetime
import requests
import json

ENDPOINT = 'https://api.fbi.gov/wanted/v1/list'


class WantedApiInfo:
    __slots__ = ['__data_retrieved', '__consult_datetime']

    def __init__(self):
        self.__data_retrieved = self.__build_dataframe_from_api_info(self.__get_api_info())
        present = datetime.datetime.now()
        self.__consult_datetime = (f'{present.year}-{present.month}-{present.day}_'
                                   f'{present.hour:02d}:{present.minute:20d}')

    @property
    def data_retrieved(self):
        return self.__data_retrieved

    @property
    def consult_datetime(self):
        return self.__consult_datetime

    def get_info_by_keyword(self, keyword: str):
        return list(self.__data_retrieved[keyword])

    @staticmethod
    def __build_dataframe_from_api_info(api_info_list: list):
        indexed_info = dict()
        dataframe_index = api_info_list[0].keys()
        for i in dataframe_index:
            currently_indexed_data = list()
            for suspect in api_info_list:
                currently_indexed_data.append(suspect[i])
            indexed_info.update({i: currently_indexed_data})
        return pd.DataFrame(indexed_info)

    @staticmethod
    def __get_api_info():
        current_page = 1
        api_content = []
        while True:
            check_ok_conn(ENDPOINT)
            page_info = json.loads(requests.get(ENDPOINT, params={'page': current_page}).content.decode())['items']
            if len(page_info) == 0:
                break
            api_content.extend(page_info)
            print(f"\rObtaining information from page {current_page:2d}...", end="")
            sleep(2)
            current_page += 1
        return api_content
