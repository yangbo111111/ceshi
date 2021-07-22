"""
created: 20210201 by yb
description: 单位频道模块用例
Modification History:
1、2021-02-01 yb创建了此文件
"""

from page.information.information_page import Information_page
from test_function.information.unit_channel_function import Unit_channel
from test_function.office_function import Office_method
import pytest
import time


@pytest.mark.dependency()
def test_01(browser):
    """
    ======单位频道菜单开始测试.....=======
    单位频道页面校验
        步骤：1、登录系统，进入后台/内容中心/单位频道
            2、页面元素校验
        预期：
            1、进入单位频道菜单
            2、页面元素存在
    """
    opteration = Unit_channel(browser)
    page = Information_page(browser)
    try:
        # 进入单位频道
        opteration.star_unit_channel(browser)
        time.sleep(1)
        # 获取批量新建按钮元素
        result = page.unit_channel_batch_add_button.is_displayed()
    except:
        opteration.refresh_unit_channel(browser)
        result = False
    assert result == True


@pytest.mark.dependency(depends=["test_01"])
def test_02(browser):
    """
    新建单位频道页面校验
        步骤：1、点击新建按钮
            2、检查频道名称元素是否存在
        预期：
            1、弹出新建单位频道页面
            2、页面元素存在
    """
    opteration = Unit_channel(browser)
    page = Information_page(browser)
    try:
        # 打开新建单位频道页面
        opteration.add_unit_channel(0)
        time.sleep(1)
        # 获取保存按钮元素
        result = page.add_unit_channel_name.is_displayed()
        # 点击页面关闭按钮
        page.add_unit_channel_close_buton.click()
    except:
        result = False
    assert result == True


@pytest.mark.dependency(depends=["test_02"])
def test_03(browser):
    """
    新建单位频道校验
        步骤：1、点击新建按钮
            2、检查频道名称元素是否存在
        预期：
            1、弹出新建单位频道页面
            2、页面元素存在
    """
    opteration = Unit_channel(browser)
    page = Information_page(browser)
    global name
    try:
        # 打开新建单位频道页面
        opteration.add_unit_channel(0)
        # 获取频道名称
        name = page.add_unit_channel_name.text
        name = name.strip()
        # 点击保存按钮
        page.add_unit_channel_save_buton.click()
        time.sleep(1)
        # 获取列表频道名称
        channel_name = page.frist_data.text
    except:
        opteration.refresh_unit_channel(browser)
        channel_name = False
    assert channel_name == name


@pytest.mark.dependency(depends=["test_03"])
def test_04(browser):
    """
    编辑单位频道页面校验
        步骤：1、点击编辑按钮
            2、检查保存按钮元素是否存在
        预期：
            1、弹出编辑数据表页面
            2、页面元素存在
    """
    opteration = Unit_channel(browser)
    page = Information_page(browser)
    try:
        page.unit_channel_edit_button.click()
        time.sleep(1)
        # 保存按钮是否存在
        result = page.edit_unit_channel_save_buton.is_displayed()
        time.sleep(1)
        # 点击编辑页面关闭按钮
        page.edit_unit_channel_close_buton.click()
    except:
        opteration.refresh_unit_channel(browser)
        result = False
    assert result == True


@pytest.mark.dependency(depends=["test_03"])
def test_05(browser):
    """
    查看单位频道校验
        步骤：1、点击频道名称
            2、获取频道名称，判断频道名称是否正确
        预期：
            1、弹出查看频道页面
            2、频道名称正确
    """
    opteration = Unit_channel(browser)
    page = Information_page(browser)
    try:
        # 点击频道名称
        page.frist_data.click()
        time.sleep(1)
        # 获取频道名称
        channel_name = page.view_unit_channel_name.text
        # 点击关闭按钮
        page.view_unit_channel_close_button.click()
    except:
        opteration.refresh_unit_channel(browser)
        channel_name = False
    assert channel_name == name


@pytest.mark.dependency(depends=["test_03"])
def test_06(browser):
    """
    查询频道校验
        步骤：1、输入频道名称，点击搜索按钮
            2、判断频道名称是否正确
        预期：
            1、搜索成功
            2、频道名称正确
    """
    opteration = Unit_channel(browser)
    opteration_office = Office_method(browser)
    page = Information_page(browser)
    try:
        # 查询单位频道
        opteration_office.query(page.unit_channel_name_query, name, page.unit_channel_name_query_button)
        time.sleep(2)
        # 获取第一个频道名称
        channel_name = page.frist_data.text
    except:
        opteration.refresh_unit_channel(browser)
        channel_name = False
    assert channel_name == name


