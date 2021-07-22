"""
created: 20200803 by zly
description: 公共函数库
Modification History:
1、2020-8-3 zly创建了此文件
"""

from page.report.report_page import Reportpage
import time
import csv
import codecs
from config import RunConfig

class Logon():
    """
    登录，包含浏览器访问、登录、退出
    """
    def login(self, username, userpassword, browser1):
        """
        登录，username：账号，userpassword：密码
        """
        page = Reportpage(browser1)
        page.get(RunConfig.url)
        time.sleep(2)
        page.username.clear()
        page.username.send_keys(username)
        page.user_password.clear()
        page.user_password.send_keys(userpassword)
        time.sleep(2)
        page.login_button.click()
        time.sleep(5)

    def loginout(self, browser1):
        """
        登出
        """
        page = Reportpage(browser1)
        # ActionChains(browser1).move_to_element(page.user_img).perform()
        # time.sleep(2)
        page.user_img.click()
        time.sleep(1)
        page.loginout_button.click()


class mycsv:
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


class windowsOption():
    """
    窗口切换、关闭
    """
    def __init__(self, object1):
        self.object1 = object1

    def closeB(self):
        """
        A跳转至当前页B，窗口切换到B后，关闭B
        """
        drivers = self.object1.window_handles
        nowdriver = self.object1.current_window_handle
        if nowdriver == drivers[0]:
            self.object1.switch_to_window(drivers[1])
            self.object1.close()
        elif nowdriver == drivers[1]:
            self.object1.switch_to_window(drivers[0])
            self.object1.close()

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
                time.sleep(2)
                self.object1.switch_to_windw(nowdriver)
        time.sleep(3)
        windowsOption(self.object1).tratoframe(nowdriver)

    def swtich(self,now1):
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

    def tratoframe(self, now):
        """
        其他页面切换回列表区域 ,now:取初始列表页句柄
        """
        self.object1.switch_to.window(now)
        frame1 = self.object1.find_element_by_id('mainFrame')
        self.object1.switch_to.frame(frame1)
