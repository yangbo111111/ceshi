"""
created: 202008011 by yb
description: 栏目内容函数库
Modification History:
1、2020-8-11 yb创建了此文件
"""

from page.information.information_page import Information_page
from test_function.office_function import Office_method, Mycsv
from test_function.information.column_management_function import Column_Management
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time


class Column_Content(object):
    """
        栏目内容操作函数
    """

    def __init__(self, browser):
        self.page = Information_page(browser)

    def go_information(self, browser):
        """
            登录，进入信息模块
        """
        office_menthod = Office_method(browser)
        mycsv = Mycsv()
        # 登录系统
        office_menthod.login( mycsv.read(1, 0), mycsv.read(1, 1))
        # 点击信息
        self.page.information.click()

    def star_column_content(self):
        """
            进入栏目内容
        """
        # office_menthod = Office_method()
        # mycsv = Mycsv()
        # # 登录系统
        # office_menthod.login(browser, mycsv.read(1, 0), mycsv.read(1, 1))
        # # 点击信息
        # self.page.information.click()
        # 点击栏目内容
        self.page.column_content.click()
        time.sleep(2)

    def add_information(self, name, content, stautes, browser):
        """
            新建信息，name:信息名称、content：信息内容、status:0 点击新增   1 新增保存、browser:浏览器对象
        """
        # 点击左侧树第一个栏目
        self.page.information_frist_column.click()
        # 点击新建按钮
        self.page.add_button.click()
        time.sleep(2)
        if stautes == 1:
            # 输入标题
            self.page.information_name.send_keys(name)
            browser.switch_to.frame("ueditor_0")
            # 输入内容
            self.page.information_content.send_keys(content)
            browser.switch_to.default_content()
            # 点击发布按钮
            self.page.information_save_button.click()

    def modify_information(self, name, content, stautes, browser):
        """
            修改信息，name:信息名称、content：信息内容、status:0 点击新增   1 修改保存、browser:浏览器对象
        """
        # 点击编辑按钮
        self.page.information_modify_button.click()
        time.sleep(3)
        if stautes == 1:
            self.page.information_name.clear()
            # 输入标题
            self.page.information_name.send_keys(name)
            browser.switch_to.frame("ueditor_0")
            self.page.information_content.clear()
            # 输入内容
            self.page.information_content.send_keys(content)
            browser.switch_to.default_content()
            # 点击保存按钮
            self.page.modify_information_save_button.click()

    def query_information(self, name):
        """
            查询信息，name:标题
        """
        self.page.information_query_name.clear()
        # 输入标题
        self.page.information_query_name.send_keys(name)
        # 点击查询按钮
        self.page.information_query_button.click()

    def delete_information(self):
        """
            删除信息
        """
        # 点击删除
        self.page.information_delete_button.click()
        # 点击确定按钮
        self.page.ok_button.click()

    def refresh_column_content(self, browser):
        """
            刷新页面，进入信息/栏目内容
        """
        # 刷新页面
        browser.refresh()
        time.sleep(1)
        # 点击信息
        self.page.information.click()
        # 点击栏目内容
        self.page.column_content.click()
        time.sleep(2)

    def add_column(self, browser, name, code, content):
        """
            新增栏目
        """
        # office_menthod = Office_method()
        # mycsv = Mycsv()
        # # 登录系统
        # office_menthod.login(browser, mycsv.read(1, 0), mycsv.read(1, 1))
        # # 点击信息
        # self.page.information.click()
        column = Column_Management(browser)
        # 点击栏目管理
        self.page.Column_management.click()
        # 新建栏目
        column.add_column(name, code, content)

    def batch_copy_information(self, name, status):
        """
            批量复制信息，  status:1 保存
        """
        if status == 1:
            # 点击左侧树第一个栏目
            self.page.information_frist_column.click()
            time.sleep(2)
            # 选择第一条信息
            self.page.choice_frist_information.click()
            # 点击批量复制按钮
            self.page.information_batch_copy_button.click()
            time.sleep(2)
            # 查询栏目
            self.column_choice_query(name)
            time.sleep(1)
            # 选择第一个栏目
            self.page.column_choice_frist_column.click()
            # 点击保存按钮
            self.page.copy_column_choice_save_button.click()
        else:
            # 选择第一条信息
            self.page.choice_frist_information.click()
            # 点击批量复制按钮
            self.page.information_batch_copy_button.click()

    def batch_move_information(self, name):
        """
            批量移动信息
        """
        # 选择第一条信息
        self.page.choice_frist_information.click()
        # 点击批量移动按钮
        self.page.information_batch_move_button.click()
        time.sleep(2)
        # 查询栏目
        self.column_choice_query(name)
        time.sleep(1)
        # 选择第一个栏目
        self.page.column_choice_frist_column.click()
        # 点击保存按钮
        self.page.move_column_choice_save_button.click()

    def column_choice_query(self, name):
        """
            栏目选择页面，查询
        """
        # 输入栏目名称
        self.page.column_choice_query.send_keys(name)
        # 点击查询按钮
        self.page.column_choice_query_button.click()
