from Unit.handle_excel import excel_data
from Base.base_request import BaseRequest
from Unit.handle_result import handle_result,handle_result_json,get_result_json,write_token_header
from Unit.handle_cookie import get_cookie_value,write_cookie
from Unit.handle_header import get_header
from Unit.codition_data import get_data, get_depend_data
from Unit.handle_ini import hanle_ini
import json
import os
base_path = os.getcwd()
import pytest
import time
from py.xml import html


class RunMain:
    def run_case(self):
        rows=excel_data.get_rows()
        for i in range(rows):
            data = excel_data.get_rows_value(i+2)
            cookie = None
            get_cookie = None
            header = None
            depend_data = None
            is_run = data[hanle_ini.get_value('is_run', 'excel')]
            if is_run == 'yes':
                data1 = json.loads(data[hanle_ini.get_value('data1', 'excel')])
                is_depend = data[hanle_ini.get_value('is_depend', 'excel')]
                if is_depend:
                    depend_key = data[hanle_ini.get_value('depend_key', 'excel')]
                    depend_data = get_data(is_depend)
                    data1[depend_key] = depend_data
                method = data[hanle_ini.get_value('method', 'excel')]
                url = data[hanle_ini.get_value('url', 'excel')]
                is_header = data[hanle_ini.get_value('is_header', 'excel')]
                expect_method = data[hanle_ini.get_value('expect_method', 'excel')]
                expect_code = data[hanle_ini.get_value('expect_code', 'excel')]
                cookie_method = data[hanle_ini.get_value('cookie_method', 'excel')]
                if cookie_method == 'yes':
                    cookie = get_cookie_value('login')
                if cookie_method == 'write':
                    '''
                    必须是获取到cookie
                    '''
                    get_cookie={"is_cookie":"app"}
                if is_header == 'yes':
                    header = get_header()

                res = BaseRequest().run_main(method,url,data1,cookie,get_cookie,header)
                if is_header == "write":
                    write_token_header(res)
                message = get_depend_data(res, expect_code)
                print(message)
                if expect_method == "message":
                    config_message = handle_result(url, expect_code)
                    print(config_message)
                    if message == config_message:
                        excel_data.excel_write_data(i+2,13,'通过')
                    else:
                        excel_data.excel_write_data(i+2,13,'失败')
                    excel_data.excel_write_data(i + 2, 14, json.dumps(res))
                if expect_method == "json":
                    expect_result = get_result_json(url, expect_code)
                    result = handle_result_json(res,expect_result)
                    if result:
                        excel_data.excel_write_data(i+2,13,'通过')
                    else:
                        excel_data.excel_write_data(i + 2, 13, '失败')
                    excel_data.excel_write_data(i + 2, 14, json.dumps(res))


if __name__ == '__main__':
    # case_path = base_path + "/Run"
    # base_path = base_path + "/report/"
    # now_time = time.strftime("%Y_%m_%d_%H_%M_%S")
    # html_report = os.path.join(base_path, now_time, "report.html")
    # # xml_report = os.path.join(REPORT_DIR, now_time, "junit-xml.xml")
    # pytest.main(["-s", "-v", case_path,
    #              "--html=" + html_report,
    #              # "--junit-xml=" + xml_report,
    #              "--self-contained-html"]
    #             )
    RunMain().run_case()