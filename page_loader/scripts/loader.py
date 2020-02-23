#!/usr/bin/env python
import argparse

from page_loader.client import get_response


def main():
    parser = argparse.ArgumentParser(description='Page loader')
    parser.add_argument('url', type=str)
    parser.add_argument('-o', '--output', help='set download folder')
    args = parser.parse_args()
    output_file = args.output
    url = args.url
    response = get_response(url)
    if response.status_code == 200:
        pass
    else:
        raise Exception(f"Cant load page {url}, status code is "
                        f"{response.status_code}")
    pass


if __name__ == '__main__':
    main()
