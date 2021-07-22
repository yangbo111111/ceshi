"""
created: 202008011 by yb
description: 栏目管理函数库
Modification History:
1、2020-8-11 yb创建了此文件
"""

from page.information.information_page import Information_page
from test_function.office_function import Office_method, Mycsv
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time


class Column_Management(object):

    def __init__(self, browser):
        self.page = Information_page(browser)

    def star_column_management(self, browser):
        """
            登录系统，进入信息/栏目管理
        """
        office_menthod = Office_method(browser)
        mycsv = Mycsv()
        # 登录系统
        office_menthod.login(mycsv.read(1, 0), mycsv.read(1, 1))
        # 点击信息
        self.page.information.click()
        # 点击栏目管理
        self.page.Column_management.click()
        time.sleep(3)

    def add_column(self, name, code, content):
        """
            新增栏目，name：栏目名称、code：栏目编码、content：描述
        """
        # 输入栏目名称
        self.page.column_name.send_keys(name)
        self.page.column_code.clear()
        # 输入栏目编码
        self.page.column_code.send_keys(code)
        # 输入描述
        self.page.column_describe.send_keys(content)
        # 点击详细设置页签
        self.page.details.click()
        time.sleep(2)
        # 点击选人按钮
        self.page.allownow_button.click()
        time.sleep(2)
        # 选择默认组织
        self.page.largest_organization.click()
        # 点击确定按钮
        self.page.pick_ok_button.click()
        time.sleep(2)
        # 点击基本信息页签
        self.page.base_infomation.click()
        # 点击保存按钮
        self.page.column_save_button.click()
        time.sleep(2)

    def modify_column(self, name, content, stautes):
        """
            修改栏目，name：栏目名称、content：描述、status:0 点击新增   1 新增保存
        """
        # 点击左侧树第一个栏目名称
        self.page.first_column.click()
        if stautes == 1:
            time.sleep(3)
            # 修改栏目的名称、描述，点击保存按钮
            self.page.column_name.clear()
            self.page.column_name.send_keys(name)
            self.page.column_describe.clear()
            self.page.column_describe.send_keys(content)
            self.page.column_modifysave_button.click()
            time.sleep(1)

    def query_column(self, name):
        """
            查询栏目，name：栏目名称
        """
        # 查询框输入栏目名称按回车键查询
        self.page.column_query.clear()
        self.page.column_query.send_keys(name)
        time.sleep(2)
        self.page.column_query.send_keys(Keys.ENTER)

    def query_allcolumn(self):
        """
            查询所有栏目
        """
        # 不输入查询条件直接回车查询
        self.page.column_query.clear()
        self.page.column_query.send_keys(Keys.ENTER)

    def delete_column(self, browser):
        """
            删除栏目，browser：浏览器对象
        """
        # 选择第一个栏目，鼠标右击删除栏目
        ActionChains(browser).context_click(self.page.first_column).perform()
        time.sleep(2)
        self.page.column_delete_button.click()
        time.sleep(2)
        self.page.ok_button.click()


