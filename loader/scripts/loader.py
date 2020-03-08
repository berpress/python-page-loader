#!/usr/bin/env python
import argparse
import logging.config
import sys
from http.client import HTTPException

from loader.core.engine import save_html

logger = logging.getLogger()

LOGGER_LEVEL = ['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG']


def main():
    parser = argparse.ArgumentParser(description='Page loader')
    parser.add_argument('url', type=str)
    parser.add_argument('-o', '--output', help='set download folder', type=str)
    parser.add_argument('-l', '--level',
                        help=f'set logging level {LOGGER_LEVEL}',
                        type=str)
    args = parser.parse_args()
    output_file = args.output
    url = args.url
    logging_level = args.level
    if logging_level is None:
        logging_level = 'INFO'
    elif logging_level not in LOGGER_LEVEL:
        sys.exit(1)
    save_html(url=url, output_file=output_file, level=logging_level)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(2)
    except OSError:
        sys.exit(3)
    except HTTPException:
        sys.exit(4)
    sys.exit(0)
