#!/usr/bin/env python
import argparse

from gendiff.formatters.json_format import get_json_diff
from gendiff.formatters.plain_format import get_plain_diff
from gendiff.formatters.json_print_format import get_dict_diff
from gendiff.gendiff import generate_diff


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file)
    _type = args.format
    if _type == 'plain':
        print(get_plain_diff(diff))
    elif _type == 'json':
        print(get_json_diff(diff))
    elif _type is None:
        print(get_dict_diff(diff))
    else:
        raise Exception("Invalid format, run --help!")


if __name__ == '__main__':
    main()
