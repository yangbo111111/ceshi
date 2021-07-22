"""
created: 20201230 by yb
description: 虚拟栏目函数库
Modification History:
1、2020-12-30 yb创建了此文件
"""


from page.information.information_page import Information_page
from test_function.office_function import Office_method, Mycsv, WindowsOption
from selenium.webdriver.common.action_chains import ActionChains
import time


class Virtual_column(object):
    """
        虚拟栏目操作函数
    """
    def __init__(self, browser):
        self.page = Information_page(browser)
        self.office_menthod = Office_method(browser)

    def star_virtual_column(self, browser, name):
        """
            登录，进入后台/内容中心/虚拟栏目
        """
        mycsv = Mycsv()
        # 登录系统
        self.office_menthod.login(mycsv.read(1, 0), mycsv.read(1, 1))
        # 点击信息
        self.page.information.click()
        # 点击栏目管理
        self.page.Column_management.click()
        time.sleep(1)
        # 输入栏目名称
        self.page.column_name.send_keys(name)
        # 点击保存按钮
        self.page.column_save_button.click()
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
        self.page.virtual_column.click()

    def refresh_virtual_column(self, browser):
        """
            刷新页面，进入内容中心/虚拟栏目
        """
        # 刷新页面
        browser.refresh()
        time.sleep(1)
        # 点击内容中心
        self.page.content_center.click()
        # 点击虚拟栏目
        self.page.virtual_column.click()
        time.sleep(1)

    def add_virtual_column(self, name):
        """
            新建虚拟栏目，name:栏目名称
        """
        # 添加栏目名称
        self.page.virtual_column_name.send_keys(name)
        self.page.virtual_column_save_button.click()

    def add_lower_virtual_column(self, name):
        """
            新建下级虚拟栏目，name:栏目名称
        """
        # 点击新建按钮
        self.page.lower_virtual_add_button.click()
        # 输入栏目名称
        self.page.lower_virtual_column_name.send_keys(name)
        # 点击选择关联栏目按钮
        self.page.lower_virtual_column_chose_button.click()
        # 选择第一个栏目
        self.page.connected_column_frist_column.click()
        # 点击关联栏目保存按钮
        self.page.connected_column_save_button.click()
        time.sleep(1)
        # 点击下级虚拟栏目保存按钮
        self.page.lower_virtual_column_save_button.click()

    def edit_lower_virtual_column(self, name, status):
        """
            编辑下级栏目，name:栏目名称、status:0 点击编辑   1 编辑保存
        """
        self.page.lower_virtual_edit_button.click()
        if status == 1:
            self.page.edit_lower_virtual_column_name.clear()
            self.page.edit_lower_virtual_column_name.send_keys(name)
            self.page.edit_lower_virtual_column_save_button.click()

    def end_lower_virtual_column(self, browser):
        ActionChains(browser).move_to_element(self.page.virtual_column_frist_column).perform()
        # 选择第一个栏目，鼠标右击删除栏目
        ActionChains(browser).context_click(self.page.virtual_column_frist_column).perform()
        # 点击删除按钮
        self.page.virtual_column_delete_column.click()
        time.sleep(1)
        # 点击确定按钮
        self.page.ok_button.click()
        # 点击头像
        self.page.head_portrait.click()
        # 点击进入前台
        self.page.enter_office.click()
        # 切换到前台
        now_handle = browser.current_window_handle
        change_widows = WindowsOption(browser)
        change_widows.swtich(now_handle)
        change_widows.closeA()
        time.sleep(2)
        # 点击信息
        self.page.information.click()
        # 点击栏目管理
        self.page.Column_management.click()
        # 选择第一个栏目，鼠标右击删除栏目
        ActionChains(browser).context_click(self.page.first_column).perform()
        time.sleep(2)
        # 点击栏目删除按钮
        self.page.column_delete_button.click()
        time.sleep(2)
        # 点击确定按钮
        self.page.ok_button.click()
        time.sleep(2)
