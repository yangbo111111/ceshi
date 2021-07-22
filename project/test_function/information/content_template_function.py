"""
created: 202008011 by yb
description: 内容模板函数库
Modification History:
1、2020-8-11 yb创建了此文件
"""

from page.information.information_page import Information_page
from test_function.office_function import Office_method, Mycsv
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time


class Content_template(object):
    """
        内容模板操作函数
    """

    def __init__(self, browser):
        self.page = Information_page(browser)

    def star_content_template(self, browser):
        """
            登录系统，进入信息/内容模板
        """
        office_menthod = Office_method(browser)
        mycsv = Mycsv()
        # 登录系统
        office_menthod.login(mycsv.read(1, 0), mycsv.read(1, 1))
        # 点击信息
        self.page.information.click()
        # 点击内容模板
        self.page.content_template.click()
        time.sleep(2)

    def refresh_content_template(self, browser):
        """
            刷新页面，进入信息/内容模板
        """
        browser.refresh()
        time.sleep(1)
        # 点击信息
        self.page.information.click()
        # 点击内容模板
        self.page.content_template.click()
        time.sleep(2)

    def add_category(self, name, content, stautes):
        """
            新增类别，name：类别名称、content：类别描述、status:0 点击新增   1 新增保存
        """
        self.page.add_category_button.click()
        if stautes == 1:
            self.page.category_name.clear()
            self.page.category_name.send_keys(name)
            self.page.category_describe.clear()
            self.page.category_describe.send_keys(content)
            self.page.add_category_save_button.click()

    def modify_category(self, browser, name, content, stautes):
        """
            修改类别，browser:浏览器对象，name：类别名称、content：类别描述、status:0 点击新增   1 新增保存
        """
        # 选择第一个类别，鼠标右击编辑
        ActionChains(browser).context_click(self.page.first_category).perform()
        time.sleep(2)
        # 带年纪编辑按钮
        self.page.category_edit_button.click()
        if stautes == 1:
            # 输入类别名称、类别描述、点击保存按钮
            self.page.category_name.clear()
            self.page.category_name.send_keys(name)
            self.page.category_describe.clear()
            self.page.category_describe.send_keys(content)
            self.page.modify_category_save_button.click()

    def query_category(self,name):
        """
            查询类别，name：类别名称
        """
        # 查询框输入栏目名称按回车键查询
        self.page.category_name_query.clear()
        self.page.category_name_query.send_keys(name)
        self.page.category_name_query.send_keys(Keys.ENTER)

    def delete_category(self, browser):
        """
         删除类别，browser：浏览器对象
        """
        # 选择第一个栏目，鼠标右击删除栏目
        ActionChains(browser).context_click(self.page.first_category).perform()
        time.sleep(2)
        # 点击删除按钮
        self.page.category_delete_button.click()
        time.sleep(2)
        # 点击删除提示确定按钮
        self.page.ok_button.click()

    def add_template(self, name, stautes):
        """
         新增模板，name：模板名称、status:0 点击新增   1 新增保存
        """
        # 点击新建按钮
        self.page.template_add_button.click()
        if stautes == 1:
            # 输入模板名称，选择模板类别，点击保存按钮
            self.page.template_name.clear()
            self.page.template_name.send_keys(name)
            self.page.category_dropdown_button.click()
            self.page.dropdown_first_category.click()
            self.page.add_template_save_button.click()
        time.sleep(2)

    def modify_template(self, browser, name, content, stautes):
        """
            修改模板，name：模板名称、content：内容、status:0 点击修改   1 修改保存
        """
        self.page.template_modify_button.click()
        time.sleep(2)
        if stautes == 1:
            self.page.template_name.clear()
            self.page.template_name.send_keys(name)
            # browser.switch_to.frame("ueditor_1")
            # self.page.template_content.send_keys(content)
            # browser.switch_to.default_content()
            self.page.modify_template_save_button.click()
        time.sleep(2)

    def query_template(self, name):
        self.page.template_query_name.clear()
        self.page.template_query_name.send_keys(name)
        self.page.template_query_button.click()

    def see_template(self):
        self.page.frist_template_name.click()

    def delete_template(self):
        self.page.template_delete_button.click()
        time.sleep(1)
        self.page.ok_button.click()


