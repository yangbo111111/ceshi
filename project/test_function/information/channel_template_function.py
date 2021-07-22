"""
created: 20201221 by yb
description: 频道模板函数库
Modification History:
1、2020-12-21 yb创建了此文件
"""

from page.information.information_page import Information_page
from test_function.office_function import Office_method, Mycsv, WindowsOption
import time


class Channel_template(object):
    """
        频道模板操作函数
    """
    def __init__(self, browser):
        self.page = Information_page(browser)
        self.office_menthod = Office_method(browser)

    def star_channel_template(self, browser):
        """
            登录，进入后台/内容中心/频道模板
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
        # 点击频道模板
        self.page.channel_template.click()

    def refresh_channel_template(self, browser):
        """
            刷新页面，进入内容中心/频道模板
        """
        # 刷新页面
        browser.refresh()
        time.sleep(1)
        # 点击内容中心
        self.page.content_center.click()
        # 点击频道管理
        self.page.channel_template.click()

    def add_channel_template(self, name, code, status):
        """
            新建频道模板，name:模板名称、code：频道编码、status:0 点击新增   1 新增保存
        """
        self.page.add_button.click()
        if status == 1:
            self.page.add_channel_template_name.send_keys(name)
            self.page.add_channel_template_code.send_keys(code)
            self.page.add_channel_template_save_button.click()

    def edit_channel_template(self, name, code, status):
        """
            编辑频道模板，name:模板名称、code：模板编码、status:0 点击编辑   1 编辑保存
        """
        self.page.edit_button.click()
        if status == 1:
            self.page.add_channel_template_name.clear()
            self.page.add_channel_template_name.send_keys(name)
            self.page.add_channel_template_code.clear()
            self.page.add_channel_template_code.send_keys(code)
            self.page.edit_channel_template_save_button.click()