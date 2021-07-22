from Unit.handle_json import get_value
from deepdiff import DeepDiff
from Unit.codition_data import get_depend_data
from  Unit.handle_json import read_json,write_value


# def handle_result(url,code):
#     data = get_value(url,"/Config/code_message.json")
#     print(data)
#     if data !=None:
#         for i in data:
#             message = i.get(str(code))
#             print(message)
#             if message:
#                 return message
#     return None

def handle_result(url,code):
    data = get_value(url,"/Config/code_message.json")
    if data !=None:
        message = get_depend_data(data, code)
        if message != None:
            return message
    return None


def get_result_json(url,status):
    data = get_value(url, "/Config/result.json")
    if data != None:
        for i in data:
            message = i.get(status)
            if message:
                return message
    return None


def handle_result_json(dict1, dict2):
    if isinstance(dict1,dict) and isinstance(dict2,dict):
        cmp_dict = DeepDiff(dict1, dict2, ignore_order=True).to_dict()
        if cmp_dict.get("dictionary_item_added"):
            return False
        else:
            return True
    else:
        return False


def write_token_header(data):
    data_json = read_json("/Config/header.json")
    code = "data.token"
    token = get_depend_data(data, code)
    Authorization = "Bearer " + token
    data_json["Authorization"] = Authorization
    write_value(data_json, "/Config/header.json")




if __name__ == '__main__':
    handle_result("/flexoffice/api/w/info/list", "pageable.offset")
