"""
pyWanted: the most-wanted application
    Author:                     Alberto Pérez Bernabeu
    Starting date:              2024-04-23
    Last modification:          2024-04-24

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

Sources and useful info:
    FBI Wanted API: https://api.fbi.gov/wanted/v1/list
    FBI webpage with example of request with Python: https://www.fbi.gov/wanted/api

    About HTTP status codes: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
    StackOverflow on "getting around 429":
        https://stackoverflow.com/questions/22786068/how-to-avoid-http-error-429-too-many-requests-python

    Exponential Backoff: https://en.wikipedia.org/wiki/Exponential_backoff

"""
import requests
import json
import time


def check_ok_conn(target_url: str, max_retries: int = 7, retry_lapse: int = 15):
    for retry in range(max_retries):
        status_code = requests.get(target_url).status_code
        match status_code:
            case 200:
                return
            case 429:  # Too many requests in a short period of time.
                deal_with_429(max_retries, retry, retry_lapse)

            case 400 | 401 | 403 | 404:
                raise ConnectionError(f"Connection or permission issues. Code: {status_code}")
            case _:
                raise NotImplementedError(f"No implementation for the received code '{status_code}'. "
                                          f"Please check manually.")


# TODO: check this when I feel less tired
def deal_with_429(max_retries, retry, retry_lapse):
    if retry == max_retries - 1:
        raise ConnectionError("Too many retries. Try again WAY later.")
    print("Too many requests; retrying connection...")
    time.sleep(retry_lapse)
    retry_lapse *= 1.2


# Returns an array with the data in the selected column (target_info). By default, it aims to retrieve all the
# field offices mentioned in the place (including Nones).
# In further versions, "target_info = 'all'" could be implemented to retrieve the full page info.
def get_page_info(target_url: str, target_info: str = 'field_offices', page: int = 1):
    response = requests.get(target_url, params={'page': page}).content.decode()
    data = json.loads(response)['items']

    field_offices_in_page = [suspect[target_info] for suspect in data]
    return field_offices_in_page


def get_field_offices():  # TODO: A very specific function that gets all the operating offices and the nº of suspects.
    pass


def main():
    url = 'https://api.fbi.gov/wanted/v1/list'

    # TODO: An user-friendly welcome.

    while True:
        # We try to establish a connection to the FBI. If an Error takes place, the program stops and lets the user
        # know what happened.
        try:
            check_ok_conn(url)

        except ConnectionError as e:
            exit(f"Something happened meanwhile the connection was being established. Error: \n\t'{e}'")

        except NotImplementedError as e:
            exit("There was a problem with the connection or it was established but the HTTP code "
                 f"received was not expected. Please check manually. Error: \n\t'{e}'")

        # TODO: instead of giving an exit, in future versions there should be other kind of management.

        else:
            print("Smooth connection :)")  # A supportive comment to well-behaving connections.

        print(get_page_info(url))
        break


if __name__ == "__main__":
    main()
