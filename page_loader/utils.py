import os
import tempfile
from os import path
import urllib.parse
import re
from bs4 import BeautifulSoup

from page_loader.client import get_response


def write_data_to_file(data: str, file_name: str, _dir=None, file_type='html') -> str:
    '''
    :param file_type: file type
    :param data: html to write in file
    :param file_name: name of file
    :param _dir: file dir
    :return: path to file
    '''
    if _dir is None:
        _dir = tempfile.TemporaryDirectory().name
    elif not os.path.exists(_dir):
        os.makedirs(_dir)
    file_path = f"{path.join(_dir, file_name)}.{file_type}"
    with open(f'{file_path}', "w") as file:
        file.write(data)
    return file_path


def get_file_name_from_url(url: str) -> str:
    '''
    :param url: url to get file name
    :return: file name wo .html
    '''
    pars_file_name = urllib.parse.urlparse(url)
    if pars_file_name.hostname is None:
        file_name = os.path.splitext(pars_file_name.path[1:])[0]
    else:
        file_name = f'{pars_file_name.hostname}{pars_file_name.path}'
    file_name_only_w_d = re.sub(r'[^\w|\d]', '-', file_name)
    return file_name_only_w_d


def set_local_links(data: str, path_to_file: str, url: str) -> str:
    '''
    :param data: response.text
    :param path_to_file: path to file
    :param url: url
    :return: edited text html
    '''
    soup = BeautifulSoup(data, 'html.parser')
    for tag in soup.findAll(re.compile("(link|script|img)")):
        link = tag.get('src')
        if link is not None and link[:1] == '/':
            url = urllib.parse.urlparse(url)
            download_link = f'{url.scheme}://{url.hostname}{link}'
            res = get_response(download_link)
            if res.status_code == 200:
                file_type = re.split(r'\.', link)[-1]
                file_name = get_file_name_from_url(link)
                path_link = write_data_to_file(data=res.text,
                                               file_name=file_name,
                                               _dir=f'{path_to_file}_files'
                                               , file_type=file_type)
                tag['src'] = path_link
    return str(soup)
