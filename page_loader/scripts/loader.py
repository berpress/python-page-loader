#!/usr/bin/env python
import argparse
from os import path

from page_loader.client import get_response
from page_loader.utils import write_data_to_file, get_file_name_from_url, \
    set_local_links


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
        path_to_file = path.join(output_file, file_name)
        edited_html = set_local_links(response.text, path_to_file, url)
        write_data_to_file(edited_html, file_name=file_name,
                           _dir=output_file)
    else:
        raise Exception(f"Cant load page {url}, status code is "
                        f"{response.status_code}")


if __name__ == '__main__':
    main()
