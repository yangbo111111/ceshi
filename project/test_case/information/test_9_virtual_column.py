"""
created: 20201230 by yb
description: 虚拟栏目模块用例
Modification History:
1、2020-12-30 yb创建了此文件
"""


from page.information.information_page import Information_page
from test_function.information.virtual_column_function import Virtual_column
from test_function.office_function import Office_method
import pytest
import time


@pytest.mark.dependency()
def test_01(browser):
    """
    ======虚拟栏目菜单开始测试.....=======
    频道管理页面校验
        步骤：1、登录系统，进入后台/内容中心/虚拟栏目
            2、页面元素校验
        预期：
            1、进入虚拟栏目菜单
            2、页面元素存在
    """
    opteration = Virtual_column(browser)
    page = Information_page(browser)
    try:
        # 进入虚拟栏目
        opteration.star_virtual_column(browser, "自动化栏目")
        # 获取搜索按钮元素
        result = page.virtual_column_name.is_displayed()
    except:
        opteration.refresh_virtual_column(browser)
        result = False
    assert result == True


@pytest.mark.dependency(depends=["test_01"])
def test_02(browser):
    """
    新建虚拟栏目校验
        步骤：1、输入模板名称、编码，点击保存按钮
            2、判断虚拟栏目名称是否正确
        预期：
            1、保存成功
            2、虚拟栏目名称正确
    """
    opteration = Virtual_column(browser)
    page = Information_page(browser)
    try:
        # 新建虚拟栏目
        opteration.add_virtual_column("自动化栏目")
        time.sleep(2)
        # 获取左侧第一个栏目的名称
        template_name = page.virtual_column_frist_column.text
    except:
        opteration.refresh_virtual_column(browser)
        template_name = False
    assert template_name == "自动化栏目"


@pytest.mark.dependency(depends=["test_01"])
def test_03(browser):
    """
    查询虚拟栏目校验
        步骤：1、输入栏目名称，点击搜索按钮
            2、判断栏目名称是否正确
        预期：
            1、搜索成功
            2、栏目名称正确
    """
    opteration = Virtual_column(browser)
    opteration_office = Office_method(browser)
    page = Information_page(browser)
    try:
        # 查询栏目
        opteration_office.query(page.virtual_column_query, "自动化栏目", page.virtual_column_query_button)
        time.sleep(2)
        # 获取第一个栏目名称
        column_name = page.virtual_column_frist_column.text
    except:
        opteration.refresh_virtual_column(browser)
        column_name = False
    assert column_name == "自动化栏目"


@pytest.mark.dependency(depends=["test_01"])
def test_04(browser):
    """
    下级栏目页面校验
        步骤：1、点击栏目、点击下级栏目
            2、判断新建按钮元素是否存在
        预期：
            1、进入新建下级栏目列表
            2、新建元素存在
    """
    opteration = Virtual_column(browser)
    page = Information_page(browser)
    try:
        # 点击左侧第一个栏目
        page.virtual_column_frist_column.click()
        time.sleep(1)
        # 点击下级栏目
        page.virtual_column_lower_column.click()
        # 判断新建按钮是否存在
        result = page.lower_virtual_add_button.is_displayed()
    except:
        opteration.refresh_virtual_column(browser)
        # 点击左侧第一个栏目
        page.virtual_column_frist_column.click()
        time.sleep(1)
        # 点击下级栏目
        page.virtual_column_lower_column.click()
        result = False
    assert result == True


@pytest.mark.dependency(depends=["test_04"])
def test_05(browser):
    """
    新建下级虚拟栏目页面校验
        步骤：1、点击新建下级虚拟栏目
            2、判断栏目名称元素是否存在
        预期：
            1、弹出新增下级虚拟栏目页面
            2、栏目名称元素存在
    """
    opteration = Virtual_column(browser)
    page = Information_page(browser)
    try:
        # 点击新建按钮
        page.lower_virtual_add_button.click()
        # 判断栏目名称是否存在
        result = page.lower_virtual_column_name.is_displayed()
    except:
        opteration.refresh_virtual_column(browser)
        result = False
    assert result == True


@pytest.mark.dependency(depends=["test_05"])
def test_06(browser):
    """
    选择关联栏目页面校验
        步骤：1、点击新建下级虚拟栏目
            2、点击选择关联栏目按钮
            3、判断栏目名称元素是否存在
        预期：
            1、弹出新增下级虚拟栏目页面
            2、弹出选择关联栏目页面
            3、栏目名称元素存在
    """
    opteration = Virtual_column(browser)
    page = Information_page(browser)
    try:
        # 点击选择关联栏目按钮
        page.lower_virtual_column_chose_button.click()
        # 判断栏目查询框是否存在
        result = page.connected_column_query.is_displayed()
        time.sleep(1)
    except:
        opteration.refresh_virtual_column(browser)
        result = False
    assert result == True


