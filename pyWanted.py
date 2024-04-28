"""
pyWanted: the most-wanted application
    Author:                     Alberto Pérez Bernabeu
    Starting date:              2024-04-23
    Last modification:          2024-04-28
"""

from utils.menu import Menu
from dependencies.suspects_per_office import display_suspects_per_office

url = 'https://api.fbi.gov/wanted/v1/list'


def welcome():
    print('\n=============================================='
          '\n             _    _             _           _ '
          '\n            | |  | |           | |         | |'
          '\n _ __  _   _| |  | | __ _ _ __ | |_ ___  __| |'
          "\n| '_ \| | | | |/\| |/ _` | '_ \| __/ _ \/ _` |"
          '\n| |_) | |_| \  /\  / (_| | | | | ||  __/ (_| |'
          '\n| .__/ \__, |\/  \/ \__,_|_| |_|\__\___|\__,_|'
          '\n| |     __/ |                                 '
          '\n|_|    |___/                                  '
          '\n==============================================\n'
          "\nWelcome to pyWanted:\n"
          "\nThe Python program to retrieve info\n"
          "\nabout the FBI Most-Wanted suspects.\n"
          "\n==============================================\n")


def main():
    global url
    # TODO: usar matplotlib
    # TODO: implementar menús y guardado en ficheros

    main_menu = Menu()
    saves_menu = Menu()

    welcome()

    display_suspects_per_office()


if __name__ == "__main__":
    main()
