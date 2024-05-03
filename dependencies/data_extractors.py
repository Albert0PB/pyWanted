from dependencies.data_storage import WantedApiInfo
from typeguard import typechecked
from utils.depurators import depurate_list
from abc import ABC
import collections


@typechecked
class DataExtractor(ABC):

    def obtain_from(self, datasource: WantedApiInfo):
        pass


@typechecked
class SuspectsPerOfficeExtractor(DataExtractor):
    def obtain_from(self, datasource: WantedApiInfo):
        return self.__suspects_amount_per_office(depurate_list(datasource.get_info_by_keyword('field_offices')))

    @staticmethod
    def __suspects_amount_per_office(offices_repetitions_list: list[str, None]):
        distinct_offices = set(offices_repetitions_list)
        suspect_count_per_office = dict()
        for office in distinct_offices:
            if office is None:
                suspect_count_per_office.update({'No office related': offices_repetitions_list.count(None)})
            else:
                suspect_count_per_office.update({f'{office}': offices_repetitions_list.count(office)})
        return dict(collections.OrderedDict(sorted(suspect_count_per_office.items())))
