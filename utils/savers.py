from typeguard import typechecked  # TODO: instalar typeguard en el entorno virtual
from abc import ABC
import os


@typechecked
class Saver(ABC):
    def __init__(self, target_file_extension: str):
        self.__target_file_extension = target_file_extension

    @staticmethod
    def __check_source_file_exists(source_file):
        try:
            open(source_file)
            return True
        except FileNotFoundError:
            return False

    def __convert_extension(self, source_file):
        filename, file_extension = os.path.splitext(source_file)
        return filename + self.__target_file_extension

    def save(self, source_file):
        if self.__check_source_file_exists(source_file):
            try:
                with open(self.__convert_extension(source_file), 'w') and open(source_file, 'r'):
                    self.__convert_extension(source_file).write(source_file.read())
            except FileExistsError as e:
                print(f'Ya existe un fichero con ese nombre y extensión "{self.__target_file_extension}".')


class SaverCSV(Saver):
    def __init__(self):
        super().__init__('.csv')


class SaverJSON(Saver):
    def __init__(self):
        super().__init__('.json')


class SaverTXT(Saver):
    def __init__(self):
        super().__init__('.txt')


if __name__ == "__main__":
    pass
