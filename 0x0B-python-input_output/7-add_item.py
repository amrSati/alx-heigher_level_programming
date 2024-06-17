#!/usr/bin/python3

"""Script that adds all arguments to a Python list, then save to file
"""
from sys import argv
from os.path import exists

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    """Main function"""
    arg_list = []
    filename = "add_item.json"
    file_exists = exists(filename)

    if file_exists:
        arg_list = load_from_json_file(filename)

    if len(argv) > 1:
        arg_list.extend(argv[1:])

    save_to_json_file(arg_list, filename)


if __name__ == "__main__":
    main()
