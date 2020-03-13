import logging
from os import path

from loader.core.client import run_requests, check_status
from loader.core.logging import setup
from loader.core.files import convert_page, file_to_url, \
    write_to_file, create_dir, save_page_data
from loader.core.progress import ProgressBar

logger = logging.getLogger()


def save_html(url: str, output_file: str, level='INFO'):
    """
    :param url: download url
    :param output_file: file to write
    :param level: level logging
    """
    setup(level)
    logger.setLevel(level)
    bar = ProgressBar(level=logger.level)
    response = run_requests(url)
    bar.up(30)
    logger.debug('Output file is %s, download from %s', output_file,
                 url)
    # status_code = response.status_code
    check_status(response)
    logger.debug('Status code is 200, GET %s', url)
    file_name = file_to_url(url)
    if output_file is None:
        output_file = create_dir()
    path_to_file = path.join(output_file, file_name)
    bar.up(30)
    edited_html, page_data = convert_page(response.text, path_to_file, url)
    write_to_file(edited_html, file_name=file_name, file_dir=output_file)
    save_page_data(page_data)
    bar.up(40)
    logger.info('Finish write data to %s file in %s folder', file_name,
                output_file)
    bar.finish()
