from typeguard import typechecked


class OptNotPosInt(Exception):
    def __init__(self, value):
        super().__init__(f"Picked option must be a positive integer. Inputted: '{value}'.")
        self.value = value


@typechecked
class Menu:
    def __init__(self, *options: str):
        self.__options = list(options)

    @property
    def options(self):
        return self.__options

    def __str__(self):
        menu_str = '\n'
        for i in range(len(self.__options)):
            menu_str += f'{i}- {self.__options[i]}\n'
        menu_str += '\n'
        return menu_str

    def pick_option(self):
        print(self)
        chosen_one = input('Pick your desired option (a positive integer must be inputted): ')

        try:
            chosen_one = int(chosen_one)
            if chosen_one < 0:
                raise OptNotPosInt(chosen_one)
        except ValueError:
            raise OptNotPosInt(chosen_one)
        except OptNotPosInt as e:
            print(f'Picked option must be a positive integer. Inputted: "{e.value}"')

        if 0 <= chosen_one <= len(self.__options):
            return chosen_one
