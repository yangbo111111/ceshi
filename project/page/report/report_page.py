"""
created: 20200805 by yb
description: 汇报页面元素库
Modification History:
1、2020-8-5 yb创建了此文件
"""

from poium import Page, PageElement, NewPageElement


class Reportpage(Page):
    username = NewPageElement(id_="userAccount",describe="用户名输入框")
    user_password = NewPageElement(id_="userPassword",describe="密码")
    login_button = NewPageElement(id_="mysubmit", describe="登录按钮")
    loginout_button = NewPageElement(xpath="//a[@title='安全登出']", describe="安全登出按钮")
    user_img = NewPageElement(xpath="//a[@class='wh-hd-user-info']/img", describe="用户头像")
    # 以下是汇报菜单
    report=NewPageElement(id_="menu_workReport",describe="汇报菜单")
    my_report=NewPageElement(link_text="我的汇报",describe="我的汇报菜单")
    it_report = NewPageElement(link_text="其它", describe="其它菜单")
    # 以下是其它列表
    list_addbutton = NewPageElement(xpath="//input[@value='新　增']", describe="新增按钮")
    list_modifybutton=NewPageElement(xpath="//tr[1]//td[8]//a[1]//img[1]",describe="修改按钮")
    list_delbutton=NewPageElement(xpath="//tr[1]//td[8]//a[2]//img[1]",describe="删除按钮")
    list_frist_title=NewPageElement(xpath="//*[@id='itemContainer']/tr[1]/td[3]/a",describe="第一条汇报标题")
    list_norecord=NewPageElement(xpath="//tbody[@id='itemContainer']//tr//td",describe="无数据提示")
    list_title_query=NewPageElement(name="queryReportTitle",describe="标题查询框")
    query_button =NewPageElement(xpath="//td[@class='SearchBar_toolbar']//input[1]",describe="立即查找按钮")
    eliminate_button=NewPageElement(xpath="//td[@class='SearchBar_toolbar']//input[2]",describe="清除按钮")
    # 以下是汇报页面
    report_title =NewPageElement(name="workReport.reportTitle",describe="标题")
    report_content=NewPageElement(xpath="/html/body",describe="汇报内容")
    report_send_button=NewPageElement(id_="sendClose",describe="发送退出按钮")
    report_tips=NewPageElement(class_name="ui_state_highlight",describe="提示确定按钮")
    # 弹出框
    ok_button=NewPageElement(xpath="//input[@class='ui_state_highlight']",describe="弹出框确定按钮")