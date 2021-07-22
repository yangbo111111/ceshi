"""
created: 20201012 by yb
description: 频道管理模块用例
Modification History:
1、2020-10-12 yb创建了此文件
"""


from page.information.information_page import Information_page
from test_function.information.channel_management_function import Channel_management
from test_function.office_function import Office_method
import pytest
import time


@pytest.mark.dependency()
def test_01(browser):
    """
    ======频道管理菜单开始测试.....=======
    频道管理页面校验
        步骤：1、登录系统，进入后台/内容中心/频道管理
            2、页面元素校验
        预期：
            1、进入频道管理菜单
            2、页面元素存在
    """
    opteration = Channel_management(browser)
    page = Information_page(browser)
    try:
        # 进入频道管理
        opteration.star_channel_management(browser)
        time.sleep(1)
        # 获取搜索按钮元素
        result = page.channel_management_query_button.is_displayed()
    except:
        opteration.refresh_channel_management(browser)
        result = False
    assert result == True


@pytest.mark.dependency(depends=["test_01"])
def test_02(browser):
    """
    新建频道页面校验
        步骤：1、点击新建按钮
            2、检查频道名称元素是否存在
        预期：
            1、弹出新建频道页面
            2、页面元素存在
    """
    opteration = Channel_management(browser)
    page = Information_page(browser)
    try:
        # 打开新建频道页面
        opteration.add_channel("自动化频道", "zidonghua", 0)
        # 频道名称是否存在
        result = page.channel_name.is_displayed()
        # 点击新建页面关闭按钮
        page.add_channel_close_button.click()
    except:
        opteration.refresh_channel_management(browser)
        result = False
    assert result == True


@pytest.mark.dependency(depends=["test_02"])
def test_03(browser):
    """
    新建频道校验
        步骤：1、点击新建按钮
            2、输入频道名称、编码，点击保存按钮
            3、判断频道名称是否正确
        预期：
            1、弹出新建频道页面
            2、保存成功
            3、频道名称正确
    """
    opteration = Channel_management(browser)
    page = Information_page(browser)
    try:
        # 新建频道
        opteration.add_channel("自动化频道", "zidonghua", 1)
        time.sleep(2)
        # 获取第一个频道名称
        channel_name = page.frist_data.text
    except:
        opteration.refresh_channel_management(browser)
        channel_name = False
    assert channel_name == "自动化频道"


@pytest.mark.dependency(depends=["test_03"])
def test_04(browser):
    """
    编辑频道页面校验
        步骤：1、点击编辑按钮
            2、检查频道名称元素是否存在
        预期：
            1、弹出编辑频道页面
            2、页面元素存在
    """
    opteration = Channel_management(browser)
    page = Information_page(browser)
    try:
        # 打开编辑频道页面
        opteration.edit_channel("编辑自动化频道", "zidonghua", 0)
        # 频道名称是否存在
        result = page.channel_name.is_displayed()
        # 点击新建页面关闭按钮
        page.edit_channel_close_button.click()
    except:
        opteration.refresh_channel_management(browser)
        result = False
    assert result == True


@pytest.mark.dependency(depends=["test_04"])
def test_05(browser):
    """
    编辑频道校验
        步骤：1、点击编辑按钮
            2、输入频道名称、编码，点击保存按钮
            3、判断频道名称是否正确
        预期：
            1、弹出编辑频道页面
            2、保存成功
            3、频道名称正确
    """
    opteration = Channel_management(browser)
    page = Information_page(browser)
    try:
        # 编辑频道
        opteration.edit_channel("修改自动化频道", "zidonghua", 1)
        time.sleep(2)
        # 获取第一个频道名称
        channel_name = page.frist_data.text
    except:
        opteration.refresh_channel_management(browser)
        channel_name = False
    assert channel_name == "修改自动化频道"


@pytest.mark.dependency(depends=["test_05"])
def test_06(browser):
    """
    查看频道校验
        步骤：1、点击频道名称
            2、获取频道名称，判断频道名称是否正确
        预期：
            1、弹出查看频道页面
            2、频道名称正确
    """
    opteration = Channel_management(browser)
    page = Information_page(browser)
    try:
        # 点击频道名称
        page.frist_data.click()
        # 获取频道名称
        channel_name = page.see_channel_name.text
        # 点击关闭按钮
        page.see_channel_close_button.click()
    except:
        opteration.refresh_channel_management(browser)
        channel_name = False
    assert channel_name == "修改自动化频道"


