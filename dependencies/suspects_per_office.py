from dependencies.general_use import get_page_info
from utils.depurators import depurate_list
from utils.name_generator import name_generator_by_datetime
import matplotlib. pyplot as plt
import time
import csv


def get_field_offices(lapse_between_requests: (int, float) = 2):
    current_page = 1
    total_field_offices_amount = []
    while True:
        print("\b" * 37, f"Obtaining information from page {current_page:2d}...")
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


def generate_suspects_per_office_files(target_directory: str = '/home/pywanted_data/'):
    offices_info = suspects_amount_per_office()
    sorted_offices_info = dict(sorted(offices_info.items()))
    print(f"Saving data files in {target_directory}")
    generate_bar_graph(list(sorted_offices_info.keys()), list(suspects_amount_per_office().values()), target_directory)
    generate_csv_file(sorted_offices_info, target_directory)
    print("Files generated satisfactorily.")
    # total = sum(list(offices_info.values()))
    #  for office in sorted_offices_names:
    #      print(f"{office}: {offices_info[office]} / {total}")


def generate_bar_graph(items: list[str], items_count: list[int], target_directory: str = '/home/pywanted_data/'):
    fig, ax = plt.subplots()
    plt.xticks(rotation=90)
    ax.tick_params(axis='x', which='major', pad=15, labelsize=5)
    ax.bar(items, items_count)
    plt.savefig(f"{target_directory}{name_generator_by_datetime('.png')}",
                bbox_inches='tight', dpi=200)
    plt.show(block=True)


def generate_csv_file(data_to_write: dict, target_directory: str = '/home/pywanted_data/'):
    csv_fields = data_to_write.keys()
    filename = f'{name_generator_by_datetime(".csv")}'
    with open(f'{target_directory}{filename}') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=csv_fields)
        writer.writeheader()
        writer.writerows(data_to_write)
