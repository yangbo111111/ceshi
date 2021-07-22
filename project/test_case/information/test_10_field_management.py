"""
created: 20201221 by yb
description: 字段管理模块用例
Modification History:
1、2021-1-12 yb创建了此文件
"""


from page.information.information_page import Information_page
from test_function.information.field_management import Field_management
from test_function.office_function import Office_method
import pytest
import time


@pytest.mark.dependency()
def test_01(browser):
    """
    ======字段管理菜单开始测试.....=======
    字段管理页面校验
        步骤：1、登录系统，进入后台/内容中心/字段管理
            2、页面元素校验
        预期：
            1、进入字段管理菜单
            2、页面元素存在
    """
    opteration = Field_management(browser)
    page = Information_page(browser)
    try:
        # 进入字段管理
        opteration.star_field_management(browser)
        time.sleep(1)
        # 获取搜索按钮元素
        result = page.field_management_query_button.is_displayed()
    except:
        opteration.refresh_field_management(browser)
        result = False
    assert result == True


@pytest.mark.dependency(depends=["test_01"])
def test_02(browser):
    """
    新建数据表页面校验
        步骤：1、点击新建按钮
            2、检查数据表名称元素是否存在
        预期：
            1、弹出新建数据表页面
            2、页面元素存在
    """
    opteration = Field_management(browser)
    page = Information_page(browser)
    try:
        # 打开新建数据表页面
        opteration.add_data_sheet("自动化数据表", "zidonghuashujvbiao", 0)
        # 获取数据表名称字段
        result = page.field_management_add_data_sheet_name.is_displayed()
        # 点击页面关闭按钮
        page.field_management_add_data_sheet_close_button.click()
    except:
        opteration.refresh_field_management(browser)
        result = False
    assert result == True


@pytest.mark.dependency(depends=["test_02"])
def test_03(browser):
    """
    新建频道模板校验
        步骤：1、点击新建按钮
            2、输入数据表名称、系统名称，点击保存按钮
            3、判断数据表名称是否正确
        预期：
            1、弹出新建数据表页面
            2、保存成功
            3、数据表名称正确
    """
    opteration = Field_management(browser)
    page = Information_page(browser)
    try:
        # 新建数据表
        opteration.add_data_sheet("自动化数据表", "zidonghuashujvbiao1", 1)
        time.sleep(2)
        # 获取第一个数据表名称
        data_name = page.frist_data.text
    except:
        opteration.refresh_field_management(browser)
        data_name = False
    assert data_name == "自动化数据表"


@pytest.mark.dependency(depends=["test_03"])
def test_04(browser):
    """
    编辑数据表页面校验
        步骤：1、点击编辑按钮
            2、检查数据表名称元素是否存在
        预期：
            1、弹出编辑数据表页面
            2、页面元素存在
    """
    opteration = Field_management(browser)
    page = Information_page(browser)
    try:
        # 打开编数据表页面
        opteration.edit_data_sheet("修改自动化数据表", 0)
        time.sleep(1)
        # 数据表名称是否存在
        result = page.field_management_edit_data_sheet_name.is_displayed()
        # 点击编辑页面关闭按钮
        page.field_management_edit_data_sheet_close_button.click()
    except:
        opteration.refresh_field_management(browser)
        result = False
    assert result == True


@pytest.mark.dependency(depends=["test_04"])
def test_05(browser):
    """
    编辑数据表校验
        步骤：1、点击编辑按钮
            2、输入数据表名称，点击保存按钮
            3、判断数据表名称是否正确
        预期：
            1、弹出编辑数据表页面
            2、保存成功
            3、数据表名称正确
    """
    opteration = Field_management(browser)
    page = Information_page(browser)
    try:
        # 编辑数据表
        opteration.edit_data_sheet("修改自动化数据表", 1)
        time.sleep(2)
        # 获取第一个数据表名称
        data_name = page.frist_data.text
    except:
        opteration.refresh_field_management(browser)
        data_name = False
    assert data_name == "修改自动化数据表"


@pytest.mark.dependency(depends=["test_05"])
def test_06(browser):
    """
    查看数据表校验
        步骤：1、点击数据表名称
            2、获取数据表名称，判断数据表名称是否正确
        预期：
            1、弹出查看数据表页面
            2、数据表名称正确
    """
    opteration = Field_management(browser)
    page = Information_page(browser)
    try:
        # 点击数据表名称
        page.frist_data.click()
        # 获取数据表名称
        data_name = page.field_management_view_data_sheet_name.text
        # 点击关闭按钮
        page.field_management_view_data_sheet_close_button.click()
    except:
        opteration.refresh_field_management(browser)
        data_name = False
    assert data_name == "修改自动化数据表"


