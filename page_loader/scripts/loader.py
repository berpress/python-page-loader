#!/usr/bin/env python
import argparse
import logging.config
from os import path
import sys
from progress.bar import Bar

from page_loader.utils.client import get_response, check_response_answer
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
    with Bar('Processing', max=10) as bar:
        for i in range(10):
            bar.next()
            response = get_response(url)
            bar.next(4)
            logger.debug('Output file is %s, download from %s', output_file,
                         url)
            status_code = response.status_code
            if not check_response_answer(status_code):
                logger.error('Error, because status code is %s', status_code)
                sys.exit(1)
            logger.debug('Status code is 200, GET %s', url)
            bar.next()
            file_name = get_file_name_from_url(url)
            path_to_file = path.join(output_file, file_name)
            bar.next()
            edited_html = set_local_links(response.text, path_to_file, url)
            bar.next()
            write_data_to_file(edited_html, file_name=file_name,
                               file_dir=output_file)
            bar.next()
            bar.finish()
            logger.info('Finish write data to %s file in %s folder', file_name,
                        output_file)
            sys.exit(0)


if __name__ == '__main__':
    main()
