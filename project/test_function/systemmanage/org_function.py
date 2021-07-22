"""
created: 20200803 by zly
description: 组织管理模块函数库
Modification History:
1、2020-8-3 zly创建了此文件
"""
from page.systemmanage.sys_page import loginpage
import time
from test_function.public_function import windowsOption
from test_function.public_function import Logon, mycsv


def start_org(browser1):
    """
    登录系统，进入系统管理/组织用户管理/组织管理页面
    """
    m = Logon()
    user = mycsv()
    m.login(user.read(1, 0), user.read(1, 1), browser1)
    page = loginpage(browser1)
    page.system.click()
    time.sleep(2)
    page.org_emp.click()
    time.sleep(2)
    page.org.click()
    frame1 = browser1.find_element_by_id('mainFrame')
    browser1.switch_to.frame(frame1)
    time.sleep(2)


def org_add(object1,orgname,orgsimplename,orgSerial,status):
    """
    新增组织，object1：对象、orgname：组织名称、orgsimplename：组织简称、orgSerial：组织简码、status:0 新增   1 新增保存
    """
    page = loginpage(object1)
    now = page.current_window_handle
    # ActionChains(object1).move_to_element(page.list_addbutton).perform()
    # time.sleep(2)
    page.list_addbutton.click()
    time.sleep(2)
    win = windowsOption(object1)
    # 切换至新增页面
    win.swtich(now)
    if status == 1:
        page.org_add_name.send_keys(orgname)
        page.org_add_simplename.send_keys(orgsimplename)
        page.org_add_orgSerial.send_keys(orgSerial)
        time.sleep(2)
        page.org_add_location_button.click()
        time.sleep(2)
        page.org_add_location1.click()
        page.org_add_orgSort.click()
        time.sleep(2)
        page.org_add_save_button.click()
        time.sleep(5)


def org_modi(object1, orgname, orgsimplename, orgSerial, status):
    """
    修改组织，object1：对象、orgname：组织名称、orgsimplename：组织简称、orgSerial：组织简码、status:0 修改   1 修改保存
    """
    page = loginpage(object1)
    now = page.current_window_handle
    page.org_list_modi_button.click()
    time.sleep(2)
    win = windowsOption(object1)
    win.swtich(now)
    if status == 1:
        page.org_add_name.clear()
        page.org_add_name.send_keys(orgname)
        page.org_add_simplename.clear()
        page.org_add_simplename.send_keys(orgsimplename)
        # page.orgSerial.clear()
        # page.org_add_orgSerial.send_keys(orgSerial)
        time.sleep(2)
        page.org_add_save_button.click()
        time.sleep(3)


def search(object1, orgname):
    """
     查询功能 object1：对象、orgname：查询框需要输入的组织名称
    """
    page = loginpage(object1)
    # 查询框中输入组织名称内容
    page.org_add_name.clear()
    page.org_add_name.send_keys(orgname)
    time.sleep(2)
    # 点击查询
    page.search_button.click()
    time.sleep(2)
    data1 = page.org_no1_data.text
    return data1


def org_del(object1):
    """
    删除功能（删除列表第一条记录）  object1：对象
    """
    page=loginpage(object1)
    # ActionChains(object1).move_to_element(page.org_list_dele_button).perform()
    page.org_list_dele_button.click()
    time.sleep(2)
    # 切换到主页面
    object1.switch_to.default_content()
    # 点击提示框确定按钮
    page.ok_button.click()
    # 切换到列表区域
    frame1 = object1.find_element_by_id('mainFrame')
    object1.switch_to.frame(frame1)


def except_option(object1, now1):
    """
    如果页面异常，则关闭非当前浏览器以外窗口
    """
    drivers = object1.window_handles
    print("except  is :", now1)
    if len(drivers) > 1:
        print("except_option!!!!!!!!!!!!!")
        windowsOption(object1).close_not_All(now1)

