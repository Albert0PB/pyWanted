from dependencies.general_use import get_page_info
from utils.depurators import depurate_list
from utils.name_generator import name_generator_by_datetime
import matplotlib. pyplot as plt
import time
import csv


def get_field_offices(lapse_between_requests: (int, float) = 2):
    current_page = 1
    total_field_offices_amount = []
    while current_page != 2:
        print(f"\rObtaining information from page {current_page:2d}...", end="")
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


def generate_suspects_per_office_files():
    offices_info = suspects_amount_per_office()
    sorted_offices_info = dict(sorted(offices_info.items()))
    print(f"\nSaving data files...")
    generate_csv_file(sorted_offices_info)
    generate_bar_graph(list(sorted_offices_info.keys()), list(offices_info.values()))
    print("Files generated satisfactorily.")
    # total = sum(list(offices_info.values()))
    #  for office in sorted_offices_names:
    #      print(f"{office}: {offices_info[office]} / {total}")


def generate_bar_graph(items: list[str], items_count: list[int]):
    fig, ax = plt.subplots()
    plt.xticks(rotation=90)
    ax.tick_params(axis='x', which='major', pad=15, labelsize=5)
    ax.bar(items, items_count)
    plt.savefig(fname=f"./data_results/{name_generator_by_datetime()}.png",
                bbox_inches='tight', dpi=200, format='png')
    plt.close()


def generate_csv_file(data_to_write: dict):
    csv_fields = data_to_write.keys()
    filename = f'./data_results/{name_generator_by_datetime()}'
    with open(f'{filename}.csv', mode='w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=csv_fields)
        writer.writeheader()
        writer.writerow(data_to_write)
