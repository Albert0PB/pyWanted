"""
pyWanted: the most-wanted application
    Author:                     Alberto Pérez Bernabeu
    Starting date:              2024-04-23
    Last modification:          2024-04-30
"""

from dependencies.suspects_per_office import generate_suspects_per_office_files

url = 'https://api.fbi.gov/wanted/v1/list'


def welcome():
    print("\n===============================================\n"
          "\nWelcome to pyWanted:\n"
          "\nThe Python program to retrieve info\n"
          "\nabout the FBI Most-Wanted suspects.\n"
          '\n==============================================='
          '\n             __    __            _           _ '
          "\n _ __  _   _/ / /\ \ \__ _ _ __ | |_ ___  __| |"
          "\n| '_ \| | | \ \/  \/ / _` | '_ \| __/ _ \/ _` |"
          '\n| |_) | |_| |\  /\  / (_| | | | | ||  __/ (_| |'
          '\n| .__/ \__, | \/  \/ \__,_|_| |_|\__\___|\__,_|'
          '\n|_|    |___/                                   '
          '\n===============================================\n')


def main():
    global url

    welcome()

    generate_suspects_per_office_files()


if __name__ == "__main__":
    main()
