import os
import tempfile
from os import path
import urllib.parse
import re
from bs4 import BeautifulSoup
import logging

from loader.core.client import get_response, check_status

logger = logging.getLogger()


def write_to_file(data: str, file_name: str, file_dir=None,
                  file_type='html') -> str:
    """

    :param file_type: file type
    :param data: html to write in file
    :param file_name: name of file
    :param file_dir: file dir
    :return: path to file
    """
    file_dir = create_dir(file_dir)
    file_path = f"{path.join(file_dir, file_name)}.{file_type}"
    try:
        with open(f'{file_path}', "w") as file:
            file.write(data)
            logger.info('Write data to %s file', file_path)
    except IOError:
        logger.error('Error to create %s file', file_path)
        raise OSError('Error to create file')
    return file_path


def file_to_url(url: str) -> str:
    """
    :param url: url to get file name
    :return: file name wo .html
    """
    pars_file_name = urllib.parse.urlparse(url)
    if pars_file_name.hostname is None:
        file_name = os.path.splitext(pars_file_name.path[1:])[0]
    else:
        file_name = f'{pars_file_name.hostname}{pars_file_name.path}'
    file_name_only_w_d = re.sub(r'[^\w|\d]', '-', file_name)
    logger.info('Get file name %s from %s', file_name_only_w_d, url)
    return file_name_only_w_d


def page_conversion(data: str, path_to_file: str, url: str):
    """
    :param data: response.text
    :param path_to_file: path to file
    :param url: url
    :return: edited html and pair file path/download link
    """
    file_data = []
    soup = BeautifulSoup(data, 'html.parser')
    for tag in soup.findAll(re.compile("(link|script|img)")):
        link = tag.get('src')
        if link is not None and link[:1] == '/':
            logger.debug('Find link to file %s', link)
            url = urllib.parse.urlparse(url)
            logger.debug('Get url %s', url)
            download_link = f'{url.scheme}://{url.hostname}{link}'
            logger.info('Get download link %s', download_link)
            file_type = re.split(r'\.', link)[-1]
            file_name = file_to_url(link)
            logger.debug('File type is %s, file name is %s', file_type,
                         file_name)
            path_to_file = f'{path_to_file}_files'
            path_link = f"{path.join(path_to_file, file_name)}.{file_type}"
            file_data.append((download_link, file_name, path_to_file, file_type))
            tag['src'] = path_link
            logger.info('Change link to %s', path_link)
    return str(soup), file_data


def create_dir(file_dir=None) -> str:
    """
    :param file_dir:
    :return: return name of created dir or created random tmp dir
    """
    try:
        if file_dir is None:
            with tempfile.TemporaryDirectory() as fd:
                file_dir = fd
                logging.info('Create temporary %s folder', file_dir)
        elif not os.path.exists(file_dir):
            os.mkdir(file_dir)
            logging.info('Create %s folder', file_dir)
        else:
            logging.debug('Folder %s is exist', file_dir)
    except OSError:
        logger.error('Error to create %s folder', file_dir)
        raise OSError('Error to create folder')
    return file_dir


def save_page_data(data: list):
    """
    :param data: tuple(url, file_path, file_dir, file_type)
    """
    for i in data:
        url, file_path, file_dir, file_type = i
        res = get_response(url)
        check_status(res.status_code)
        write_to_file(res.text, file_name=file_path, file_dir=file_dir,
                      file_type=file_type)
