from typeguard import typechecked
from classes.data_storage import WantedApiInfo
from classes.data_extractors import DataExtractor
from abc import ABC
import matplotlib.pyplot as plt
import csv


@typechecked
class Saver(ABC):
    @classmethod
    def save(cls, datasource: WantedApiInfo, data_extractor: DataExtractor):
        pass


@typechecked
class SaverCSV(Saver):
    @classmethod
    def save(cls, datasource: WantedApiInfo, data_extractor: DataExtractor):
        data_to_save = data_extractor.obtain_from(datasource)
        cls.__write_csv(data_to_save, datasource.consult_datetime)

    # TODO: change the way the CSV is writen. Suspects per office should have two columns and fifty-ish rows.
    @staticmethod
    def __write_csv(data_to_write, filename):
        csv_fields = data_to_write.keys()
        filename = f'./data_results/{filename}'
        with open(f'{filename}.csv', mode='w') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=csv_fields)
            writer.writeheader()
            writer.writerow(data_to_write)


@typechecked
class SaverBarGraphPNG(Saver):
    @classmethod
    def save(cls, datasource: WantedApiInfo, data_extractor: DataExtractor):
        data_to_save = data_extractor.obtain_from(datasource)
        cls.__generate_bar_graph(data_to_save, datasource.consult_datetime)

    @staticmethod
    def __generate_bar_graph(data: dict, filename: str):
        items, count = list(data.keys()), list(data.values())
        fig, ax = plt.subplots()
        plt.xticks(rotation=90)
        ax.tick_params(axis='x', which='major', pad=15, labelsize=5)
        ax.bar(items, count)
        plt.savefig(fname=f"./data_results/{filename}.png",
                    bbox_inches='tight', dpi=200, format='png')
        plt.close()