@pytest.mark.dependency(depends=["test_05"])
def test_07(browser):
    """
    查询数据表校验
        步骤：1、输入数据表名称，点击搜索按钮
            2、判断数据表名称是否正确
        预期：
            1、搜索成功
            2、数据表名称正确
    """
    opteration = Field_management(browser)
    opteration_office = Office_method(browser)
    page = Information_page(browser)
    try:
        # 查询数据表
        opteration_office.query(page.field_management_query, "修改自动化数据表", page.field_management_query_button)
        time.sleep(2)
        # 获取第一个数据表名称
        data_name = page.frist_data.text
    except:
        opteration.refresh_field_management(browser)
        data_name = False
    assert data_name == "修改自动化数据表"


# @pytest.mark.dependency(depends=["test_03"])
# def test_08(browser):
#     """
#     同步数据表校验
#         步骤：1、同步按钮
#             2、判断提示语是否正确
#         预期：
#             1、同步成功
#             2、提示语正确
#     """
#     opteration = Field_management(browser)
#     page = Information_page(browser)
#     try:
#         # 点击同步按钮
#         page.field_management_sync_button.click()
#         time.sleep(1)
#         page.ok_button.click()
#         # 获取同步成功提示语
#         success_tips = page.success_tips.text
#     except:
#         opteration.refresh_field_management(browser)
#         success_tips = False
#     assert success_tips == "数据表已同步到数据库"


@pytest.mark.dependency(depends=["test_04"])
def test_09(browser):
    """
    复制数据表校验
        步骤：1、点击复制按钮
            2、输入数据表名称，点击保存按钮
            3、判断数据表名称是否正确
        预期：
            1、弹出复制数据表页面
            2、保存成功
            3、数据表名称正确
    """
    opteration = Field_management(browser)
    opteration_office = Office_method(browser)
    page = Information_page(browser)
    try:
        # 复制数据表
        opteration.copy_data_sheet("复制自动化数据表", "fuzhishujvbiao")
        # 查询数据表
        opteration_office.query(page.field_management_query, "复制自动化数据表", page.field_management_query_button)
        time.sleep(2)
        # 获取第一个数据表名称
        data_name = page.frist_data.text
    except:
        opteration.refresh_field_management(browser)
        data_name = False
    assert data_name == "复制自动化数据表"


# @pytest.mark.dependency(depends=["test_09"])
# def test_10(browser):
#     """
#     同步数据表校验
#         步骤：1、同步按钮
#             2、判断提示语是否正确
#         预期：
#             1、同步成功
#             2、提示语正确
#     """
#     opteration = Field_management(browser)
#     page = Information_page(browser)
#     try:
#         # 选中第一条数据
#         page.choice_frist_data.click()
#         # 点击批量同步按钮
#         page.field_management_batch_sync_button.click()
#         page.ok_button.click()
#         time.sleep(1)
#         # 获取同步成功提示语
#         success_tips = page.success_tips.text
#     except:
#         opteration.refresh_field_management(browser)
#         success_tips = False
#     assert success_tips == "数据表已同步到数据库"


@pytest.mark.dependency(depends=["test_09"])
def test_11(browser):
    """
    删除数据表校验
        步骤：1、点击删除按钮，删除数据表
            2、判断数据表是否被删除
        预期：
            1、数据表被删除
            2、数据表删除成功
    """
    opteration = Field_management(browser)
    opteration_office = Office_method(browser)
    page = Information_page(browser)
    try:
        # 删除数据表
        opteration_office.delete(page.field_management_delete_button)
        time.sleep(2)
        # 查询数据表
        opteration_office.query(page.field_management_query, "复制自动化数据表", page.field_management_query_button)
        time.sleep(2)
        no_search = page.no_query_result.text
    except:
        opteration.refresh_field_management(browser)
        no_search = False
    assert no_search == "无搜索结果"


@pytest.mark.dependency(depends=["test_07"])
def test_12(browser):
    """
    批量删除数据表校验
        步骤：1、点击删除按钮，删除数据表
            2、判断数据表是否被删除
        预期：
            1、数据表被删除
            2、数据表删除成功
    """
    opteration = Field_management(browser)
    opteration_office = Office_method(browser)
    page = Information_page(browser)
    try:
        # 查询数据表
        opteration_office.query(page.field_management_query, "修改自动化数据表", page.field_management_query_button)
        time.sleep(1)
        # 批量删除频道
        opteration_office.batch_delete()
        time.sleep(1)
        no_search = page.no_query_result.text
    except:
        opteration.refresh_field_management(browser)
        no_search = False
    assert no_search == "无搜索结果"


