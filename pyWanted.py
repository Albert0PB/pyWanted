"""
pyWanted: the most-wanted application
    Author:                     Alberto Pérez Bernabeu
    Starting date:              2024-04-23
    Last modification:          2024-04-26

Petitions:
    Please Mr. FBI, let me know:
        - How many requests I can make per minute.
        - How many pages I'd need to consult to get all suspects' info.
        - How many suspects are there in the current consulted page.
        (Via trial and error I've learnt this information, but you could have made it easier, goddamnit!)

Ideas for further versions:
    - Implement database management (SQL) or Python's Pandas to make easier consults (GROUP BY could help a lot here).
    - Filter suspects with known possible locations.
    - Filter suspects with active rewards.
    - Use Python's Matplotlib to display statistics.
    - Browse suspect information by name (and exporting it to a file).
    - Retrieve information about all the suspects relative to a certain field office.
    - Check the most-recently updated suspects information.

Abandoned ideas:
    - At first, recursion was used to deal with '429 Too Many Requests', repeating the check_ok_conn() function over
    and over until '200 OK' was received or an Error happened. This was replaced with a 'retries system', although
    further changes might be done in that bit of the program.

    - The 'retries system' failed catastrophically, so it had to be replaced by a 'preventive lapse system', meaning
    that after retrieving the information of one page, the program always waits a fixed lapse of time (>1 second)
    before attempting to make the next request. If the response sent by the FBI contained the data about how many
    requests can be made per minute or how much time one should wait until the next request, this could be done in
    a much more elegant way. God bless ´Murica!

Sources and useful info:
    FBI Wanted API: https://api.fbi.gov/wanted/v1/list
    FBI webpage with example of request with Python: https://www.fbi.gov/wanted/api
    About HTTP status codes: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
    CodeReview on "handling HTTP status codes":
        https://codereview.stackexchange.com/questions/282754/python-handling-different-http-status-codes-using-the-requests-library
    StackOverflow on "getting around 429":
        https://stackoverflow.com/questions/22786068/how-to-avoid-http-error-429-too-many-requests-python
    Exponential Backoff: https://en.wikipedia.org/wiki/Exponential_backoff
    A progress bar in Python: https://www.youtube.com/watch?v=x1eaT88vJUA
    Bar graphs with Matplotlib: https://www.youtube.com/watch?v=zwSJeIcRFuQ

"""
import requests
import json
import time


def welcome():
    print('\n==============================================')
    print('             _    _             _           _ ')
    print('            | |  | |           | |         | |')
    print(' _ __  _   _| |  | | __ _ _ __ | |_ ___  __| |')
    print("| '_ \| | | | |/\| |/ _` | '_ \| __/ _ \/ _` |")
    print('| |_) | |_| \  /\  / (_| | | | | ||  __/ (_| |')
    print('| .__/ \__, |\/  \/ \__,_|_| |_|\__\___|\__,_|')
    print('| |     __/ |                                 ')
    print('|_|    |___/                                  ')
    print('==============================================\n')
    print("Welcome to pyWanted:\nThe Python program to retrieve info \nabout the FBI Most-Wanted suspects.\n\n"
          "==============================================\n")


# Tuples not included because this is intended to be used when extracting data from a .json.
def depure_list(list_to_depure: list):
    result_list = list()
    for i in list_to_depure:
        if isinstance(i, list):
            for j in i:
                if isinstance(j, list):
                    for k in j:
                        result_list.append(k)
                else:
                    result_list.append(j)
        else:
            result_list.append(i)
    return result_list


def get_conn_status(source_url: str):
    try:
        return requests.get(source_url).status_code
    except requests.exceptions.HTTPError as e:
        exit("An error happened while it was being attempted to connect to the API.\n"
             f"Error: {e}")


def check_ok_conn(source_url):
    conn_status = get_conn_status(source_url)
    if conn_status // 10 != 20:
        exit(f"Something unexpected happened. HTTP Code status: {conn_status}")


def get_page_info(source_url: str, desired_info: str, page: int = 1):
    check_ok_conn(source_url)

    response = requests.get(source_url, params={'page': page})
    data = json.loads(response.content.decode())['items']

    return [suspect[desired_info] for suspect in data]


def get_field_offices(source_url, lapse_between_requests: (int, float) = 1.5):
    current_page = 1
    total_field_offices_amount = []
    while True:
        page_offices = get_page_info(source_url, desired_info='field_offices', page=current_page)
        if len(page_offices) == 0:
            break
        total_field_offices_amount.append(page_offices)
        time.sleep(lapse_between_requests)
        current_page += 1
    ready_list = depure_list(total_field_offices_amount)
    return ready_list, set(ready_list)


def suspects_amount_per_office(source_url):
    repetitions, distinct_offices = get_field_offices(source_url)
    suspect_count_per_office = dict()
    for office in distinct_offices:
        suspect_count_per_office.update({f'{office}': repetitions.count(office)})
        if office is None:
            suspect_count_per_office.update({'No office related': repetitions.count(None)})
    return suspect_count_per_office


def display_suspects_per_office(source_url):
    offices_info = suspects_amount_per_office(source_url)
    total = sum(list(offices_info.values()))
    for office in list(offices_info.keys()):
        print(f"{office}: {offices_info[office]} / {total}")


def main():
    url = 'https://api.fbi.gov/wanted/v1/list'
    # TODO: declare url as global variable

    welcome()
    # check_ok_conn(url)
    # print(get_conn_status(url))
    print(display_suspects_per_office(url))
    # get_field_offices(url)


if __name__ == "__main__":
    main()