@pytest.mark.dependency(depends=["test_06"])
def test_07(browser):
    """
    关联栏目查询校验
        步骤：1、点击选择关联栏目按钮
            2、输入栏目名称查询
            3、判断查询结果
        预期：
            1、弹出新增下级虚拟栏目页面
            2、查询成功
            3、查询结果正确
    """
    opteration = Virtual_column(browser)
    opteration_office = Office_method(browser)
    page = Information_page(browser)
    try:
        # 查询栏目
        opteration_office.query(page.connected_column_query, "自动化栏目", page.connected_column_query_button)
        time.sleep(1)
        # 获取第一个栏目名称
        column_name = page.connected_column_frist_column.text
        time.sleep(1)
        # 关联栏目页面
        page.connected_column_close_button.click()
        # 关闭新建下级栏目页面
        page.lower_virtual_column_close_button.click()
    except:
        opteration.refresh_virtual_column(browser)
        # 点击左侧第一个栏目
        page.virtual_column_frist_column.click()
        time.sleep(1)
        # 点击下级栏目
        page.virtual_column_lower_column.click()
        column_name = False
    assert column_name == "自动化栏目"


@pytest.mark.dependency(depends=["test_04"])
def test_08(browser):
    """
    新建下级栏目校验
        步骤：1、新建下级栏目
            2、判断新建栏目名称是否正确
        预期：
            1、新建成功
            2、栏目名称正确
    """
    opteration = Virtual_column(browser)
    opteration_office = Office_method(browser)
    page = Information_page(browser)
    try:
        # 新建栏目
        opteration.add_lower_virtual_column("自动化下级栏目")
        time.sleep(1)
        # 查询栏目
        opteration_office.query(page.virtual_column_query, "自动化下级栏目", page.virtual_column_query_button)
        time.sleep(1)
        # 获取第一个栏目名称
        column_name = page.virtual_column_frist_column.text
    except:
        opteration.refresh_virtual_column(browser)
        # 点击左侧第一个栏目
        page.virtual_column_frist_column.click()
        time.sleep(1)
        # 点击下级栏目
        page.virtual_column_lower_column.click()
        column_name = False
    assert column_name == "自动化下级栏目"


@pytest.mark.dependency(depends=["test_04"])
def test_09(browser):
    """
    修改下级栏目页面校验
        步骤：1、点击编辑按钮
            2、判断编辑页面元素是否存在
        预期：
            1、弹出编辑页面
            2、编辑页面元素存在
    """
    opteration = Virtual_column(browser)
    page = Information_page(browser)
    try:
        # 点击编辑按钮
        opteration.edit_lower_virtual_column("自动化修改下级栏目", 0)
        # 获取编辑页面元素
        result = page.edit_lower_virtual_column_name.is_displayed()
        time.sleep(1)
        # 点击页面关闭按钮
        page.edit_lower_virtual_column_close_button.click()
    except:
        opteration.refresh_virtual_column(browser)
        # 点击左侧第一个栏目
        page.virtual_column_frist_column.click()
        time.sleep(1)
        # 点击下级栏目
        page.virtual_column_lower_column.click()
        result = False
    assert result == True


@pytest.mark.dependency(depends=["test_09"])
def test_10(browser):
    """
    编辑下级栏目校验
        步骤：1、点击编辑按钮
            2、修改栏目名称保存
            3、查询栏目是否存在
        预期：
            1、弹出编辑页面
            2、保存成功
            3、栏目名称存在
    """
    opteration = Virtual_column(browser)
    opteration_office = Office_method(browser)
    page = Information_page(browser)
    try:
        # 编辑栏目
        opteration.edit_lower_virtual_column("自动化修改下级栏目", 1)
        time.sleep(1)
        # 查询栏目
        opteration_office.query(page.virtual_column_query, "自动化修改下级栏目", page.virtual_column_query_button)
        time.sleep(1)
        # 获取第一个栏目名称
        column_name = page.virtual_column_frist_column.text
    except:
        opteration.refresh_virtual_column(browser)
        # 点击左侧第一个栏目
        page.virtual_column_frist_column.click()
        time.sleep(1)
        # 点击下级栏目
        page.virtual_column_lower_column.click()
        column_name = False
    assert column_name == "自动化修改下级栏目"


@pytest.mark.dependency(depends=["test_08"])
def test_11(browser):
    """
    查看下级栏目校验
        步骤：1、新建下级栏目
            2、查看栏目名称是否正确
        预期：
            1、新建成功
            2、栏目名称正确
    """
    opteration = Virtual_column(browser)
    page = Information_page(browser)
    try:
        # 新建栏目
        opteration.add_lower_virtual_column("自动化查看栏目")
        time.sleep(1)
        # 点击标题名称
        page.frist_data.click()
        # 获取查看页面栏目名称
        column_name = page.see_lower_virtual_column_name.text
        time.sleep(1)
        # 点击页面关闭按钮
        page.see_lower_virtual_close_button.click()
    except:
        opteration.refresh_virtual_column(browser)
        # 点击左侧第一个栏目
        page.virtual_column_frist_column.click()
        time.sleep(1)
        # 点击下级栏目
        page.virtual_column_lower_column.click()
        column_name = False
    assert column_name == "自动化查看栏目"


