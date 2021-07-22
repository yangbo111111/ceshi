"""
created: 20210201 by yb
description: 单位频道函数库
Modification History:
1、2021-02-01 yb创建了此文件
"""

from page.information.information_page import Information_page
from test_function.office_function import Office_method, Mycsv, WindowsOption
import time


class Unit_channel(object):
    """
        单位频道操作函数
    """
    def __init__(self, browser):
        self.page = Information_page(browser)
        self.office_menthod = Office_method(browser)

    def star_unit_channel(self, browser):
        """
            登录，进入后台/内容中心/单位频道
        """
        mycsv = Mycsv()
        # 登录系统
        self.office_menthod.login(mycsv.read(1, 0), mycsv.read(1, 1))
        # 点击头像
        self.page.head_portrait.click()
        # 点击进入后台
        self.page.enter_base.click()
        # 切换到后台
        now_handle = browser.current_window_handle
        change_widows = WindowsOption(browser)
        change_widows.swtich(now_handle)
        change_widows.closeA()
        time.sleep(2)
        # 点击内容中心
        self.page.content_center.click()
        # 点击单位频道
        self.page.unit_channel.click()

    def add_unit_channel(self, status):
        """
            新建单位频道，status:0 点击新增   1 新增保存
        """
        # 点击批量新建按钮
        self.page.unit_channel_batch_add_button.click()
        time.sleep(2)
        # 选择默认组织
        self.page.largest_organization.click()
        # 点击确定按钮
        self.page.unit_channel_chose_user_ok_button.click()
        time.sleep(1)
        if status == 1:
            # 点击保存按钮
            self.page.add_unit_channel_save_buton.click()

    def refresh_unit_channel(self, browser):
        """
            刷新页面，进入内容中心/单位频道
        """
        # 刷新页面
        browser.refresh()
        time.sleep(1)
        # 点击内容中心
        self.page.content_center.click()
        # 点击单位频道
        self.page.unit_channel.click()
