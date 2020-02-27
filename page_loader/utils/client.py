import logging

import requests
from requests import Response


def get_response(url: str) -> Response:
    response = requests.get(url)
    logging.debug('GET url %s', url)
    return response
