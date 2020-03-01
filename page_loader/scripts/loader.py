#!/usr/bin/env python
import argparse
import logging.config
from os import path
import sys

from page_loader.utils.client import get_response
from page_loader.utils.logger import run_logger
from page_loader.utils.utils import write_data_to_file, \
    get_file_name_from_url, set_local_links

run_logger()
logger = logging.getLogger()


def main():
    parser = argparse.ArgumentParser(description='Page loader')
    parser.add_argument('url', type=str)
    parser.add_argument('-o', '--output', help='set download folder', type=str)
    parser.add_argument('-l', '--logging_level', help='set logging level '
                                                      'from 0 to 50',
                        type=int)
    args = parser.parse_args()
    output_file = args.output
    url = args.url
    logging_level = args.logging_level
    if logging_level is None:
        logging_level = 20
    logger.setLevel(logging_level)
    logger.debug('Set logging level %s (NOTSET 0, CRITICAL 50)', logging_level)
    response = get_response(url)
    logger.debug('Output file is %s, download from %s', output_file, url)
    if response.status_code == 200:
        logger.debug('Status code is 200, GET %s', url)
        file_name = get_file_name_from_url(url)
        path_to_file = path.join(output_file, file_name)
        edited_html = set_local_links(response.text, path_to_file, url)
        write_data_to_file(edited_html, file_name=file_name,
                           _dir=output_file)
        logger.info('Finish write data to %s file in %s folder', file_name,
                    output_file)
        sys.exit(0)
    else:
        logger.error("Can't load load page, status code is %s, GET  %s",
                     response.status_code, url)
        sys.exit(0)


if __name__ == '__main__':
    main()
