"""
created: 202008011 by yb
description: 公共方法函数库
Modification History:
1、2020-8-11 yb创建了此文件
"""

from page.information.information_page import Information_page
from config import RunConfig
import time
import csv
import codecs


class Office_method(object):

    def __init__(self, browser):
        self.page = Information_page(browser)

    def login(self, username, password):
        self.page.get(RunConfig.url)
        self.page.username.clear()
        self.page.username.send_keys(username)
        self.page.password.clear()
        self.page.password.send_keys(password)
        self.page.login_button.click()
        time.sleep(5)

    def logout(self):
        self.page.head_portrait.click()
        self.page.sign_out.click()

    def batch_delete(self):
        # 全选
        self.page.choice_all.click()
        # 点击批量删除
        self.page.batch_deletion_button.click()
        # 点击确定按钮
        self.page.ok_button.click()

    def delete(self, delete_button):
        self.delete_button = delete_button
        self.delete_button.click()
        self.page.ok_button.click()

    def query(self, element, name, query_button):
        self.element = element
        self.query_button = query_button
        self.element.clear()
        self.element.send_keys(name)
        self.query_button.click()

class Mycsv(object):
    """
    csv数据操作类
    """

    # 读取csv中第row行第column列数据
    def read(self, row, column):
        data = csv.reader(codecs.open('./././data.csv', 'r', 'utf_8_sig'))
        datas = []
        for d in data:
            datas.append(d)
        data1 = datas[row]
        return data1[column]


class WindowsOption(object):
    """
    窗口切换、关闭
    """
    def __init__(self, browser):
        self.object1 = browser

    def closeA(self):
        """
        A跳转至当前页B，窗口切换到B后，关闭A
        """
        drivers = self.object1.window_handles
        nowdriver = self.object1.current_window_handle
        if nowdriver == drivers[1]:
            self.object1.switch_to_window(drivers[0])
            self.object1.close()
            self.object1.switch_to_window(drivers[1])

    def close_not_All(self, nowdriver):
        """
        关闭非列表页面的所有浏览器页面,nowdriver传列表页面
        """
        drivers = self.object1.window_handles
        for new in drivers:
            if new != nowdriver:
                self.object1.switch_to_window(new)
                time.sleep(2)
                self.object1.close()
                self.object1.switch_to_windw(nowdriver)
        time.sleep(1)

    def swtich(self, now1):
        """
        切换至新窗口(2个窗口间切换),now1:取初始列表页句柄
        """
        drivers = self.object1.window_handles
        if now1 == drivers[0] and len(drivers) == 2:
            new = drivers[1]
            self.object1.switch_to.window(new)
        elif now1 == drivers[1] or len(drivers) == 1:
            new = drivers[0]
            self.object1.switch_to.window(new)