@pytest.mark.dependency(depends=["test_11"])
def test_12(browser):
    """
    批量移动栏目页面校验
        步骤：1、选择记录，点击批量移动按钮
            2、判断查询框是否存在
        预期：
            1、弹出选择栏目页面
            2、查询框元素存在
    """
    opteration = Virtual_column(browser)
    page = Information_page(browser)
    try:
        # 选择数据
        page.lower_virtual_chose_frist_data.click()
        time.sleep(1)
        # 点击批量移动按钮
        page.lower_virtual_move_button.click()
        time.sleep(1)
        # 判断查询框是否存在
        result = page.move_lower_virtual_column_query.is_displayed()
    except:
        opteration.refresh_virtual_column(browser)
        # 点击左侧第一个栏目
        page.virtual_column_frist_column.click()
        time.sleep(1)
        # 点击下级栏目
        page.virtual_column_lower_column.click()
        result = False
    assert result == True


@pytest.mark.dependency(depends=["test_12"])
def test_13(browser):
    """
    批量移动栏目查询校验
        步骤：1、输入栏目名称查询
            2、判断查询结果是否正确
        预期：
            1、查询成功
            2、栏目名称正确
    """
    opteration = Virtual_column(browser)
    opteration_office = Office_method(browser)
    page = Information_page(browser)
    try:
        # 查询栏目
        opteration_office.query(page.move_lower_virtual_column_query, "自动化修改下级栏目", page.move_lower_virtual_column_query_button)
        time.sleep(1)
        # 获取栏目名称
        column_name = page.move_lower_virtual_column_frist_column.text
    except:
        opteration.refresh_virtual_column(browser)
        # 点击左侧第一个栏目
        page.virtual_column_frist_column.click()
        time.sleep(1)
        # 点击下级栏目
        page.virtual_column_lower_column.click()
        column_name = False
    assert column_name == "自动化修改下级栏目"


@pytest.mark.dependency(depends=["test_13"])
def test_14(browser):
    """
    批量移动栏目校验
        步骤：1、选择第一个栏目
            2、点击保存按钮
        预期：
            1、栏目被选中
            2、移动成功
    """
    opteration = Virtual_column(browser)
    page = Information_page(browser)
    try:
        # 点击第一个栏目
        page.move_lower_virtual_column_frist_column.click()
        # 点击保存按钮
        page.move_lower_virtual_column_save_button.click()
        # 获取移动成功提示语
        success_tips = page.success_tips.text
    except:
        opteration.refresh_virtual_column(browser)
        # 点击左侧第一个栏目
        page.virtual_column_frist_column.click()
        time.sleep(1)
        # 点击下级栏目
        page.virtual_column_lower_column.click()
        success_tips = False
    assert success_tips == "移动栏目成功！"


@pytest.mark.dependency(depends=["test_10"])
def test_15(browser):
    """
    删除下级栏目校验
        步骤：1、点击删除按钮，删除栏目
            2、判断栏目是否被删除
        预期：
            1、栏目被删除
            2、栏目删除成功
    """
    opteration = Virtual_column(browser)
    opteration_office = Office_method(browser)
    page = Information_page(browser)
    try:
        # 删除下级栏目
        opteration_office.delete(page.lower_virtual_delete_button)
        time.sleep(1)
        # 查询下级栏目
        opteration_office.query(page.virtual_column_query, "自动化修改下级栏目", page.virtual_column_query_button)
        time.sleep(1)
        no_search = page.virtual_column_no_query.text
    except:
        opteration.refresh_virtual_column(browser)
        # 点击左侧第一个栏目
        page.virtual_column_frist_column.click()
        time.sleep(1)
        # 点击下级栏目
        page.virtual_column_lower_column.click()
        no_search = False
    assert no_search == "无搜索结果"


@pytest.mark.dependency(depends=["test_08"])
def test_16(browser):
    """
    批量删除栏目校验
        步骤：1、新建下级栏目
            2、批量删除栏目
        预期：
            1、新建成功
            2、栏目删除成功
    """
    opteration = Virtual_column(browser)
    opteration_office = Office_method(browser)
    page = Information_page(browser)
    try:
        # 新建栏目
        opteration.add_lower_virtual_column("批量删除栏目")
        time.sleep(1)
        # 批量删除栏目
        opteration_office.batch_delete()
        # 查询下级栏目
        opteration_office.query(page.virtual_column_query, "批量删除栏目", page.virtual_column_query_button)
        time.sleep(1)
        # 未查询到结果
        no_search = page.virtual_column_no_query.text
    except:
        opteration.refresh_virtual_column(browser)
        # 点击左侧第一个栏目
        page.virtual_column_frist_column.click()
        time.sleep(1)
        # 点击下级栏目
        page.virtual_column_lower_column.click()
        no_search = False
    assert no_search == "无搜索结果"


@pytest.mark.dependency()
def test_end(browser):
    """
    ======虚拟栏目菜单结束测试.....=======

    """
    opteration = Virtual_column(browser)
    page = Information_page(browser)
    opteration_office = Office_method(browser)
    # 点击虚拟栏目
    page.virtual_column.click()
    time.sleep(1)
    # 删除创建的数据
    opteration.end_lower_virtual_column(browser)
    # 登出
    opteration_office.logout()


if __name__ == '__main__':
    pytest.main()