@pytest.mark.dependency(depends=["test_03"])
def test_13(browser):
    """
    字段设置页面校验
        步骤：1、新建数据表
            2、点击字段设置按钮
            3、判断批量新增按钮是否存在
        预期：
            1、新增成功
            2、进入字段设置页面
            3、批量新增按钮存在
    """
    opteration = Field_management(browser)
    page = Information_page(browser)
    try:
        # 点击字段管理菜单
        page.field_management.click()
        # 新建数据表
        opteration.add_data_sheet("自动化字段设置", "zidonghuaziduan", 1)
        time.sleep(1)
        # 点击字段设置按钮
        page.field_management_field_setup_button.click()
        time.sleep(1)
        result = page.field_setup_batch_add_button.is_displayed()
    except:
        opteration.refresh_field_setup(browser)
        result = False
    assert result == True


@pytest.mark.dependency(depends=["test_12"])
def test_14(browser):
    """
    新增字段页面校验
        步骤：1、点击新建按钮
            2、判断字段名称是否存在
        预期：
            1、弹出新建页面
            2、字段名称存在
    """
    opteration = Field_management(browser)
    page = Information_page(browser)
    try:
        # 新建字段
        opteration.add_field("自动化字段", 0)
        # 判断元素
        result = page.field_setup_field_name.is_displayed()
        # 关闭页面
        page.field_setup_add_field_close_button.click()
    except:
        opteration.refresh_field_setup(browser)
        result = False
    assert result == True


@pytest.mark.dependency(depends=["test_12"])
def test_15(browser):
    """
    新增字段校验
        步骤：1、点击新建按钮，创建字段
            2、判断字段名称是否正确
        预期：
            1、新增成功
            2、字段名称正确
    """
    opteration = Field_management(browser)
    page = Information_page(browser)
    try:
        # 新建字段
        opteration.add_field("自动化字段", 1)
        time.sleep(1)
        # 获取字段名称
        field_name = page.frist_data.text
    except:
        opteration.refresh_field_setup(browser)
        field_name = False
    assert field_name == "自动化字段"


@pytest.mark.dependency(depends=["test_15"])
def test_16(browser):
    """
    编辑字段页面校验
        步骤：1、点击编辑按钮
            2、判断字段名称是否存在
        预期：
            1、弹出编辑页面
            2、字段名称存在
    """
    opteration = Field_management(browser)
    page = Information_page(browser)
    try:
        # 编辑字段
        opteration.edit_field("修改自动化字段", 0)
        # 判断元素
        result = page.field_setup_field_name.is_displayed()
        # 关闭页面
        page.field_setup_edit_field_close_button.click()
    except:
        opteration.refresh_field_setup(browser)
        result = False
    assert result == True


@pytest.mark.dependency(depends=["test_16"])
def test_17(browser):
    """
    编辑字段校验
        步骤：1、点击编辑按钮，编辑字段
            2、判断字段名称是否正确
        预期：
            1、编辑成功
            2、字段名称正确
    """
    opteration = Field_management(browser)
    page = Information_page(browser)
    try:
        # 编辑字段
        opteration.edit_field("修改自动化字段", 1)
        time.sleep(1)
        # 获取字段名称
        field_name = page.frist_data.text
    except:
        opteration.refresh_field_setup(browser)
        field_name = False
    assert field_name == "修改自动化字段"


@pytest.mark.dependency(depends=["test_17"])
def test_18(browser):
    """
    查看字段校验
        步骤：1、点击字段名称
            2、获取字段名称，判断字段是否正确
        预期：
            1、弹出查看字段页面
            2、字段名称正确
    """
    opteration = Field_management(browser)
    page = Information_page(browser)
    try:
        # 点击字段名称
        page.frist_data.click()
        # 获取字段名称
        field_name = page.field_setup_view_field_name.text
        # 点击关闭按钮
        page.field_setup_view_field_close_button.click()
    except:
        opteration.refresh_field_setup(browser)
        field_name = False
    assert field_name == "修改自动化字段"


@pytest.mark.dependency(depends=["test_05"])
def test_19(browser):
    """
    查询数据表校验
        步骤：1、输入数据表名称，点击搜索按钮
            2、判断数据表名称是否正确
        预期：
            1、搜索成功
            2、数据表名称正确
    """
    opteration = Field_management(browser)
    opteration_office = Office_method(browser)
    page = Information_page(browser)
    try:
        # 查询字段
        opteration_office.query(page.field_setup_query, "修改自动化字段", page.field_management_query_button)
        time.sleep(1)
        # 获取第一个字段名称
        data_name = page.frist_data.text
    except:
        opteration.refresh_field_setup(browser)
        data_name = False
    assert data_name == "修改自动化字段"


@pytest.mark.dependency(depends=["test_12"])
def test_20(browser):
    """
    属性设置页面校验
        步骤：1、点击属性设置按钮
            2、判断元素是否存在
        预期：
            1、弹出属性设置页面
            2、元素存在
    """
    opteration = Field_management(browser)
    page = Information_page(browser)
    try:
        # 点击属性设置按钮
        page.field_setup_attribute_button.click()
        time.sleep(1)
        # 获取第一个字段名称
        result = page.field_setup_attribute_close_button.is_displayed()
        page.field_setup_attribute_close_button.click()
    except:
        opteration.refresh_field_setup(browser)
        result = False
    assert result == True