@pytest.mark.dependency(depends=["test_03"])
def test_07(browser):
    """
    预览单位频道页面校验
        步骤：1、点击预览按钮
            2、判断页面标题是否存在
        预期：
            1、弹出预览页面
            2、页面标题存在
    """
    opteration = Unit_channel(browser)
    page = Information_page(browser)
    try:
        # 点击预览按钮
        page.unit_channel_preview_button.click()
        time.sleep(1)
        # 判断页面标题是否存在
        result = page.preview_unit_channel_title.is_displayed()
        # 点击关闭按钮
        page.preview_unit_channel_close_button.click()
    except:
        opteration.refresh_unit_channel(browser)
        result = False
    assert result == True


@pytest.mark.dependency(depends=["test_03"])
def test_08(browser):
    """
    设计频道校验
        步骤：1、点击设计按钮
            2、判断基础设置页签元素
            3、点击列表字段设置页签，判断新增按钮元素
        预期：
            1、打开设计页面
            2、基础设置页签元素存在
            3、切换到列表字段设置页签，新增按钮存在
    """
    page = Information_page(browser)
    opteration = Unit_channel(browser)
    try:
        # 点击设计按钮
        page.unit_channel_design_button.click()
        time.sleep(1)
        result1 = page.design_channel_basics.is_displayed()
        # 点击列表字段设置
        page.design_channel_field.click()
        result2 = page.design_channel_add_button.is_displayed()
        result = result1 and result2
        # 点击页面关闭按钮
        page.design_channel_close_button.click()
    except:
        opteration.refresh_unit_channel(browser)
        result = False
    assert result == True


@pytest.mark.dependency(depends=["test_03"])
def test_09(browser):
    """
    取消发布校验
        步骤：1、点击取消发布按钮
            2、判断单位频道的状态
        预期：
            1、单位频道取消发布
            2、频道状态为待发布
    """
    page = Information_page(browser)
    opteration = Unit_channel(browser)
    try:
        # 点击取消发布按钮
        page.unit_channel_unpublish_button.click()
        time.sleep(1)
        page.ok_button.click()
        time.sleep(1)
        # 获取列表状态
        state = page.unit_channel_release_state.text
    except:
        opteration.refresh_unit_channel(browser)
        state = False
    assert state == "待发布"


@pytest.mark.dependency(depends=["test_03"])
def test_10(browser):
    """
    删除单位频道校验
        步骤：1、点击删除按钮，删除频道
            2、判断频道是否被删除
        预期：
            1、频道被删除
            2、频道删除成功
    """
    opteration = Unit_channel(browser)
    opteration_office = Office_method(browser)
    page = Information_page(browser)
    try:
        # 删除频道
        opteration_office.delete(page.unit_channel_delete_button)
        time.sleep(2)
        # 查询频道
        opteration_office.query(page.unit_channel_name_query, name, page.unit_channel_name_query_button)
        time.sleep(2)
        no_search = page.no_query_result.text
    except:
        opteration.refresh_unit_channel(browser)
        no_search = False
    assert no_search == "无搜索结果"


@pytest.mark.dependency(depends=["test_07"])
def test_11(browser):
    """
    批量删除频道校验
        步骤：1、点击批量删除按钮，删除频道
            2、判断频道是否被删除
        预期：
            1、频道被删除
            2、频道删除成功
    """
    opteration = Unit_channel(browser)
    opteration_office = Office_method(browser)
    page = Information_page(browser)
    try:
        # 打开新建单位频道页面
        opteration.add_unit_channel(1)
        page.unit_channel_unpublish_button.click()
        time.sleep(1)
        page.ok_button.click()
        time.sleep(1)
        # 查询频道
        opteration_office.query(page.unit_channel_name_query, name, page.unit_channel_name_query_button)
        time.sleep(1)
        # 批量删除频道
        opteration_office.batch_delete()
        time.sleep(2)
        no_search = page.no_query_result.text
    except:
        opteration.refresh_unit_channel(browser)
        no_search = False
    assert no_search == "无搜索结果"


@pytest.mark.dependency()
def test_end(browser):
    """
    ======单位频道菜单结束测试.....=======

    """
    page = Information_page(browser)
    opteration_office = Office_method(browser)
    # 登出
    opteration_office.logout()


if __name__ == '__main__':
    pytest.main()

