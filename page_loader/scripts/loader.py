#!/usr/bin/env python
import argparse
import logging
from os import path

from page_loader.utils.client import get_response
from page_loader.utils.utils import write_data_to_file, \
    get_file_name_from_url, set_local_links


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
    logging.basicConfig(level=logging_level)
    logging.debug('Set logging level %s (NOTSET 0, CRITICAL 50)',
                  logging_level)
    response = get_response(url)
    logging.debug('Output file is %s, download from %s', output_file, url)
    if response.status_code == 200:
        logging.debug('Status code is 200, GET %s', url)
        file_name = get_file_name_from_url(url)
        path_to_file = path.join(output_file, file_name)
        edited_html = set_local_links(response.text, path_to_file, url)
        write_data_to_file(edited_html, file_name=file_name,
                           _dir=output_file)
        logging.info('Finish write data to %s file in %s folder', file_name,
                     output_file)
    else:
        logging.error('Status code is %s, GET %s', response.status_code, url)
        raise Exception(f"Cant load page {url}, status code is "
                        f"{response.status_code}")


if __name__ == '__main__':
    main()
