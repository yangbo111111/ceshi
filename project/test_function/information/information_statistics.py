"""
created: 202009027 by yb
description: 信息统计函数库
Modification History:
1、2020-9-27 yb创建了此文件
"""
from page.information.information_page import Information_page
from test_function.office_function import Office_method, Mycsv
from test_function.information.column_content_function import Column_Content
import time


class Information_Statistics(object):
    """
        信息统计操作函数
    """
    def __init__(self, browser):
        self.page = Information_page(browser)
        self.column_content = Column_Content(browser)

    def star_information_statistics(self, browser):
        """
            登录，进入信息/信息统计
        """
        office_menthod = Office_method(browser)
        mycsv = Mycsv()
        # 登录系统
        office_menthod.login(mycsv.read(1, 0), mycsv.read(1, 1))
        self.page.information.click()
        self.page.information_statistics.click()

    def add_colunm_information(self, browser, stautes):
        """
            增加栏目和信息
        """
        # 点击信息
        self.page.information.click()
        if stautes == 1:
            # 增加栏目
            self.column_content.add_column(browser, "自动化栏目", "zidonghua", "自动化内容")
            # 点击栏目内容
            self.page.column_content.click()
            time.sleep(1)
            # 增加信息
            self.column_content.add_information("精华信息", "精华信息内容", 1, browser)
        else:
            # 增加信息
            self.column_content.add_information("自动化信息", "自动化信息内容", 1, browser)

    def essence_information(self, name):
        """
            添加精华信息
        """
        # 点击信息
        self.page.information.click()
        # 查询信息
        self.column_content.query_information(name)
        time.sleep(2)
        # 精华信息
        self.page.information_essence_button.click()
        time.sleep(1)
        self.page.ok_button.click()

    def query_publisher(self, name, publisher_element, query_element):
        """
            发布人查询
        """
        self.publisher_element = publisher_element
        self.query_element = query_element
        # 点击查询展开按钮
        # self.open_element.click()
        # 发布人输入
        self.publisher_element.clear()
        self.publisher_element.send_keys(name)
        # 点击查询按钮
        self.query_element.click()

    def refresh_information_statistics(self, browser):
        """
            刷新页面，进入信息/信息统计
        """
        # 刷新页面
        browser.refresh()
        time.sleep(1)
        # 点击信息
        self.page.information.click()
        # 点击信息统计
        self.page.information_statistics.click()

