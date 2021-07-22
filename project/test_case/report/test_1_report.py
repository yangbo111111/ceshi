# from selenium.common.exceptions import NoSuchElementException
# from test_function.report.report_function import start_report,report_add,except_option,report_modify,report_query,report_del
# from page.report.report_page import  Reportpage
# from test_function.public_function import mycsv,windowsOption
# import time
# import pytest
# now = None
#
#
# def test_init(browser):
#     """
#     ======汇报菜单开始测试.....=======
#     """
#     # 打开浏览器，点击汇报/我的汇报/其它
#     start_report(browser)
#     global now
#     now = browser.current_window_handle
#
#
# @pytest.mark.dependency()
# def test_01(browser):
#     """
#     其它汇报列表页面校验
#     预期：列表新增按钮存在，页面显示正常
#     """
#     page = Reportpage(browser)
#     try:
#         result1 = page.list_addbutton.is_displayed()
#     except NoSuchElementException:
#         result1 = False
#     assert result1 == True
#
#
# @pytest.mark.dependency(depends=["test_01"])
# def test_02(browser):
#
#     """
#         发送汇报页面校验
#         步骤：1、点击新增按钮
#             2、填写标题和内容
#     """
#     user = mycsv()
#     title = user.read(2,0)
#     content = user.read(2,1)
#     page = Reportpage(browser)
#     # 如果页面出错，关闭新增页面
#     try:
#         report_add(browser, title, content, 0)
#         if page.report_title.is_displayed():
#             result = True
#         else:
#             result = False
#         browser.close()
#         # 切换回列表页面
#         windowsOption(browser).tratoframe(now)
#         time.sleep(2)
#     # 页面出错，关闭除列表页面的所有页面
#     except NoSuchElementException:
#         except_option(browser, now)
#         result = False
#     assert result == True
#
#
# @pytest.mark.dependency(depends=["test_02"])
# def test_03(browser):
#     """
#             发送汇报
#             步骤：1、点击新增按钮
#                 2、填写标题和内容
#                 3、点击发送退出按钮
#                 4、检验数据是否生成
#         """
#     user = mycsv()
#     title = user.read(2, 0)
#     content = user.read(2, 1)
#     page = Reportpage(browser)
#     title_test = user.read(2, 2)
#     # 如果页面出错，关闭新增页面
#     try:
#         report_add(browser,title,content, 1)
#         # 切换回列表页面
#         windowsOption(browser).tratoframe(now)
#         time.sleep(3)
#     # 页面出错，关闭除列表页面的所有页面
#     except NoSuchElementException:
#         except_option(browser, now)
#     # 获取列表第一条记录的标题
#     time.sleep(2)
#     title = page.list_frist_title.text
#     assert title == title_test
#
#
# @pytest.mark.dependency(depends=["test_01"])
# def test_04(browser):
#     """
#     修改汇报页面校验
#     步骤：1、点击修改按钮,检验标题元素是否存在
#     """
#     user = mycsv()
#     title = user.read(3, 0)
#     content = user.read(3, 1)
#     page = Reportpage(browser)
#     # 如果页面出错，关闭新增页面
#     try:
#         report_modify(browser, title, content, 0)
#         if page.report_title.is_displayed():
#             result = True
#         else:
#             result = False
#             browser.close()
#         # 切换回列表页面
#         windowsOption(browser).tratoframe(now)
#         time.sleep(2)
#     # 页面出错，关闭除列表页面的所有页面
#     except NoSuchElementException:
#         except_option(browser,now)
#         result = False
#     assert result == True
#
#
# @pytest.mark.dependency(depends=["test_03", "test_04"])
# def test_05(browser):
#     """
#         修改汇报页面校验
#         步骤：1、点击修改按钮
#             2、修改标题和内容
#             3、点击发送退出按钮
#     """
#     user = mycsv()
#     title = user.read(3, 0)
#     content = user.read(3, 1)
#     # 如果页面出错，关闭新增页面
#     try:
#         report_modify(browser, title, content, 1)
#         time.sleep(2)
#         # 切换回列表页面
#         windowsOption(browser).tratoframe(now)
#     # 页面出错，关闭除列表页面的所有页面
#     except NoSuchElementException:
#         except_option(browser,now)
#     title_test = user.read(3, 2)
#     assert title == title_test
#
#
# @pytest.mark.dependency(depends=["test_03","test_05"])
# def test_06(browser):
#     """
#     查询校验
#     步骤：1、输入查询内容
#         2、点击立即查找按钮
#         3、校验查询出的数据
#     """
#     user = mycsv()
#     title = user.read(3, 0)
#     page = Reportpage(browser)
#     try:
#         title_query=report_query(browser,title)
#         page.eliminate_button.click()
#     except NoSuchElementException:
#         except_option(browser,now)
#         assert False
#     assert title_query == title
#
#
# @pytest.mark.dependency(depends=["test_06"])
# def test_07(browser):
#     """
#         删除校验
#         步骤：1、查询需删除的内容
#             2、删除内容
#             3、校验数据是否被删除
#         """
#     user = mycsv()
#     title = user.read(3, 0)
#     page = Reportpage(browser)
#     try:
#         report_query(browser, title)
#         report_del(browser)
#     except NoSuchElementException:
#         except_option(browser, now)
#         assert False
#     time.sleep(3)
#     assert page.list_norecord.text == '系统没有查询到任何记录！'
#
#
# if __name__ == '__main__':
#     pytest.main()