@pytest.mark.dependency(depends=["test_12"])
def test_21(browser):
    """
    删除字段校验
        步骤：1、点击删除按钮，删除字段
            2、判断字段是否被删除
        预期：
            1、数据表被删除
            2、数据表删除成功
    """
    opteration = Field_management(browser)
    opteration_office = Office_method(browser)
    page = Information_page(browser)
    try:
        # 删除字段
        opteration_office.delete(page.field_setup_delete_button)
        time.sleep(1)
        # 查询字段
        opteration_office.query(page.field_setup_query, "修改自动化字段", page.field_management_query_button)
        time.sleep(1)
        no_search = page.no_query_result.text
        page.field_management_clear_button.click()
    except:
        opteration.refresh_field_management(browser)
        no_search = False
    assert no_search == "无搜索结果"


@pytest.mark.dependency(depends=["test_12"])
def test_22(browser):
    """
    批量新增字段页面校验
        步骤：1、点击批量新建按钮
            2、判断字段名称是否存在
        预期：
            1、弹出批量新建页面
            2、字段名称存在
    """
    opteration = Field_management(browser)
    page = Information_page(browser)
    try:
        # 新建字段
        opteration.batch_add_field("批量新增自动化字段", 0)
        # 判断元素
        result = page.field_setup_batch_field_name.is_displayed()
        # 关闭页面
        page.field_setup_batch_add_field_close_button.click()
    except:
        opteration.refresh_field_setup(browser)
        result = False
    assert result == True


@pytest.mark.dependency(depends=["test_22"])
def test_23(browser):
    """
    批量新增字段校验
        步骤：1、点击批量新建按钮，创建字段
            2、判断字段名称是否正确
        预期：
            1、新增成功
            2、字段名称正确
    """
    opteration = Field_management(browser)
    page = Information_page(browser)
    try:
        # 新建字段
        opteration.batch_add_field("批量新增自动化字段", 1)
        time.sleep(1)
        # 获取字段名称
        field_name = page.frist_data.text
    except:
        opteration.refresh_field_setup(browser)
        field_name = False
    assert field_name == "批量新增自动化字段"


@pytest.mark.dependency(depends=["test_23"])
def test_24(browser):
    """
    批量编辑字段页面校验
        步骤：1、选择数据点击批量修改按钮
            2、判断字段名称是否存在
        预期：
            1、弹出批量编辑页面
            2、字段名称存在
    """
    opteration = Field_management(browser)
    page = Information_page(browser)
    try:
        # 选择第一条数据
        page.choice_frist_data.click()
        # 点击批量修改按钮
        page.field_setup_batch_edit_button.click()
        # 判断元素
        result = page.field_setup_batch_field_name.is_displayed()
        # 关闭页面
        page.field_setup_batch_edit_field_close_button.click()
    except:
        opteration.refresh_field_setup(browser)
        result = False
    assert result == True


@pytest.mark.dependency(depends=["test_24"])
def test_25(browser):
    """
    批量编辑字段校验
        步骤：1、点击批量编辑按钮，编辑字段
            2、判断字段名称是否正确
        预期：
            1、编辑成功
            2、字段名称正确
    """
    opteration = Field_management(browser)
    page = Information_page(browser)
    try:
        # 编辑字段
        opteration.batch_edit_field("批量修改自动化字段")
        time.sleep(1)
        # 获取字段名称
        field_name = page.frist_data.text
    except:
        opteration.refresh_field_setup(browser)
        field_name = False
    assert field_name == "批量修改自动化字段"


@pytest.mark.dependency(depends=["test_25"])
def test_26(browser):
    """
    批量删除字段校验
        步骤：1、点击删除按钮，删除数据表
            2、判断数据表是否被删除
        预期：
            1、数据表被删除
            2、数据表删除成功
    """
    opteration = Field_management(browser)
    opteration_office = Office_method(browser)
    page = Information_page(browser)
    try:
        # 查询数据表
        opteration_office.query(page.field_setup_query, "批量修改自动化字段", page.field_management_query_button)
        # 批量删除频道
        opteration_office.batch_delete()
        time.sleep(1)
        no_search = page.no_query_result.text
    except:
        opteration.refresh_field_management(browser)
        no_search = False
    assert no_search == "无搜索结果"


@pytest.mark.dependency()
def test_end(browser):
    """
    ======字段管理菜单结束测试.....=======

    """
    page = Information_page(browser)
    opteration_office = Office_method(browser)
    # 点击字段管理
    page.field_management.click()
    # 删除数据表
    opteration_office.delete(page.field_management_delete_button)
    # 登出
    opteration_office.logout()