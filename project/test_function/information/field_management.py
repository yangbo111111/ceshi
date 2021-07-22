"""
created: 20210111 by yb
description: 字段管理函数库
Modification History:
1、2021-01-11 yb创建了此文件
"""


from page.information.information_page import Information_page
from test_function.office_function import Office_method, Mycsv, WindowsOption
import time


class Field_management(object):
    """
        字段管理操作函数
    """
    def __init__(self, browser):
        self.page = Information_page(browser)
        self.office_menthod = Office_method(browser)

    def star_field_management(self, browser):
        """
            登录，进入后台/内容中心/字段管理
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
        # 点击字段管理
        self.page.field_management.click()

    def refresh_field_management(self, browser):
        """
            刷新页面，进入内容中心/字段管理
        """
        # 刷新页面
        browser.refresh()
        time.sleep(1)
        # 点击内容中心
        self.page.content_center.click()
        # 点击频道管理
        self.page.field_management.click()

    def add_data_sheet(self, data_name, system_name, status):
        """
            新建数据表，data_name:数据表名称、system_name：系统名称、status:0 点击新增   1 新增保存
        """
        # 点击新建按钮
        self.page.field_management_add_button.click()
        if status == 1:
            # 输入数据表名称
            self.page.field_management_add_data_sheet_name.send_keys(data_name)
            # 输入系统名称
            self.page.field_management_add_data_sheet_system_name.send_keys(system_name)
            # 选择所属分类
            self.page.field_management_add_data_sheet_dropdown_button.click()
            self.page.field_management_add_data_sheet_chose_classification.click()
            # 点击保存按钮
            self.page.field_management_add_data_sheet_save_button.click()

    def edit_data_sheet(self, data_name, status):
        """
            编辑数据表，data_name:数据表名称、status:0 点击新增   1 新增保存
        """
        # 点击编辑按钮
        self.page.field_management_edit_button.click()
        if status == 1:
            # 修改数据表名称
            self.page.field_management_edit_data_sheet_name.clear()
            self.page.field_management_edit_data_sheet_name.send_keys(data_name)
            # 点击保存按钮
            self.page.field_management_edit_data_sheet_save_button.click()

    def copy_data_sheet(self, data_name, system_name):
        """
            编辑数据表，data_name:数据表名称,system_name:系统名称
        """
        # 点击复制按钮
        self.page.field_management_copy_button.click()
        # 修改数据表名称
        self.page.field_management_edit_data_sheet_name.clear()
        self.page.field_management_edit_data_sheet_name.send_keys(data_name)
        # 输入系统名称
        self.page.field_management_add_data_sheet_system_name.clear()
        self.page.field_management_add_data_sheet_system_name.send_keys(system_name)
        # 点击保存按钮
        self.page.field_management_edit_data_sheet_save_button.click()

    def add_field(self, field_name, status):
        """
            新建字段，field_name:字段名称、status:0 点击新增   1 新增保存
        """
        # 点击新建按钮
        self.page.field_management_add_button.click()
        if status == 1:
            # 输入字段名称
            self.page.field_setup_field_name.send_keys(field_name)
            # 点击保存按钮
            self.page.field_setup_add_field_save_button.click()

    def edit_field(self, field_name, status):
        """
            编辑字段，field_name:字段名称、status:0 点击新增   1 新增保存
        """
        # 点击编辑按钮
        self.page.field_setup_edit_button.click()
        if status == 1:
            # 输入字段名称
            self.page.field_setup_field_name.clear()
            self.page.field_setup_field_name.send_keys(field_name)
            # 点击保存按钮
            self.page.field_setup_edit_field_save_button.click()

    def batch_add_field(self, field_name, status):
        """
            新建字段，field_name:字段名称、status:0 点击新增   1 新增保存
        """
        # 点击批量新建按钮
        self.page.field_setup_batch_add_button.click()
        if status == 1:
            # 输入字段名称
            self.page.field_setup_batch_field_name.send_keys(field_name)
            # 点击保存按钮
            self.page.field_setup_batch_add_field_save_button.click()

    def batch_edit_field(self, field_name):
        """
            编辑字段，field_name:字段名称、status:0 点击新增   1 新增保存
        """
        # 点击批量修改按钮
        self.page.field_setup_batch_edit_button.click()
        # 修改字段名称
        self.page.field_setup_batch_field_name.clear()
        self.page.field_setup_batch_field_name.send_keys(field_name)
        # 点击保存按钮
        self.page.field_setup_batch_edit_field_save_button.click()

    def refresh_field_setup(self, browser):
        """
            刷新页面，进入内容中心/字段管理/字段设置
        """
        # 刷新页面
        browser.refresh()
        time.sleep(1)
        # 点击内容中心
        self.page.content_center.click()
        # 点击频道管理
        self.page.field_management.click()
        # 点击字段设置
        self.page.field_management_field_setup_button.click()