@pytest.mark.dependency(depends=["test_06"])
def test_07(browser):
    """
    查询频道校验
        步骤：1、输入频道名称，点击搜索按钮
            2、判断频道名称是否正确
        预期：
            1、搜索成功
            2、频道名称正确
    """
    opteration = Channel_management(browser)
    opteration_office = Office_method(browser)
    page = Information_page(browser)
    try:
        # 查询频道
        opteration_office.query(page.channel_management_query, "修改自动化频道", page.channel_management_query_button)
        time.sleep(2)
        # 获取第一个频道名称
        channel_name = page.frist_data.text
    except:
        opteration.refresh_channel_management(browser)
        channel_name = False
    assert channel_name == "修改自动化频道"


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
    opteration = Channel_management(browser)
    try:
        # 点击设计按钮
        page.channel_management_design_button.click()
        result1 = page.design_channel_basics.is_displayed()
        # 点击列表字段设置
        page.design_channel_field.click()
        result2 = page.design_channel_add_button.is_displayed()
        result = result1 and result2
        # 点击页面关闭按钮
        page.design_channel_close_button.click()
    except:
        opteration.refresh_channel_management(browser)
        result = False
    assert result == True


@pytest.mark.dependency(depends=["test_08"])
def test_09(browser):
    """
    设计频道查询校验
        步骤：1、点击设计按钮
            2、输入字段名称点击查询按钮
        预期：
            1、打开设计页面
            2、查询成功
    """
    page = Information_page(browser)
    opteration = Channel_management(browser)
    opteration_office = Office_method(browser)
    try:
        # 点击设计按钮
        page.channel_management_design_button.click()
        # 点击列表字段设置
        page.design_channel_field.click()
        # 查询标题
        opteration_office.query(page.design_channel_query, "标题", page.design_channel_query_button)
        time.sleep(1)
        # 获取第一条数据的名称
        frist_name = page.design_channel_frist_field.text
        page.design_channel_clear_button.click()
    except:
        opteration.refresh_channel_management(browser)
        # 点击设计按钮
        page.channel_management_design_button.click()
        frist_name = False
    assert frist_name == "标题"


@pytest.mark.dependency(depends=["test_08"])
def test_10(browser):
    """
    新增字段页面校验
        步骤：1、点击新增按钮
            2、判断基础设置页签元素
        预期：
            1、打开设置页面
            2、基础设置页签元素存在
    """
    page = Information_page(browser)
    opteration = Channel_management(browser)
    try:
        # 点击列表字段设置
        page.design_channel_field.click()
        # 点击添加按钮
        page.design_channel_add_button.click()
        result = page.add_field_shift_right_button.is_displayed()
        # 点击页面关闭按钮
        page.add_field_close_button.click()
    except:
        opteration.refresh_channel_management(browser)
        # 点击设计按钮
        page.channel_management_design_button.click()
        # 点击列表字段设置
        page.design_channel_field.click()
        result = False
    assert result == True


@pytest.mark.dependency(depends=["test_10"])
def test_11(browser):
    """
    新增字段校验
        步骤：1、点击新增按钮
            2、判断基础设置页签元素
        预期：
            1、打开设置页面
            2、基础设置页签元素存在
    """
    page = Information_page(browser)
    opteration = Channel_management(browser)
    opteration_office = Office_method(browser)
    try:
        # 点击添加按钮
        page.design_channel_add_button.click()
        # 获取右边第一个字段名称
        field_name = page.add_field_frist_field.text
        # 选择左边第一个字段
        page.add_field_frist_field.click()
        time.sleep(1)
        # 点击右移按钮
        page.add_field_shift_right_button.click()
        # 点击保存按钮
        page.add_field_save_button.click()
        time.sleep(1)
        # 查询标题
        opteration_office.query(page.design_channel_query, field_name, page.design_channel_query_button)
        time.sleep(1)
        # 获取第一条数据的名称
        frist_name = page.design_channel_frist_field.text
    except:
        opteration.refresh_channel_management(browser)
        # 点击设计按钮
        page.channel_management_design_button.click()
        # 点击列表字段设置
        page.design_channel_field.click()
        frist_name = False
        field_name = "失败"
    assert frist_name == field_name


@pytest.mark.dependency(depends=["test_03"])
def test_12(browser):
    """
    编辑字段页面校验
        步骤：1、点击编辑按钮
            2、判断标题框元素
        预期：
            1、弹出编辑页面
            2、标题元素存在
    """
    page = Information_page(browser)
    opteration = Channel_management(browser)
    try:
        # 点击标题按钮
        page.design_channel_edit_button.click()
        result = page.edit_field_title.is_displayed()
        # 点击页面关闭按钮
        page.edit_field_close_button.click()
    except:
        opteration.refresh_channel_management(browser)
        result = False
    assert result == True


@pytest.mark.dependency(depends=["test_12"])
def test_13(browser):
    """
    编辑字段校验
        步骤：1、点击编辑按钮
            2、判断标题框元素
        预期：
            1、弹出编辑页面
            2、标题元素存在
    """
    page = Information_page(browser)
    opteration = Channel_management(browser)
    opteration_office = Office_method(browser)
    try:
        # 点击字段编辑按钮
        page.design_channel_edit_button.click()
        # 清空标题框
        page.edit_field_title.clear()
        # 输入标题
        page.edit_field_title.send_keys("自动化字段")
        # 点击保存按钮
        page.edit_field_save_button.click()
        # 查询标题
        opteration_office.query(page.design_channel_query, "自动化字段", page.design_channel_query_button)
        time.sleep(1)
        # 获取第一条数据的名称
        frist_name = page.design_channel_frist_field.text
    except:
        opteration.refresh_channel_management(browser)
        # 点击设计按钮
        page.channel_management_design_button.click()
        # 点击列表字段设置
        page.design_channel_field.click()
        frist_name = False
    assert frist_name == "自动化字段"


