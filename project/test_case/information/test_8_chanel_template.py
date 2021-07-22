"""
created: 20201221 by yb
description: 频道管理模块用例
Modification History:
1、2020-12-21 yb创建了此文件
"""


from page.information.information_page import Information_page
from test_function.information.channel_template_function import Channel_template
from test_function.office_function import Office_method
import pytest
import time


@pytest.mark.dependency()
def test_01(browser):
    """
    ======频道模板菜单开始测试.....=======
    频道模板页面校验
        步骤：1、登录系统，进入后台/内容中心/频道模板
            2、页面元素校验
        预期：
            1、进入频道模板菜单
            2、页面元素存在
    """
    opteration = Channel_template(browser)
    page = Information_page(browser)
    try:
        # 进入模板管理
        opteration.star_channel_template(browser)
        time.sleep(1)
        # 获取搜索按钮元素
        result = page.channel_template_query_button.is_displayed()
    except:
        opteration.refresh_channel_template(browser)
        result = False
    assert result == True


@pytest.mark.dependency(depends=["test_01"])
def test_02(browser):
    """
    新建频道模板页面校验
        步骤：1、点击新建按钮
            2、检查模板名称元素是否存在
        预期：
            1、弹出新建频道模板页面
            2、页面元素存在
    """
    opteration = Channel_template(browser)
    page = Information_page(browser)
    try:
        # 打开新建模板页面
        opteration.add_channel_template("自动化模板", "zidonghuamoban", 0)
        # 获取模板名称元素
        result = page.add_channel_template_name.is_displayed()
        # 关闭页面
        page.add_channel_template_close_button.click()
    except:
        opteration.refresh_channel_template(browser)
        result = False
    assert result == True


@pytest.mark.dependency(depends=["test_02"])
def test_03(browser):
    """
    新建频道模板校验
        步骤：1、点击新建按钮
            2、输入模板名称、编码，点击保存按钮
            3、判断模板名称是否正确
        预期：
            1、弹出新建频道页面
            2、保存成功
            3、频道名称正确
    """
    opteration = Channel_template(browser)
    page = Information_page(browser)
    try:
        # 新建频道
        opteration.add_channel_template("自动化频道模板", "zidonghuamoban", 1)
        time.sleep(2)
        # 获取第一个频道名称
        template_name = page.frist_data.text
    except:
        opteration.refresh_channel_template(browser)
        template_name = False
    assert template_name == "自动化频道模板"


@pytest.mark.dependency(depends=["test_03"])
def test_04(browser):
    """
    编辑频道模板页面校验
        步骤：1、点击编辑按钮
            2、检查频道模板名称元素是否存在
        预期：
            1、弹出编辑频道模板页面
            2、页面元素存在
    """
    opteration = Channel_template(browser)
    page = Information_page(browser)
    try:
        # 打开编辑频道模板页面
        opteration.edit_channel_template("编辑自动化模板", "zidonghuamoban", 0)
        time.sleep(1)
        # 模板名称是否存在
        result = page.add_channel_template_name.is_displayed()
        # 点击编辑页面关闭按钮
        page.edit_channel_template_close_button.click()
    except:
        opteration.refresh_channel_template(browser)
        result = False
    assert result == True


@pytest.mark.dependency(depends=["test_04"])
def test_05(browser):
    """
    编辑频道模板校验
        步骤：1、点击编辑按钮
            2、输入模板名称、编码，点击保存按钮
            3、判断频道模板名称是否正确
        预期：
            1、弹出编辑频道模板页面
            2、保存成功
            3、频道模板名称正确
    """
    opteration = Channel_template(browser)
    page = Information_page(browser)
    try:
        # 编辑频道模板
        opteration.edit_channel_template("修改自动化频道模板", "zidonghuamoban", 1)
        time.sleep(2)
        # 获取第一个频道模板名称
        template_name = page.frist_data.text
    except:
        opteration.refresh_channel_template(browser)
        template_name = False
    assert template_name == "修改自动化频道模板"


