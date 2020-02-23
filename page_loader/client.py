import requests
from requests import Response


def get_response(url: str) -> Response:
    return requests.get(url)
