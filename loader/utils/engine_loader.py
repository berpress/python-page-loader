import logging
import sys
from os import path

from progress.bar import ChargingBar

from loader.client import get_response, check_response_answer
from loader.logger import run_logger
from loader.utils.utils import set_local_links, get_file_name_from_url, \
    write_data_to_file

logger = logging.getLogger()


def write_html_to_files(url: str, output_file: str, level=20):
    '''
    :param url: download url
    :param output_file: file to write
    :param level: level logging
    :return: None
    '''
    run_logger(level)
    logger.setLevel(level)
    if level > 20:
        bar = ChargingBar('Processing', max=100)
    response = get_response(url)
    if level > 20:
        bar.next(30)
    logger.debug('Output file is %s, download from %s', output_file,
                 url)
    status_code = response.status_code
    if not check_response_answer(status_code):
        logger.error('Error, because status code is %s', status_code)
        sys.exit(1)
    logger.debug('Status code is 200, GET %s', url)
    file_name = get_file_name_from_url(url)
    path_to_file = path.join(output_file, file_name)
    if level > 20:
        bar.next(30)
    edited_html = set_local_links(response.text, path_to_file, url)
    write_data_to_file(edited_html, file_name=file_name, file_dir=output_file)
    if level > 20:
        bar.next(40)
    logger.info('Finish write data to %s file in %s folder', file_name,
                output_file)
    if level > 20:
        bar.finish()