@pytest.mark.dependency(depends=["test_13"])
def test_14(browser):
    """
    删除字段校验
        步骤：1、点击删除按钮
            2、判断查询结果
        预期：
            1、弹出删除提示页面
            2、判断无搜索结果是否存在
    """
    page = Information_page(browser)
    opteration = Channel_management(browser)
    opteration_office = Office_method(browser)
    try:
        # 查询标题
        opteration_office.query(page.design_channel_query, "自动化字段", page.design_channel_query_button)
        time.sleep(1)
        # 删除字段
        opteration_office.delete(page.design_channel_delete_button)
        # 查询的结果
        no_query = page.no_query_result.text
    except:
        opteration.refresh_channel_management(browser)
        # 点击设计按钮
        page.channel_management_design_button.click()
        # 点击列表字段设置
        page.design_channel_field.click()
        no_query = False
    assert no_query == "无搜索结果"


@pytest.mark.dependency(depends=["test_03"])
def test_15(browser):
    """
    批量删除字段校验
        步骤：1、点击删除按钮
            2、判断查询结果
        预期：
            1、弹出删除提示页面
            2、判断无搜索结果是否存在
    """
    page = Information_page(browser)
    opteration = Channel_management(browser)
    try:
        # 点击清除按钮
        page.design_channel_clear_button.click()
        # 批量删除字段
        page.design_channel_choice_all.click()
        page.design_channel_batch_deletion_button.click()
        time.sleep(1)
        page.ok_button.click()
        time.sleep(1)
        # 结果
        no_data = page.no_data.text
    except:
        opteration.refresh_channel_management(browser)
        # 点击设计按钮
        page.channel_management_design_button.click()
        no_data = False
    assert no_data == "暂无数据"


@pytest.mark.dependency(depends=["test_03"])
def test_16(browser):
    """
    设计页面保存校验
        步骤：1、点击选择表单下拉框，选择表单
            2、点击保存按钮
        预期：
            1、表单被选中
            2、保存成功
    """
    page = Information_page(browser)
    opteration = Channel_management(browser)
    try:
        # 点击基础设置页签
        page.design_channel_basics.click()
        # 点击选择表单下拉按钮
        page.design_channel_choice_form_down_button.click()
        # 选择第一个表单
        page.design_channel_choice_form.click()
        # 点击保存按钮
        page.design_channel_save_button.click()
        # 保存成功提示
        result = page.success_tips.text
    except:
        opteration.refresh_channel_management(browser)
        result = False
    assert result == "保存成功"


@pytest.mark.dependency(depends=["test_02"])
def test_17(browser):
    """
    频道管理发布校验
        步骤：1、点击发布按钮
            2、点击确定按钮
        预期：
            1、弹出确定发布提示
            2、发布成功
    """
    page = Information_page(browser)
    opteration = Channel_management(browser)
    try:
        # 点击发布按钮
        page.channel_management_publish_button.click()
        # 点击ok按钮
        page.ok_button.click()
        # 成功提示
        result = page.success_tips.text
    except:
        opteration.refresh_channel_management(browser)
        result = False
    assert result == "发布成功"


@pytest.mark.dependency(depends=["test_07"])
def test_18(browser):
    """
    删除频道校验
        步骤：1、点击删除按钮，删除频道
            2、判断频道是否被删除
        预期：
            1、频道被删除
            2、频道删除成功
    """
    opteration = Channel_management(browser)
    opteration_office = Office_method(browser)
    page = Information_page(browser)
    try:
        # 删除频道
        opteration_office.delete(page.channel_delete_button)
        time.sleep(2)
        # 查询频道
        opteration_office.query(page.channel_management_query, "修改自动化频道", page.channel_management_query_button)
        time.sleep(2)
        no_search = page.no_query_result.text
    except:
        opteration.refresh_channel_management(browser)
        no_search = False
    assert no_search == "无搜索结果"


@pytest.mark.dependency(depends=["test_02"])
def test_19(browser):
    """
    批量删除频道校验
        步骤：1、点击删除按钮，删除频道
            2、判断频道是否被删除
        预期：
            1、频道被删除
            2、频道删除成功
    """
    opteration = Channel_management(browser)
    opteration_office = Office_method(browser)
    page = Information_page(browser)
    try:
        # 新建频道
        opteration.add_channel("批量删除频道", "piliangshanchu", 1)
        # 查询频道
        opteration_office.query(page.channel_management_query, "批量删除频道", page.channel_management_query_button)
        # 批量删除频道
        opteration_office.batch_delete()
        time.sleep(2)
        no_search = page.no_query_result.text
    except:
        opteration.refresh_channel_management(browser)
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