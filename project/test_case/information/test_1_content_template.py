"""
created: 202008018 by zly
description: 内容模板模块测试
Modification History:
1、2020-8-18 yb创建了此文件
"""

from test_function.information.content_template_function import Content_template
from page.information.information_page import Information_page
from test_function.office_function import Office_method
import time
import pytest


@pytest.mark.dependency()
def test_01(browser):
    """
    ======内容模板菜单开始测试.....=======
        栏目管理菜单校验
        步骤：登录系统，点击信息、栏目管理
        预期：页面正常，栏目名称字段显示
    """
    opteration = Content_template(browser)
    page = Information_page(browser)
    try:
        # 进入栏目管理菜单
        opteration.star_content_template(browser)
        # 验证新建按钮是否存在
        result = page.template_add_button.is_displayed()
    except:
        result = False
    assert result == True


@pytest.mark.dependency(depends=["test_01"])
def test_02(browser):
    """
    新增类别页面校验
    步骤：点击新建类编按钮，检查类别名称是否存在
    预期：页面正常，类别名称显示正常
    """
    opteration = Content_template(browser)
    page = Information_page(browser)
    try:
        # 点击新建类别按钮
        opteration.add_category("自动化类别", "自动化类别内容", 0)
        # 检查类别名称是否存在
        result = page.category_name.is_displayed()
        # 点击页面关闭按钮
        page.add_category_close_button.click()
        time.sleep(1)
    except:
        opteration.refresh_content_template(browser)
        result = False
    assert result == True


@pytest.mark.dependency(depends=["test_02"])
def test_03(browser):
    """
        新增类别校验
        步骤：1、点击新建类别按钮
            2、输入类别名称、类别描述，点击保存按钮
            3、检查类别名称是否正确
        预期：1、弹出新建页面
            2、数据保存成功
            3、类别名称正确
    """
    opteration = Content_template(browser)
    page = Information_page(browser)
    try:
        # 输入类别名称、类别描述，点击保存按钮
        opteration.add_category("自动化类别", "自动化类别内容", 1)
        time.sleep(2)
        # 获取第一个类别名称
        first_category = page.first_category.text
    except:
        opteration.refresh_content_template(browser)
        first_category = False
    # 检查类别名称是否相等
    assert first_category == ' 自动化类别'


@pytest.mark.dependency(depends=["test_02", "test_03"])
def test_04(browser):
    """
        修改类别页面校验
        步骤：点击类别编辑按钮，检查类别名称是否存在
        预期：页面正常，类别名称显示正常
    """
    opteration = Content_template(browser)
    page = Information_page(browser)
    try:
        # 点击类编编辑按钮
        opteration.modify_category(browser, "自动化类别修改", "自动化类别修改内容", 0)
        # 检查类别名称是否存在
        result = page.category_name.is_displayed()
        # 点击页面关闭按钮
        page.modify_category_close_button.click()
        time.sleep(2)
    except:
        opteration.refresh_content_template(browser)
        result = False
    assert result == True


@pytest.mark.dependency(depends=["test_04"])
def test_05(browser):
    """
        修改类别校验
        步骤：1、点击类别编辑按钮
            2、修改类别名称、类别描述，点击保存按钮
            3、检查类别名称是否正确
        预期：1、弹出修改页面
            2、数据保存成功
            3、类别名称正确
    """
    opteration = Content_template(browser)
    page = Information_page(browser)
    try:
        # 修改类别的名称、类别描述
        opteration.modify_category(browser, "自动化类别修改", "自动化类别修改内容", 1)
        time.sleep(2)
        # 获取第一个类别的名称
        first_category = page.first_category.text
    except:
        opteration.refresh_content_template(browser)
        first_category = False
    # 检查类别名称是否相等
    assert first_category == ' 自动化类别修改'


@pytest.mark.dependency(depends=["test_05"])
def test_06(browser):
    """
        类别查询校验
        步骤：输入类别名称查询
        预期：查询结果正确
    """
    opteration = Content_template(browser)
    page = Information_page(browser)
    try:
        # 输入类别名称查询
        opteration.query_category("自动化类别修改")
        time.sleep(2)
        # 获取第一个类别的名称
        first_category = page.first_category.text
    except:
        first_category = False
    assert first_category == ' 自动化类别修改'


@pytest.mark.dependency(depends=["test_01"])
def test_07(browser):
    """
        新增模板页面校验
        步骤：点击新建按钮，检查模板名称是否存在
        预期：页面正常，模板名称显示正常
    """
    opteration = Content_template(browser)
    page = Information_page(browser)
    try:
        # 点击新建按钮
        opteration.add_template("自动化模板", 0)
        time.sleep(1)
        # 检查模板名称是否存在
        result = page.template_name.is_displayed()
        # 点击模板页面关闭按钮
        page.add_template_close_button.click()
    except:
        opteration.refresh_content_template(browser)
        result = False
    assert result == True


