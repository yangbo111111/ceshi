"""
created: 202008011 by zly
description: 栏目管理模块测试
Modification History:
1、2020-8-11 yb创建了此文件
"""

from test_function.information.column_management_function import Column_Management
from page.information.information_page import Information_page
from selenium.common.exceptions import NoSuchElementException
from test_function.office_function import Office_method
import time
import pytest


@pytest.mark.dependency()
def test_01(browser):
    """
    ======栏目管理菜单开始测试.....=======
        栏目管理菜单校验
        步骤：登录系统，点击信息、栏目管理
        预期：页面正常，栏目名称字段显示
    """
    opteration = Column_Management(browser)
    page = Information_page(browser)
    try:
        # 进入栏目管理菜单
        opteration.star_column_management(browser)
        # 验证栏目名称输入框是否存在
        result = page.column_name.is_displayed()
    except NoSuchElementException:
        result = False
    assert result == True


@pytest.mark.dependency()
def test_02(browser):
    """
        详细设置页签校验
        步骤：点击详细设置页签，检查选择按钮是否存在
        预期：页面正常，选择按钮显示正常
    """
    opteration = Column_Management(browser)
    page = Information_page(browser)
    try:
        # 进入详细设置页签
        page.details.click()
        # 验证新建人选择按钮是否存在
        result = page.allownow_button.is_displayed()
        time.sleep(1)
        page.base_infomation.click()
    except NoSuchElementException:
        result = False
    assert result == True


@pytest.mark.dependency(depends=["test_01", "test_02"])
def test_03(browser):
    """
        新增栏目
        步骤：1、输入栏目名称、栏目编号、描述
            2、点击详细设置页签，选择允许新建人
            3、点击保存按钮，判断栏目名称是否正确
        预期：1、数据输入成功
            2、新建人保存成功
            3、栏目新增成功，栏目名称正确
    """
    opteration = Column_Management(browser)
    page = Information_page(browser)
    try:
        # 新增栏目
        opteration.add_column("自动化栏目", "ZDH001", "测试自动化的栏目")
        # 获取第一个栏目的名称
        first_column = page.first_column.text
    except NoSuchElementException:
        first_column = False
    assert first_column == "自动化栏目"


@pytest.mark.dependency(depends=["test_03"])
def test_04(browser):
    """
        修改栏目页面校验
        步骤：1、点击第一个栏目
            2、判断栏目名称元素是否存在
        预期：1、栏目被选中
            2、修改页面正常，栏目名称元素存在
    """
    opteration = Column_Management(browser)
    page = Information_page(browser)
    try:
        # 进入修改页面
        opteration.modify_column("自动化栏目修改", "测试自动化栏目修改", 0)
        # 验证栏目名称输入框是否存在
        result = page.column_name.is_displayed()
    except NoSuchElementException:
        result = False
    assert result == True


@pytest.mark.dependency(depends=["test_03", "test_04"])
def test_05(browser):
    """
        修改栏目
        步骤：1、点击第一个栏目
            2、修改栏目名称、描述，点击保存按钮
            3、判断栏目名称书否正确
        预期：1、栏目被选中
            2、栏目修改成功
            3、栏目名称正确
    """
    opteration = Column_Management(browser)
    page = Information_page(browser)
    try:
        # 修改栏目
        opteration.modify_column("自动化栏目修改", "测试自动化栏目修改", 1)
        # 获取第一个栏目的名称
        first_column = page.first_column.text
    except NoSuchElementException:
        first_column = False
    assert first_column == "自动化栏目修改"


@pytest.mark.dependency(depends=["test_05"])
def test_06(browser):
    """
        查询栏目
        步骤：1、输入栏目名称查询
            2、验证查询出的栏目名称是否正确
        预期：1、输入成功
            2、栏目查询成功，栏目名称正确
    """
    opteration = Column_Management(browser)
    page = Information_page(browser)
    try:
        # 查询栏目
        opteration.query_column("自动化栏目修改")
        time.sleep(2)
        # 获取第一个栏目的名称
        first_column = page.first_column.text
    except NoSuchElementException:
        first_column = False
    assert first_column == "自动化栏目修改"


@pytest.mark.dependency(depends=["test_06"])
def test_07(browser):
    """
        删除栏目
        步骤：1、查询出需删除的栏目
            2、删除栏目
            3、查询删除的栏目是否存在
        预期：1、查询成功
            2、栏目删除成功
            3、删除的栏目不存在
    """
    opteration = Column_Management(browser)
    page = Information_page(browser)
    try:
        # 删除栏目
        opteration.delete_column(browser)
        time.sleep(2)
        no_search = page.column_no_search.text
    except NoSuchElementException:
        no_search = False
    assert no_search == "无搜索结果"


@pytest.mark.dependency()
def test_end(browser):
    """
        ======栏目管理菜单结束测试.....=======
    """
    opteration_office = Office_method(browser)
    opteration_office.logout()


if __name__ == '__main__':
    pytest.main()