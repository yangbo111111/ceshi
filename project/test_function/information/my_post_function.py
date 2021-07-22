"""
created: 202009017 by yb
description: 我的发布函数库
Modification History:
1、2020-9-17 yb创建了此文件
"""
from page.information.information_page import Information_page
from test_function.office_function import Office_method, Mycsv
from test_function.information.column_content_function import Column_Content
import time


class My_post(object):
    """
        我的发布操作函数
    """
    def __init__(self, browser):
        self.page = Information_page(browser)
        self.column_content = Column_Content(browser)

    def add_my_information(self, browser, stautes):
        """
            登录，进入信息模块,增加栏目和信息, stautes:1 登录，增加栏目、信息、复制信息，stautes:0 复制信息
        """
        office_menthod = Office_method(browser)
        mycsv = Mycsv()
        if stautes == 1:
            # 登录系统
            office_menthod.login(mycsv.read(1, 0), mycsv.read(1, 1))
            # 点击信息
            self.page.information.click()
            time.sleep(1)
            # 增加栏目
            self.column_content.add_column(browser, "自动化栏目", "zidonghua", "自动化内容")
            self.column_content.add_column(browser, "移动栏目", "fuzhi", "复制内容")
            # 点击栏目内容
            self.page.column_content.click()
            # 增加信息
            self.column_content.add_information("自动化信息", "自动化信息内容", 1, browser)
        else:
            # 点击栏目内容
            self.page.column_content.click()
            # 增加信息
            self.column_content.add_information("自动化信息", "自动化信息内容", 1, browser)
            # 进入我的发布
            self.page.information.click()
            self.page.my_content.click()
            self.page.my_post.click()

    def star_my_post(self):
        """
            进入我的发布
        """
        # 点击信息
        self.page.information.click()
        # 点击我的内容
        self.page.my_content.click()
        # 点击我的发布
        self.page.my_post.click()

    def refresh_my_post(self, browser):
        """
            刷新页面，进入信息/我的发布/我的发布
        """
        # 刷新页面
        browser.refresh()
        time.sleep(1)
        # 点击信息
        self.page.information.click()
        # 点击我的内容
        self.page.my_content.click()
        # 点击草稿箱
        self.page.my_post.click()
        time.sleep(2)

    def batch_copy_information(self, column_name):
        """
            批量复制信息，column_name:栏目名称，
        """
        # 选择第一条信息
        self.page.choice_frist_information.click()
        time.sleep(2)
        # 点击批量复制按钮
        self.page.information_batch_copy_button.click()
        time.sleep(2)
        # 查询栏目
        self.column_content.column_choice_query(column_name)
        time.sleep(1)
        # 选择第一个栏目
        self.page.column_choice_frist_column.click()
        # 点击保存按钮
        self.page.copy_column_choice_save_button.click()

    def batch_move_information(self, column_name):
        """
            批量移动信息，column_name:栏目名称，
        """
        # 选择第一条信息
        self.page.choice_frist_information.click()
        time.sleep(2)
        # 点击批量复制按钮
        self.page.information_batch_move_button.click()
        time.sleep(2)
        # 查询栏目
        self.column_content.column_choice_query(column_name)
        time.sleep(1)
        # 选择第一个栏目
        self.page.column_choice_frist_column.click()
        # 点击保存按钮
        self.page.move_column_choice_save_button.click()

    def delete_information(self):
        """
            删除信息
        """
        # 点击删除
        self.page.my_post_delete_button.click()
        # 点击确定按钮
        self.page.ok_button.click()

    def synchronization_information(self, column_name):
        """
            同步信息
        """
        # 点击同步按钮
        self.page.my_post_synchronization_button.click()
        # 查询栏目
        self.column_content.column_choice_query(column_name)
        time.sleep(1)
        # 选择第一个栏目
        self.page.column_choice_frist_column.click()
        # 点击保存按钮
        self.page.sync_column_choice_save_button.click()

    def copy_information(self, column_name):
        """
            复制信息
        """
        # 点击复制按钮
        self.page.my_post_copy_button.click()
        # 查询栏目
        self.column_content.column_choice_query(column_name)
        time.sleep(1)
        # 选择第一个栏目
        self.page.column_choice_frist_column.click()
        # 点击保存按钮
        self.page.copy_column_choice_save_button.click()

    def move_information(self, column_name):
        """
            移动信息
        """
        # 点击复制按钮
        self.page.my_post_move_button.click()
        # 查询栏目
        self.column_content.column_choice_query(column_name)
        time.sleep(1)
        # 选择第一个栏目
        self.page.column_choice_frist_column.click()
        # 点击保存按钮
        self.page.move_column_choice_save_button.click()

