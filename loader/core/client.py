import logging

from http.client import HTTPException

import requests
from requests import Response

logger = logging.getLogger()


def get_response(url: str) -> Response:
    response = requests.get(url)
    logger.debug('GET url %s', url)
    return response


def check_status(status_code: int):
    """
    :param status_code: response status code
    :return: if status code is 400 or 500 then return HTTPException
    """
    if status_code == 200:
        logger.debug('Status code is 200')
        return status_code
    if 400 <= status_code <= 500:
        logger.error('Error, status code is 400 group')
        raise HTTPException('Check your url, status code is 400 group')
    if status_code >= 500:
        logger.error('Error, status code is 500 group')
        raise HTTPException('Server problem, status code is 500 group')