@pytest.mark.dependency(depends=["test_05"])
def test_06(browser):
    """
    查看频道模板校验
        步骤：1、点击频道模板名称
            2、获取频道模板名称，判断频道模板名称是否正确
        预期：
            1、弹出查看频道模板页面
            2、频道模板名称正确
    """
    opteration = Channel_template(browser)
    page = Information_page(browser)
    try:
        # 点击频道名称
        page.frist_data.click()
        # 获取频道名称
        template_name = page.see_channel_template_name.text
        # 点击关闭按钮
        page.see_channel_template_close_button.click()
    except:
        opteration.refresh_channel_template(browser)
        template_name = False
    assert template_name == "修改自动化频道模板"


@pytest.mark.dependency(depends=["test_02"])
def test_07(browser):
    """
    设计页面校验
        步骤：1、点击设计按钮
            2、判断保存按钮元素是否存在
        预期：
            1、弹出设计页面
            2、保存按钮元素存在
    """
    opteration = Channel_template(browser)
    page = Information_page(browser)
    try:
        # 点击设计按钮
        page.channel_template_design_button.click()
        # 获取保存按钮元素
        result = page.design_channel_template_save_button.is_displayed()
        # 关闭设计页面
        page.design_channel_template_close_button.click()
    except:
        opteration.refresh_channel_template(browser)
        result = False
    assert result == True


@pytest.mark.dependency(depends=["test_07"])
def test_08(browser):
    """
    预览页面校验
        步骤：1、点击预览按钮
            2、判读预览页面元素是否存在
        预期：
            1、弹出预览页面
            2、预览页面元素存在
    """
    opteration = Channel_template(browser)
    page = Information_page(browser)
    try:
        # 点击预览按钮
        page.channel_template_preview_button.click()
        # 获取预览页面内容
        name = page.preview_channel_template_name.text
        time.sleep(1)
        # 关闭预览页面
        page.preview_channel_template_close_button.click()
    except:
        opteration.refresh_channel_template(browser)
        name = False
    assert name == "模板预览"


@pytest.mark.dependency(depends=["test_05"])
def test_09(browser):
    """
    查询频道模板校验
        步骤：1、输入频道模板名称，点击搜索按钮
            2、判断频道模板名称是否正确
        预期：
            1、搜索成功
            2、频道模板名称正确
    """
    opteration = Channel_template(browser)
    opteration_office = Office_method(browser)
    page = Information_page(browser)
    try:
        # 查询频道
        opteration_office.query(page.channel_template_name_query, "修改自动化频道模板", page.channel_template_query_button)
        time.sleep(2)
        # 获取第一个频道模板名称
        template_name = page.frist_data.text
    except:
        opteration.refresh_channel_template(browser)
        template_name = False
    assert template_name == "修改自动化频道模板"


@pytest.mark.dependency(depends=["test_07"])
def test_10(browser):
    """
    删除频道模板校验
        步骤：1、点击删除按钮，删除频道
            2、判断频道模板是否被删除
        预期：
            1、频道被删除
            2、频道删除成功
    """
    opteration = Channel_template(browser)
    opteration_office = Office_method(browser)
    page = Information_page(browser)
    try:
        # 删除频道模板
        opteration_office.delete(page.delete_button)
        time.sleep(2)
        # 查询频道模板
        opteration_office.query(page.channel_template_name_query, "修改自动化频道模板", page.channel_template_query_button)
        time.sleep(2)
        no_search = page.no_query_result.text
    except:
        opteration.refresh_channel_template(browser)
        no_search = False
    assert no_search == "无搜索结果"


@pytest.mark.dependency(depends=["test_02"])
def test_11(browser):
    """
    批量删除频道模板校验
        步骤：1、点击删除按钮，删除频道
            2、判断频道模板是否被删除
        预期：
            1、频道被删除
            2、频道删除成功
    """
    opteration = Channel_template(browser)
    opteration_office = Office_method(browser)
    page = Information_page(browser)
    try:
        # 新建频道模板
        opteration.add_channel_template("批量删除模板", "zidonghuamoban", 1)
        # 查询频道
        opteration_office.query(page.channel_template_name_query, "批量删除模板", page.channel_template_query_button)
        # 批量删除频道
        opteration_office.batch_delete()
        time.sleep(2)
        no_search = page.no_query_result.text
    except:
        opteration.refresh_channel_template(browser)
        no_search = False
    assert no_search == "无搜索结果"


@pytest.mark.dependency()
def test_end(browser):
    """
    ======频道模板菜单结束测试.....=======

    """
    opteration_office = Office_method(browser)
    # 登出
    opteration_office.logout()


if __name__ == '__main__':

    pytest.main()

