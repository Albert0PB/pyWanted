import datetime


def name_generator_by_datetime():
    current_datetime = datetime.datetime.now()
    return (f'{current_datetime.year}-{current_datetime.month}-{current_datetime.day}_'
            f'{current_datetime.hour}:{current_datetime.minute}.svg')
