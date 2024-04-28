from dependencies.general_use import get_page_info
from utils.depurators import depurate_list
import time


def get_field_offices(lapse_between_requests: (int, float) = 2):
    current_page = 1
    total_field_offices_amount = []
    while True:
        page_offices = get_page_info(desired_info='field_offices', page=current_page)
        if len(page_offices) == 0:
            break
        total_field_offices_amount.append(page_offices)

        time.sleep(lapse_between_requests)
        current_page += 1
    return depurate_list(total_field_offices_amount)


def suspects_amount_per_office():
    total_offices_repetitions = get_field_offices()
    distinct_offices = set(total_offices_repetitions)
    suspect_count_per_office = dict()
    for office in distinct_offices:
        if office is None:
            suspect_count_per_office.update({'No office related': total_offices_repetitions.count(None)})
        else:
            suspect_count_per_office.update({f'{office}': total_offices_repetitions.count(office)})
    return suspect_count_per_office


def display_suspects_per_office():
    offices_info = suspects_amount_per_office()
    total = sum(list(offices_info.values()))
    sorted_offices_names = sorted(list(offices_info.keys()))
    for office in sorted_offices_names:
        print(f"{office}: {offices_info[office]} / {total}")
