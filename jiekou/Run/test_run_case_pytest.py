from Unit.handle_excel import excel_data
from Base.base_request import BaseRequest
from Unit.handle_result import handle_result,handle_result_json,get_result_json,write_token_header
from Unit.handle_cookie import get_cookie_value,write_cookie
from Unit.handle_header import get_header
from Unit.codition_data import get_data, get_depend_data
from Unit.handle_ini import hanle_ini
import os
import pytest
import json
base_path = os.getcwd()
data = excel_data.get_excel_data()


@pytest.mark.parametrize('value', data)
def test_main_case_pytest(value):
    cookie = None
    get_cookie = None
    header = None
    depend_data = None
    is_run = value[hanle_ini.get_value('is_run', 'excel')]
    case_id = value[hanle_ini.get_value('case_id', 'excel')]
    i = excel_data.get_rows_number(case_id)
    if is_run == 'yes':
        data1 = json.loads(value[hanle_ini.get_value('data1', 'excel')])
        is_depend = value[hanle_ini.get_value('is_depend', 'excel')]
        try:
            if is_depend:
                depend_key = value[hanle_ini.get_value('depend_key', 'excel')]
                depend_data = get_data(is_depend)
                data1[depend_key] = depend_data
            method = value[hanle_ini.get_value('method', 'excel')]
            url = value[hanle_ini.get_value('url', 'excel')]
            is_header = value[hanle_ini.get_value('is_header', 'excel')]
            expect_method = value[hanle_ini.get_value('expect_method', 'excel')]
            expect_code = value[hanle_ini.get_value('expect_code', 'excel')]
            cookie_method = value[hanle_ini.get_value('cookie_method', 'excel')]
            if cookie_method == 'yes':
                cookie = get_cookie_value('login')
            if cookie_method == 'write':
                '''
                必须是获取到cookie
                '''
                get_cookie = {"is_cookie": "app"}
            if is_header == 'yes':
                header = get_header()
            res = BaseRequest().run_main(method, url, data1, cookie, get_cookie, header)
            if is_header == "write":
                write_token_header(res)
            message = get_depend_data(res, expect_code)
            if expect_method == "message":
                config_message = handle_result(url, expect_code)
                assert message == config_message
                try:
                    excel_data.excel_write_data(i, 13, '通过')
                except Exception as e:
                    excel_data.excel_write_data(i, 13, '失败')
                excel_data.excel_write_data(i, 14, json.dumps(res))
            if expect_method == "json":
                expect_result = get_result_json(url, expect_code)
                result = handle_result_json(res, expect_result)
                try:
                    assert result
                    excel_data.excel_write_data(i, 13, '通过')
                except Exception as e:
                    excel_data.excel_write_data(i, 13, '失败')
                    raise e
                excel_data.excel_write_data(i, 14, json.dumps(res))
        except Exception as e:
            excel_data.excel_write_data(i, 13, '失败')
            raise e