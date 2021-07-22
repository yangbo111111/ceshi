# """
# created: 20200803 by zly
# description: 组织管理模块测试
# Modification History:
# 1、2020-8-3 zly创建了此文件
# """
#
# from selenium.common.exceptions import NoSuchElementException
# from test_function.systemmanage.org_function import org_add, org_modi, search, org_del, start_org, except_option
# from test_function.public_function import windowsOption
# from page.systemmanage.sys_page import loginpage
# import time
# import pytest
# now = None
# @pytest.mark.webtest
# def test_init(browser):
#     """
#     ======组织管理菜单开始测试.....=======
#     """
#     # 打开浏览器，点击系统管理/组织用户管理/组织管理
#     start_org(browser)
#     global now
#     now = browser.current_window_handle
#
#
# @pytest.mark.dependency()
# @pytest.mark.webtest
# def test_org01(browser):
#     """
#     组织列表页面校验
#     步骤：
#     1、点击系统管理/组织用户管理/组织管理
#     预期：
#     1、列表组织名称标题项存在，页面显示正常
#     """
#     page = loginpage(browser)
#     try:
#         result1 = page.org_list_title1.is_displayed()
#     except NoSuchElementException:
#         result1 = False
#     assert result1 == True
#
#
# @pytest.mark.dependency(depends=["test_org01"])
# @pytest.mark.webtest
# def test_org02(browser):
#     """
#     组织新增页面校验
#     步骤：
#     1、点击系统管理/组织用户管理/组织管理，点击新增按钮
#     预期：
#     1、弹出的新增页面显示组织名称输入框，新增页面正常。
#     """
#     # now = browser.current_window_handle
#     global now
#     try:
#         org_add(browser, "自动化测试组织", "自动化测试组织", "zdhcszz", 0)
#         page = loginpage(browser)
#         try:
#             result2 = page.org_add_name.is_displayed()
#         except:
#             result2 = False
#         time.sleep(3)
#         # 关闭新增页面
#         browser.close()
#         # 切回列表区域
#         windowsOption(browser).tratoframe(now)
#     except NoSuchElementException:
#         result2=False
#         # 判断是否打开多个页面，如果是，保留初始页面，关闭多余页面
#         except_option(browser, now)
#     assert result2 == True
#
#
# @pytest.mark.dependency(depends=["test_org02"])
# def test_org03(browser):
#     """
#     组织新增功能校验
#     步骤：
#     1、点击系统管理/组织用户管理/组织管理，点击新增按钮，输入组织名称、组织简称、组织简码，点击保存退出按钮。
#     预期：
#     1、列表显示新增的记录。
#     """
#     page = loginpage(browser)
#     global now
#     print("test03 first is :", now)
#     try:
#         org_add(browser, "组织新增测试_python", "组织新增_python", "zzbmpython", 1)
#         #切换回列表区域
#         print("run here!!!!!!!!!!!!!")
#         windowsOption(browser).tratoframe(now)
#         time.sleep(2)
#     except NoSuchElementException:
#         # 判断是否打开多个页面，如果是，保留初始页面，关闭多余页面
#         time.sleep(3)
#         print("test03 is :", now)
#         except_option(browser,now)
#         time.sleep(3)
#         print("run here except!!!!!!!!!!!!!!")
#         assert False
#     assert page.org_no1_data.text == "组织新增测试_python"
#
#
# @pytest.mark.dependency(depends=["test_org01"])
# @pytest.mark.webtest
# def test_org04(browser):
#     """
#     组织修改页面校验
#     步骤：
#     1、点击系统管理/组织用户管理/组织管理，点击修改按钮
#     预期：
#     1、弹出的修改页面显示组织名称输入框，修改页面正常。
#     """
#     global now
#     try:
#         org_modi(browser, "自动化测试修改组织", "自动化测试修改组织", "zdhcszz1", 0)
#         page = loginpage(browser)
#         try:
#             result4 = page.org_add_name.is_displayed()
#         except:
#             result4 = False
#         time.sleep(3)
#         # 关闭修改页面
#         print("走到关闭页面！！！")
#         browser.close()
#         # 切换列表区域
#         windowsOption(browser).tratoframe(now)
#     except NoSuchElementException:
#         # 判断是否打开多个页面，如果是，保留初始页面，关闭多余页面
#         except_option(browser, now)
#         result4 = False
#     assert result4 == True
#
#
# @pytest.mark.dependency(depends=["test_org03", "test_org04"])
# def test_org05(browser):
#     """
#     组织修改功能校验
#     步骤：
#     1、点击系统管理/组织用户管理/组织管理，点击修改按钮，修改组织名称、组织简称、组织简码，点击保存退出按钮。
#     预期：
#     1、检查列表中修改记录是否成功。
#     """
#     page = loginpage(browser)
#     global now
#     try:
#         org_modi(browser, "组织修改测试_python", "组织修改_python", "zzbmpython1", 1)
#         # 切回列表区域
#         windowsOption(browser).tratoframe(now)
#         time.sleep(2)
#     except NoSuchElementException:
#         # 判断是否打开多个页面，如果是，保留初始页面，关闭多余页面
#         except_option(browser, now)
#         assert False
#     assert page.org_no1_data.text == "组织修改测试_python" and page.org_list_orgdata2.text == "组织修改_python"
#
#
# @pytest.mark.dependency(depends=["test_org03"])
# def test_org06(browser):
#     """
#         查询功能校验
#         步骤：
#         1、点击系统管理/组织用户管理/组织管理，输入查询内容：组织修改测试_python，点击立即查询。
#         预期：
#         1、列表中显示查询的内容。
#     """
#     global now
#     page = loginpage(browser)
#     try:
#         org_add(browser, "组织查询测试_python", "组织查询测试_python", "zzcxpython11", 1)
#         # 切换回列表页面
#         windowsOption(browser).tratoframe(now)
#         result6=search(browser, "组织查询测试_python")
#         # 清除查询条件
#         page.clear_button.click()
#     except NoSuchElementException:
#         #页面异常处理
#         except_option(browser, now)
#         assert False
#     assert result6 == "组织查询测试_python"
#
#
# @pytest.mark.dependency(depends=["test_org06"])
# def test_org07(browser):
#     """
#         删除功能校验
#         步骤：
#         1、点击系统管理/组织用户管理/组织管理，删除列表中第一条记录。
#         预期：
#         1、记录成功删除，列表不显示。
#     """
#     global now
#     try:
#         org_add(browser, "组织删除测试_python", "组织删除_python", "zzbmpython2", 1)
#         # 切换回列表页面
#         windowsOption(browser).tratoframe(now)
#         # 删除记录
#         org_del(browser)
#     except NoSuchElementException:
#         # 页面异常处理
#         except_option(browser, now)
#         assert False
#     assert search(browser, "组织删除测试_python") != "组织删除测试_python"
#
#
# @pytest.mark.dependency(depends=["test_org05", "test_org07"])
# def test_org08(browser):
#     """
#     ======组织管理菜单测试结束，删除测试数据中.....=======
#     """
#     # 删除测试记录
#     datas = ["组织查询测试_python", "组织修改测试_python"]
#     for data in datas:
#         search(browser, data)
#         org_del(browser)
#         time.sleep(2)
#     time.sleep(3)
#
#
# if __name__ == '__main__':
#     pytest.main(["-v", "-s", "test_1_org.py"])
