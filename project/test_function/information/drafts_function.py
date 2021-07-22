"""
created: 202009010 by yb
description: 草稿箱函数库
Modification History:
1、2020-9-10 yb创建了此文件
"""

from page.information.information_page import Information_page
from test_function.office_function import Office_method, Mycsv
from test_function.information.column_content_function import Column_Content
import time


class Drafts(object):
    """
        栏目内容操作函数
    """

    def __init__(self, browser):
        self.page = Information_page(browser)

    def add_drafts_information(self, browser, stautes):
        """
            登录，进入信息模块,增加栏目和草稿信息, stautes:1 登录，增加栏目、信息、复制信息，stautes:0 复制信息
        """
        office_menthod = Office_method(browser)
        mycsv = Mycsv()
        column_content = Column_Content(browser)
        if stautes == 1:
            # 登录系统
            office_menthod.login(mycsv.read(1, 0), mycsv.read(1, 1))
            # 点击信息
            self.page.information.click()
            # 增加栏目
            column_content.add_column(browser, "自动化栏目", "zidonghua", "自动化内容")
            column_content.add_column(browser, "复制栏目", "fuzhi", "复制内容")
            # 点击栏目内容
            self.page.column_content.click()
            # 增加信息
            column_content.add_information("自动化信息", "自动化信息内容", 1, browser)
            # 复制信息
            column_content.batch_copy_information("自动化栏目", 1)
        else:
            # 点击栏目内容
            self.page.column_content.click()
            # 复制信息
            column_content.batch_copy_information("自动化栏目", 1)

    def star_drafts(self):
        """
            进入草稿箱
        """
        # 点击信息
        self.page.information.click()
        self.page.my_content.click()
        self.page.drafts.click()

    def refresh_drafts(self, browser):
        """
            刷新页面，进入信息/我的发布/草稿箱
        """
        # 刷新页面
        browser.refresh()
        time.sleep(1)
        # 点击信息
        self.page.information.click()
        # 点击我的内容
        self.page.my_content.click()
        # 点击草稿箱
        self.page.drafts.click()
        time.sleep(2)

    def batch_release(self):
        """
            信息批量发布
        """
        # 全选信息
        self.page.choice_all.click()
        time.sleep(1)
        # 点击批量复制按钮
        self.page.drafts_batch_release_button.click()
        # 点击确定按钮
        self.page.ok_button.click()

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
            self.page.my_modify_information_save_button.click()

    def delete_information(self):
        """
            删除信息
        """
        # 点击删除
        self.page.drafts_delete_button.click()
        # 点击确定按钮
        self.page.ok_button.click()
