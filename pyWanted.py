"""
pyWanted: the most-wanted application
    Author:                     Alberto Pérez Bernabeu
    Starting date:              2024-04-23
    Last modification:          2024-05-03
"""

from dependencies.data_storage import WantedApiInfo
from dependencies import data_savers, data_extractors
from utils.menu import Menu
from sys import exit

ENDPOINT = 'https://api.fbi.gov/wanted/v1/list'


def welcome():
    print("\n==============================================\n"
          "\nWelcome to pyWanted:\n"
          "\nThe Python program to retrieve info\n"
          "\nabout the FBI Most-Wanted suspects.\n"
          '\n=============================================='
          '\n             __    __            _           _ '
          "\n _ __  _   _/ / /\ \ \__ _ _ __ | |_ ___  __| |"
          "\n| '_ \| | | \ \/  \/ / _` | '_ \| __/ _ \/ _` |"
          '\n| |_) | |_| |\  /\  / (_| | | | | ||  __/ (_| |'
          '\n| .__/ \__, | \/  \/ \__,_|_| |_|\__\___|\__,_|'
          '\n|_|    |___/                                   '
          '\n==============================================\n')


def main():
    global ENDPOINT
    data_already_retrieved = False
    main_menu = Menu('Exit.', 'Get data from the FBI API.', 'Generate suspects per office.')
    welcome()

    while True:
        selected = main_menu.pick_option()
        match selected:
            case 0:
                exit('Thank you for using this program :)')
            case 1:
                data = WantedApiInfo()
                data_already_retrieved = True
                print('\rData retrieved successfully from the FBI API.\nRemember that, when selecting any consult '
                      'later, all files will be saved in the "data_results" folder.')
            case 2:
                if not data_already_retrieved:
                    print('\nMake sure to get data from the API (option 1 in the main menu) before selecting '
                          'any consult.')
                else:
                    extractor = data_extractors.SuspectsPerOfficeExtractor()
                    csv_saver, png_saver = data_savers.SaverCSV, data_savers.SaverPNG
                    csv_saver.save(datasource=data, data_extractor=extractor)
                    print('Data successfully saved (in folder "data_results").')


if __name__ == "__main__":
    main()
