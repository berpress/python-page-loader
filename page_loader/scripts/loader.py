#!/usr/bin/env python
import argparse

from page_loader.client import get_response
from page_loader.utils import write_data_to_file, get_file_name_from_url


def main():
    parser = argparse.ArgumentParser(description='Page loader')
    parser.add_argument('url', type=str)
    parser.add_argument('-o', '--output', help='set download folder')
    args = parser.parse_args()
    output_file = args.output
    url = args.url
    response = get_response(url)
    if response.status_code == 200:
        file_name = get_file_name_from_url(url)
        write_data_to_file(response.text, file_name=file_name,
                           _dir=output_file)
    else:
        raise Exception(f"Cant load page {url}, status code is "
                        f"{response.status_code}")


if __name__ == '__main__':
    main()
