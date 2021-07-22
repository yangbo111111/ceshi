"""
created: 20200807 by yb
description: 汇报模块函数库
Modification History:
1、2020-8-7 yb创建了此文件
"""
from page.report.report_page import Reportpage
import time
from test_function.public_function import Logon,mycsv
from test_function.public_function import windowsOption
from selenium.common.exceptions import NoSuchElementException


def start_report(browser):
    """
    登录系统，进入汇报/我的汇报/其它
    """
    m = Logon()
    user = mycsv()
    m.login(user.read(1, 0), user.read(1, 1), browser)
    page = Reportpage(browser)
    page.report.click()
    time.sleep(2)
    page.my_report.click()
    time.sleep(2)
    page.it_report.click()
    frame1 = browser.find_element_by_id('mainFrame')
    browser.switch_to.frame(frame1)
    time.sleep(2)


def report_add(browser,title,content,status):
    """
        新增汇报，browser：对象、title：汇报标题、content：汇报内容、status:0 点击新增   1 新增保存
    """
    page = Reportpage(browser)
    now_handle = browser.current_window_handle
    page.list_addbutton.click()
    change_widows = windowsOption(browser)
    change_widows.swtich(now_handle)
    if status == 1:
        page.report_title.send_keys(title)
        browser.switch_to.frame('ewebeditorIFrame')
        browser.switch_to.frame('eWebEditor')
        page.report_content.send_keys(content)
        browser.switch_to.default_content()
        page.report_send_button.click()
        time.sleep(2)
    # 弹出当前日期已有汇报时，点击确定按钮
        if page.report_tips.is_displayed():
            page.report_tips.click()
        time.sleep(2)


def report_modify(browser,title,content,status):
    """
            修改汇报，browser：对象、title：汇报标题、content：汇报内容、status:0 点击修改   1 修改保存
     """
    page = Reportpage(browser)
    now_handle = browser.current_window_handle
    page.list_modifybutton.click()
    change_widows = windowsOption(browser)
    change_widows.swtich(now_handle)
    if status == 1:
        page.report_title.clear()
        page.report_title.send_keys(title)
        browser.switch_to.frame('ewebeditorIFrame')
        browser.switch_to.frame('eWebEditor')
        page.report_content.clear()
        page.report_content.send_keys(content)
        browser.switch_to.default_content()
        page.report_send_button.click()
        time.sleep(3)


def report_query(browser,title):
    """
            查询汇报，browser：对象、title：汇报标题
    """
    page = Reportpage(browser)
    page.list_title_query.send_keys(title)
    page.query_button.click()
    time.sleep(1)
    query_title = page.list_frist_title.text
    return query_title


def report_del(browser):
    page = Reportpage(browser)
    page.list_delbutton.click()
    time.sleep(2)
    # 切换到主页面
    browser.switch_to.default_content()
    # 点击提示框确定按钮
    page.ok_button.click()
    # 切换到列表区域
    browser.switch_to.frame("mainFrame")


def except_option(object1, now1):
    """
    如果页面异常，则关闭非当前浏览器以外窗口
    """
    drivers = object1.window_hxandles
    if len(drivers) > 1:
        windowsOption(object1).close_not_All(now1)


