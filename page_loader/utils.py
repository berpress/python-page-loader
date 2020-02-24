import tempfile
from os import path
import urllib.parse
import re


def write_data_to_file(data: str, file_name: str, _dir=None) -> str:
    '''
    :param data: html to write in file
    :param file_name: name of file
    :param _dir: file dir
    :return: path to file
    '''
    if _dir is None:
        _dir = tempfile.TemporaryDirectory().name
    file_path = f"{path.join(_dir, file_name)}.html"
    with open(f'{file_path}.html', "w") as file:
        file.write(data)
    return file_path


def get_file_name_from_url(url: str) -> str:
    '''
    :param url: url to download
    :return: file name wo .html
    '''
    pars_file_name = urllib.parse.urlparse(url)
    file_name = pars_file_name.hostname + pars_file_name.path
    file_name_only_w_d = re.sub(r'[^\w|\d]', '-', file_name)
    return file_name_only_w_d
