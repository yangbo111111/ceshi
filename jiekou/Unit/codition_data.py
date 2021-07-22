from Unit.handle_excel import excel_data
from jsonpath_rw import parse
import json


def split_data(data):
    """
    根据符号分隔获取值
    """
    case_id = data.split(">")[0]
    rule_data = data.split(">")[1]
    return case_id,rule_data


def depend_data(data):
    """
    根据获取行号和表格值
    """
    case_id = split_data(data)[0]
    row_number = excel_data.get_rows_number(case_id)
    cell_data = excel_data.get_cell_value(row_number, 14)
    cell_data = json.loads(cell_data)
    return cell_data


def get_depend_data(res_data, key):
    #  获取依赖字段
    # res_data = json.loads(res_data)
    json_exe = parse(key)
    madle = json_exe.find(res_data)
    # return [math.value for math in madle][0]
    for math in madle:
        return math.value


def get_data(data):
    # 获取依赖数据
    res_data = depend_data(data)
    rule_data = split_data(data)[1]
    return get_depend_data(res_data, rule_data)


if __name__ == '__main__':
    # data = {"type": "success", "code": "0", "message": "\u767b\u5f55\u6210\u529f", "data":
    #     {"orgName": "ad\u7ec4\u7ec7", "corpId": "0", "isFirstPwdModified": "true", "beoType": "0",
    #      "orgSimpleName": "null", "userName": "\u6768\u6ce2", "userId": "402880cd717c535001717c6b128101e0", "orgId":
    #          "402880b5752f851f01752f92b43100f5", "token":
    #          "eyJhbGciOiJIUzUxMiIsInppcCI6IkRFRiJ9.eNqMjjtOxDAQQO_iei3N-LN2tqOkoeICsT2OAosdxQnsCnEUGip67rTnYLLagpJu5s3T07yLp2UUB4GEFpPSEsl00mhjZBdJS5dyMrpTWikSO9HWwLIB5T3E5NBFqy0AbtM-oPIISMDi2BqL-Uin0DeSS32mIhvNrzRv134RB9yjB23QqJ2g03QDDq4g1nm6T5zYYrE89C_Ey-Xz-_LzxeRYh7E8nqcNTm-JycrxuxjrWjgtzn0ZQr3ha-cfP9d5-KMG66zK3mJmladOBaMRIFvx8QsAAP__.G4hsm43YCUW9Nhtfj7bBmJj_JDChMMSti5X6Rhkx2o-hf0y0WV3U9PtT6B484w4r75yS1sNbw2l60_l_EZlBAA", "expiresIn": 36000, "boeToken": "eyJhbGciOiJIUzUxMiIsInppcCI6IkRFRiJ9.eNqMjjtOxDAQQO_iei3N-LN2tqOkoeICsT2OAosdxQnsCnEUGip67rTnYLLagpJu5s3T07yLp2UUB4GEFpPSEsl00mhjZBdJS5dyMrpTWikSO9HWwLIB5T3E5NBFqy0AbtM-oPIISMDi2BqL-Uin0DeSS32mIhvNrzRv134RB9yjB23QqJ2g03QDDq4g1nm6T5zYYrE89C_Ey-Xz-_LzxeRYh7E8nqcNTm-JycrxuxjrWjgtzn0ZQr3ha-cfP9d5-KMG66zK3mJmladOBaMRIFvx8QsAAP__.G4hsm43YCUW9Nhtfj7bBmJj_JDChMMSti5X6Rhkx2o-hf0y0WV3U9PtT6B484w4r75yS1sNbw2l60_l_EZlBAA", "loginName": "yangbo", "refreshToken": "eyJhbGciOiJIUzUxMiIsInppcCI6IkRFRiJ9.eNqEjkEOwiAQRe_CWhKGUoruXJq4Ml4ApoNWTWmAmhrj3YXGvbvJm__fzJvd8sB2rFfGopMNt4CWqxYlN-A7rj2S6bbkED3bsDS7ElZCGiOw76DDtmmFgDppB9KAABIlOKRUgv5Bi7OJeA53Gnmi-KRYtzazHWgwolGg5IbRMlUghZZ6BRjidOiLosrmUtwjhnksNfay48WF9caJfKR0PVd72eQ4U-HB-wHpGC5Dhd4-Ev0kq_Hv958vAAAA__8.S73mymIOg29znpR901bJRgujcr_9xP_fmFFsVnVaHHh8F9tyRoHhvSlqh-1fLqoVOSUHxegJJykTkr0mxgyKnQ", "refreshExpiresIn": 2592000}}
    # data = {
    #     "a": "a1",
    #     "b": "b1",
    #     "c": [
    #         {
    #             "d": "d1"
    #         },
    #         {
    #             "d": "d2"
    #         }
    #     ]
    # }
    # key = 'c.[1].d'
    # get_depend_data(data,key)
    data = {"pageable":{"offset": "0"}}

    key = 'pageable'
    get_depend_data(data, key)