@pytest.mark.dependency(depends=["test_07"])
def test_08(browser):
    """
        新增模板校验
        步骤：1、点击新建按钮
            2、输入模板名称，选择模板类别，点击保存按钮
            3、检查模板名称是否争取
        预期：1、弹出新建页面
            2、数据保存成功
            3、模板名称正确
    """
    opteration = Content_template(browser)
    page = Information_page(browser)
    try:
        # 点击内容模板菜单
        page.content_template.click()
        time.sleep(1)
        # 输入新建按钮，输入模板名称、选择模板类别、点击保存
        opteration.add_template("自动化模板", 1)
        time.sleep(2)
        # 获取第一个模板名称
        frist_template = page.frist_template_name.text
    except:
        # 点击模板页面关闭按钮
        opteration.refresh_content_template(browser)
        frist_template = False
    assert frist_template == "自动化模板"


@pytest.mark.dependency(depends=["test_01"])
def test_09(browser):
    """
        修改模板页面校验
        步骤：点击修改按钮，检查模板名称是否存在
        预期：页面正常，模板名称显示正正确
    """
    opteration = Content_template(browser)
    page = Information_page(browser)
    try:
        # 点击编辑按钮
        opteration.modify_template(browser, "自动化模板修改", "自动化模板修改内容", 0)
        time.sleep(1)
        # 检查模板名称是否存在
        result = page.template_name.is_displayed()
        # 点击模板页面关闭按钮
        page.modify_template_close_button.click()
    except:
        opteration.refresh_content_template(browser)
        result = False
    assert result == True


@pytest.mark.dependency(depends=["test_09"])
def test_10(browser):
    """
        修改模板校验
        步骤：1、点击修改按钮
            2、修改模板名称，点击保存按钮
            3、检查模板名称是否正确
        预期：1、弹出修改页面
            2、数据保存成功
            3、模板名称显示正确
    """
    opteration = Content_template(browser)
    page = Information_page(browser)
    try:
        opteration.modify_template(browser, "自动化模板修改", "自动化模板修改内容", 1)
        time.sleep(2)
        frist_template = page.frist_template_name.text
    except:
        opteration.refresh_content_template(browser)
        frist_template = False
    assert frist_template == "自动化模板修改"


@pytest.mark.dependency(depends=["test_09"])
def test_11(browser):
    """
        模板查看校验
        步骤：点击模板名称，检查查看页面模板名称是否正确
        预期：查看页面正确
    """
    opteration = Content_template(browser)
    page = Information_page(browser)
    try:
        # 点击列表模板名称
        opteration.see_template()
        # 获取查看页面模板名称
        template_name = page.see_template_name.text
        page.see_template_close_button.click()
    except:
        opteration.refresh_content_template(browser)
        template_name = False
    assert  template_name == "自动化模板修改"


@pytest.mark.dependency(depends=["test_10"])
def test_12(browser):
    """
        模板查询校验
        步骤：输入模板名称查询
        预期：查询结果正确
    """
    opteration = Content_template(browser)
    page = Information_page(browser)
    try:
        # 输入模板名称查询
        opteration.query_template("自动化模板修改")
        time.sleep(1)
        # 获取第一个模板名称
        frist_template = page.frist_template_name.text
    except:
        frist_template = False
    assert frist_template == "自动化模板修改"


@pytest.mark.dependency()
def test_13(browser):
    """
        模板删除校验
        步骤：点击模板删除按钮，删除模板
        预期：删除成功
    """
    opteration = Content_template(browser)
    page = Information_page(browser)
    try:
        # 删除第一个模板
        opteration.delete_template()
        # 查询模板
        opteration.query_template("自动化模板修改")
        time.sleep(1)
        # 获取第一个模板名称
        search_result = page.template_no_search.text
    except:
        search_result = False
    assert search_result == "无搜索结果"


@pytest.mark.dependency()
def test_14(browser):
    """
        批量删除校验
        步骤：1、新建模板
            2、选择模板，点击批量删除按钮
            3、检查模板是否被删除
        预期：1、模板新建成功
            2、模板删除成功
            3、模板被删除
    """
    opteration = Content_template(browser)
    page = Information_page(browser)
    office_method = Office_method(browser)
    try:
        # 点击内容模板菜单
        page.content_template.click()
        # 输入新建按钮，输入模板名称、选择模板类别、点击保存
        opteration.add_template("自动化模板", 1)
        # 查询模板
        opteration.query_template("自动化模板")
        time.sleep(1)
        # 批量删除
        office_method.batch_delete()
        # 获取第一个模板名称
        search_result = page.template_no_search.text
    except:
        # 点击模板页面关闭按钮
        opteration.refresh_content_template(browser)
        search_result = False
    assert search_result == "无搜索结果"


@pytest.mark.dependency(depends=["test_05"])
def test_15(browser):
    """
        类别删除校验
        步骤：点击类别删除按钮，删除了类别
        预期：删除成功
    """
    opteration = Content_template(browser)
    page = Information_page(browser)
    try:
        # 删除第一个类别
        opteration.delete_category(browser)
        # 查询类别
        opteration.query_category("自动化类别修改")
        time.sleep(2)
        # 获取第一个类别名称
        search_result = page.category_no_search.text
    except:
        search_result = False
    assert search_result == '无搜索结果'


@pytest.mark.dependency()
def test_end(browser):
    """
        ======内容模板菜单结束测试.....=======
    """
    opteration_office = Office_method(browser)
    opteration_office.logout()


if __name__ == '__main__':
    pytest.main()