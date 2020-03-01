import os
import tempfile
from os import path
import urllib.parse
import re
from bs4 import BeautifulSoup
import logging

from page_loader.utils.client import get_response, check_response_answer

logger = logging.getLogger()


def write_data_to_file(data: str, file_name: str, file_dir=None,
                       file_type='html') -> str:
    '''
    :param file_type: file type
    :param data: html to write in file
    :param file_name: name of file
    :param file_dir: file dir
    :return: path to file
    '''
    if file_dir is None:
        file_dir = tempfile.TemporaryDirectory().name
        logger.debug('Create temp folder %s', file_dir)
    elif not os.path.exists(file_dir):
        try:
            os.makedirs(file_dir)
            logging.debug('Create %s folder', file_dir)
        except OSError:
            logging.error('Error to create %s folder', file_dir)
            raise OSError('Error to create folder')
    file_path = f"{path.join(file_dir, file_name)}.{file_type}"
    logger.info('Create %s folder', file_dir)
    try:
        with open(f'{file_path}', "w") as file:
            file.write(data)
            logger.info('Write data to %s file', file_path)
    except IOError:
        logging.error('Error to create %s filer', file_path)
        raise OSError('Error to create file')
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
    logger.info('Get file name %s from %s', file_name_only_w_d, url)
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
            logger.debug('Find link to file %s', link)
            url = urllib.parse.urlparse(url)
            logger.debug('Get url %s', url)
            download_link = f'{url.scheme}://{url.hostname}{link}'
            logger.info('Get download link %s', download_link)
            res = get_response(download_link)
            status_code = res.status_code
            if not check_response_answer(status_code):
                logger.error('Error to get file, because status code is %s',
                             status_code)
            check_response_answer(res.status_code)
            logger.debug('Status code is  200, GET %s', download_link)
            file_type = re.split(r'\.', link)[-1]
            file_name = get_file_name_from_url(link)
            logger.debug('File type is %s, file name is %s', file_type,
                         file_name)
            path_link = write_data_to_file(data=res.text,
                                           file_name=file_name,
                                           file_dir=f'{path_to_file}_files',
                                           file_type=file_type)
            tag['src'] = path_link
            logger.info('Change link to %s', path_link)
    return str(soup)
