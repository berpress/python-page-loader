#!/usr/bin/env python
import argparse
import logging.config
from os import path
import sys
from progress.bar import Bar

from loader.utils.client import get_response, check_response_answer
from loader.utils.logger import run_logger
from loader.utils.utils import write_data_to_file, \
    get_file_name_from_url, set_local_links


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
    run_logger(logging_level)
    logger.setLevel(logging_level)
    logger.debug('Set logging level %s (NOTSET 0, CRITICAL 50)', logging_level)
    with Bar('Processing load page', max=100) as bar:
        bar.next()
        response = get_response(url)
        bar.next(5)
        logger.debug('Output file is %s, download from %s', output_file,
                     url)
        status_code = response.status_code
        if not check_response_answer(status_code):
            logger.error('Error, because status code is %s', status_code)
            sys.exit(1)
        logger.debug('Status code is 200, GET %s', url)
        bar.next(10)
        file_name = get_file_name_from_url(url)
        path_to_file = path.join(output_file, file_name)
        bar.next(15)
        edited_html = set_local_links(response.text, path_to_file, url)
        bar.next(35)
        write_data_to_file(edited_html, file_name=file_name,
                           file_dir=output_file)
        bar.next(30)
        logger.info('Finish write data to %s file in %s folder', file_name,
                    output_file)
        bar.next(4)
        bar.finish()
        sys.exit(0)


if __name__ == '__main__':
    main()
