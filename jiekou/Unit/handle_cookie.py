import json
from  Unit.handle_json import read_json,write_value
import os
base_path = os.getcwd()

def get_cookie_value(cookie_key):
    data_json = read_json("/Config/cookie.json")
    return data_json[cookie_key]

def write_cookie(cookie_key, data):
    data_json = read_json("/Config/cookie.json")
    data_json[cookie_key] = data
    write_value(data_json)

if __name__ == '__main__':
    data = {"ccc":"ccc"}
    write_cookie("web",data)