"""
created: 20200803 by zly
description: 页面元素库
Modification History:
1、2020-8-3 zly创建了此文件
"""

from poium import Page, PageElement, NewPageElement


class loginpage(Page):
    username = NewPageElement(id_="userAccount",describe="用户名输入框")
    user_password = NewPageElement(id_="userPassword",describe="密码")
    login_button = NewPageElement(id_="mysubmit", describe="登录按钮")
    loginout_button = NewPageElement(xpath="//a[@title='安全登出']", describe="安全登出按钮")
    # 以下是系统菜单
    system=NewPageElement(link_text="系统管理", describe="系统管理菜单")
    org_emp=NewPageElement(link_text="组织用户管理", describe="组织用户管理菜单")
    org = NewPageElement(link_text="组织管理", describe="组织管理菜单")
    user_img = NewPageElement(xpath="//a[@class='wh-hd-user-info']/img", describe="用户头像")
    # 组织管理列表
    list_addbutton = NewPageElement(xpath="//input[@value='新　增']", describe="新增按钮")
    org_list_title = NewPageElement(xpath="//*[@id='headerContainer']/tr",describe="列表标题项")
    org_list_title1 = NewPageElement(xpath="//*[@id='headerContainer']/tr/td[1]",describe="列表-组织名称")
    org_no1_data = NewPageElement(xpath="//*[@id='itemContainer']/tr[1]/td[1]", describe="列表第一行组织名称")
    org_list_modi_button = NewPageElement(xpath='//*[@id="itemContainer"]/tr[1]/td[8]/img[1]', describe="列表第一行记录的修改按钮")
    org_list_dele_button = NewPageElement(xpath="//*[@id='itemContainer']/tr[1]/td[8]/img[2]", describe="列表第一行记录的删除按钮")
    org_list_orgdata2 = NewPageElement(xpath='//*[@id="itemContainer"]/tr[1]/td[3]',describe="列表第一行记录的组织简称")
    org_list_orgdata3 = NewPageElement(xpath='//*[@id="itemContainer"]/tr[1]/td[4]',describe="列表第一行记录的组织简码")
    search_button = NewPageElement(xpath="//td[@class='SearchBar_toolbar']/input[1]",describe="立即查询按钮")
    clear_button = NewPageElement(xpath="//td[@class='SearchBar_toolbar']/input[2]",describe="清除按钮")
    # 新增组织页面
    org_add_name = NewPageElement(id_="orgName", describe="组织名称输入框")
    org_add_simplename = NewPageElement(id_="orgSimpleName", describe="组织简称")
    org_add_orgSerial = NewPageElement(id_="orgSerial", describe="组织编码")
    org_add_save_button = NewPageElement(xpath="//input[@value='保存退出']", describe="保存退出按钮")
    org_add_location = NewPageElement(class_name="combo-panel panel-body panel-body-noheader", describe="存放位置")
    org_add_location1 = NewPageElement(xpath="/html/body/div[3]/div/div[1]", describe="存放位置下拉框第一个组织")
    org_add_location_button = NewPageElement(class_name="combo-arrow", describe="存放位置下拉框按钮")
    org_add_orgSort = NewPageElement(id_="orgSort0", describe="前")
    # 弹出框确定
    ok_button = NewPageElement(xpath="//div[@class='ui_buttons']/input[1]", describe="弹出框确定按钮")
