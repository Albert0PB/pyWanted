from dependencies.general_use import get_page_info
from utils.depurators import depurate_list
from utils.name_generator import name_generator_by_datetime
import matplotlib. pyplot as plt
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
    sorted_offices_info = dict(sorted(offices_info.items()))

    bar_graph_display(list(sorted_offices_info.keys()), list(suspects_amount_per_office().values()))

    #  for office in sorted_offices_names:
    #      print(f"{office}: {offices_info[office]} / {total}")


def bar_graph_display(items: list[str], items_count: list[int]):
    fig, ax = plt.subplots()
    plt.xticks(rotation=90)
    ax.tick_params(axis='x', which='major', pad=15, labelsize=5)
    ax.bar(items, items_count)
    plt.savefig(f"/home/alberto/1daw/prog/pyWanted/data_results/{name_generator_by_datetime()}",
                bbox_inches='tight', dpi=1450)
    plt.show(block=True)
    pass
