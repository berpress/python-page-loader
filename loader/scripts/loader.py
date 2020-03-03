#!/usr/bin/env python
import argparse
import logging.config
import sys

from loader.utils.engine_loader import write_html_to_files


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
    if write_html_to_files(url=url, output_file=output_file,
                           level=logging_level):
        sys.exit(0)
    sys.exit(1)


if __name__ == '__main__':
    main()
