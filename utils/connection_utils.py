import requests


def get_conn_status(source_url: str):
    try:
        return requests.get(source_url).status_code
    except requests.exceptions.HTTPError as e:
        exit("An attempt to connect to the provided URL resulted in an error.\n"
             f"Error: {e}")


def check_ok_conn(source_url):
    conn_status = get_conn_status(source_url)
    if conn_status // 100 != 2:
        exit(f"Something unexpected happened. HTTP Code status: {conn_status}")
