from  Unit.handle_json import read_json,write_value
import os
base_path = os.getcwd()


def get_header():
    data = read_json("/Config/header.json")
    return data


if __name__ == '__main__':
    print(get_header())