"""
created: 202008018 by zly
description: 栏目内容模块用例
Modification History:
1、2020-8-31 yb创建了此文件
"""
from page.information.information_page import Information_page
from test_function.office_function import Office_method
from test_function.information.column_content_function import Column_Content
from test_function.information.column_management_function import Column_Management
import pytest
import time


@pytest.mark.dependency(depends=["test_case/information/test_2_column_management.py::test_03"], scope='session')
@pytest.mark.dependency()
def test_init(browser):
    """
    ======栏目内容菜单开始测试.....=======
        步骤：1、登录系统，点击信息、栏目管理
            2、增加栏目
    """
    opteration = Column_Content(browser)
    # 进入信息
    opteration.go_information(browser)
    # 增加栏目
    opteration.add_column(browser, "自动化栏目", "zidonghua", "自动化栏目内容")


@pytest.mark.dependency(depends=["test_init"])
def test_01(browser):
    """  栏目内容列表
        步骤：1、登录系统，点击信息、栏目内容
            2、检查增加的栏目是否存在
        预期：1、进入栏目内容列表
            2、页面正常、栏目存在
    """
    opteration = Column_Content(browser)
    page = Information_page(browser)
    try:
        # 进入栏目内容菜单
        opteration.star_column_content()
        # 获取左侧树第一个栏目的名称
        frist_column = page.information_frist_column.text
    except:
        opteration.refresh_column_content(browser)
        frist_column = False
    assert frist_column == "自动化栏目"


@pytest.mark.dependency(depends=["test_01"])
def test_02(browser):
    """ 信息新增页面校验
        步骤：1、点击栏目，点击新建按钮
            2、检查标题是否存在
            3、关闭页面
        预期：1、弹出新建页面
            2、页面正常、标题存在
            3、页面被关闭
    """
    opteration = Column_Content(browser)
    page = Information_page(browser)
    try:
        # 打开新建页面
        opteration.add_information("自动化信息", "自动化信息内容", 0, browser)
        # 检查标题
        result = page.information_name.is_displayed()
        # 点击页面关闭按钮
        page.infromaton_close_button.click()
    except:
        opteration.refresh_column_content(browser)
        result = False
    assert result == True


@pytest.mark.dependency(depends=["test_02"])
def test_03(browser):
    """ 信息新增校验
        步骤：1、点击栏目，点击新建按钮
            2、填写标题、内容，保存
            3、检查信息标题是否正确
        预期：1、弹出新建页面
            2、信息增加成功
            3、标题正确
    """
    opteration = Column_Content(browser)
    page = Information_page(browser)
    try:
        # 增加信息
        opteration.add_information("自动化信息", "自动化信息内容", 1, browser)
        time.sleep(2)
        # 获取第一个信息的标题
        frist_information = page.information_frist_name.text
    except:
        opteration.refresh_column_content(browser)
        frist_information = False
    assert  frist_information == "自动化信息"


@pytest.mark.dependency(depends=["test_03"])
def test_04(browser):
    """ 信息修改页面校验
        步骤：1、点击编辑按钮
            2、检查标题是否存在
            3、关闭页面
        预期：1、弹出编辑页面
            2、页面正常、标题存在
            3、页面被关闭
    """
    opteration = Column_Content(browser)
    page = Information_page(browser)
    try:
        # 打开编辑页面
        opteration.modify_information("自动化修改信息", "自动化修改信息内容", 0, browser)
        # 检查标题
        result = page.information_name.is_displayed()
        # 关闭页面
        page. modify_information_close_button.click()
    except:
        opteration.refresh_column_content(browser)
        result = False
    assert result == True


@pytest.mark.dependency(depends=["test_04"])
def test_05(browser):
    """ 信息修改校验
        步骤：1、点击编辑按钮
            2、修改标题、内容，保存
            3、检查信息标题是否正确
        预期：1、弹出编辑页面
            2、信息修改成功
            3、标题正确
    """
    opteration = Column_Content(browser)
    page = Information_page(browser)
    try:
        # 修改信息
        opteration.modify_information("自动化修改信息", "自动化修改信息内容", 1, browser)
        time.sleep(1)
        # 获取第一个信息标题
        frist_information = page.information_frist_name.text
    except:
        opteration.refresh_column_content(browser)
        frist_information = False
    assert frist_information == "自动化修改信息"


@pytest.mark.dependency(depends=["test_05"])
def test_06(browser):
    """ 信息查询校验
        步骤：1、输入信息标题查询
            2、检查信息标题是否正确
        预期：1、信息查询成功
            2、标题正确
    """
    opteration = Column_Content(browser)
    page = Information_page(browser)
    try:
        # 查询信息
        opteration.query_information("自动化修改信息")
        time.sleep(1)
        # 获取列表第一条信息的标题
        frist_information = page.information_frist_name.text
    except:
        opteration.refresh_column_content(browser)
        frist_information = False
    assert frist_information == "自动化修改信息"


@pytest.mark.dependency(depends=["test_05"])
def test_07(browser):
    """
        信息查看校验
        步骤：1、点击信息
            2、校验查看页面标题是否正确
        预期：1、弹出查看页面
            2、查看成功，标题正确
    """
    opteration = Column_Content(browser)
    page = Information_page(browser)
    try:
        # 点击信息
        page.information_frist_name.click()
        time.sleep(2)
        # 获取信息标题
        information_name = page.see_information_title.text
        # 点击信息关闭按钮
        page.see_information_close_button.click()
    except:
        opteration.refresh_column_content(browser)
        information_name = False
    assert information_name == "自动化修改信息"


@pytest.mark.dependency(depends=["test_05"])
def test_08(browser):
    """ 信息删除校验
        步骤：1、删除信息
            2、查询信息是否存在
        预期：1、信息删除成功
            2、信息不存在
    """
    opteration = Column_Content(browser)
    page = Information_page(browser)
    try:
        # 点击删除按钮
        opteration.delete_information()
        time.sleep(4)
        # 获取查询结果
        result = page.no_information_query_result.text
    except:
        opteration.refresh_column_content(browser)
        result = False
    assert result == "无搜索结果"


@pytest.mark.dependency(depends=["test_05"])
def test_09(browser):
    """ 信息批量删除校验
        步骤：1、选择信息，点击批量删除按钮
            2、删除信息
            3、查询信息是否存在
        预期：1、信息被选中
            2、信息删除成功
            3、信息不存在
    """
    opteration = Column_Content(browser)
    page = Information_page(browser)
    office_method = Office_method(browser)
    try:
        # 点击清除按钮
        page.information_eliminate_button.click()
        # 增加信息
        opteration.add_information("自动化信息", "自动化信息内容", 1, browser)
        time.sleep(1)
        # 点击批量删除按钮
        office_method.batch_delete()
        time.sleep(4)
        # 查询信息
        opteration.query_information("自动化信息")
        time.sleep(1)
        # 获取查询结果
        result = page.no_information_query_result.text
    except:
        opteration.refresh_column_content(browser)
        result = False
    assert result == "无搜索结果"


@pytest.mark.dependency(depends=["test_03"])
def test_10(browser):
    """ 选择栏目页面校验
        步骤：1、新建栏目、信息
            2、选择信息点击批量复制按钮
            3、校验选择栏目页面是否正常
        预期：1、栏目信息增加成功
            2、弹出选择栏目页面
            3、页面显示正常
    """
    opteration = Column_Content(browser)
    page = Information_page(browser)
    try:
        # 增加栏目
        opteration.add_column(browser, "移动复制栏目", "yidongfuzhi", "移动复制栏目内容")
        # 进入栏目内容
        opteration.star_column_content()
        # 增加信息
        opteration.add_information("自动化信息", "自动化信息内容", 1, browser)
        # 打开选择栏目页面
        opteration.batch_copy_information("自动化栏目", 0)
        # 保存按钮是否存在
        result = page.copy_column_choice_save_button.is_displayed()
        # 点击页面关闭按钮
        page.column_choice_close_button.click()
    except:
        opteration.refresh_column_content(browser)
        result = False
    assert result == True


@pytest.mark.dependency(depends=["test_09"])
def test_11(browser):
    """ 选择栏目页面查询校验
        步骤：1、选择信息点击批量复制按钮
            2、查询栏目
        预期：1、弹出选择栏目页面
            2、查询正常，结果正确
    """
    opteration = Column_Content(browser)
    page = Information_page(browser)
    try:
        # 点击批量复制按钮
        page.information_batch_copy_button.click()
        # 查询栏目
        opteration.column_choice_query("自动化栏目")
        time.sleep(1)
        # 获取第一个栏目名称
        column_name = page.column_choice_frist_column_name.text
        # 点击页面关闭按钮
        page.column_choice_close_button.click()
    except:
        opteration.refresh_column_content(browser)
        column_name = False
    assert column_name == "自动化栏目"


@pytest.mark.dependency(depends=["test_09"])
def test_12(browser):
    """  批量复制校验
        步骤：1、选择信息，批量复制
            2、判断复制是否成功
        预期：1、信息被复制
            2、信息复制成功
    """
    opteration = Column_Content(browser)
    page = Information_page(browser)
    try:
        # 选择信息点击批量复制按钮
        opteration.batch_copy_information("自动化栏目", 1)
        time.sleep(1)
        # 获取复制成功提示语
        success_tips = page.success_tips.text
    except:
        opteration.refresh_column_content(browser)
        success_tips = False
    assert success_tips == "已复制至草稿箱"


@pytest.mark.dependency(depends=["test_09"])
def test_13(browser):
    """ 批量移动校验
        步骤：1、新建信息
            2、选择信息，批量移动
            3、判断移动是否成功
        预期：1、弹出新建页面
            2、信息被移动
            3、移动成功
    """
    opteration = Column_Content(browser)
    page = Information_page(browser)
    try:
        # 新建信息
        opteration.add_information("自动化信息", "自动化信息内容", 1, browser)
        time.sleep(1)
        # 选择信息点击批量移动按钮
        opteration.batch_move_information("自动化栏目")
        time.sleep(1)
        # 获取移动成功提示语
        success_tips = page.success_tips.text
    except:
        opteration.refresh_column_content(browser)
        success_tips = False
    assert success_tips == "移动成功"


@pytest.mark.dependency()
def test_14(browser):
    """ 置顶校验
        步骤：1、点击置顶按钮
            2、判断置顶是否成功
        预期：1、点击成功
            2、信息置顶成功
    """
    opteration = Column_Content(browser)
    page = Information_page(browser)
    try:
        # 增加信息
        opteration.add_information("自动化信息", "自动化信息内容", 1, browser)
        time.sleep(2)
        # 点击置顶按钮
        page.information_topping_button.click()
        # 点击OK按钮
        page. information_topping_fix_button.click()
        time.sleep(1)
        # 获取置顶图标元素
        result = page.information_topping_sign.is_displayed()
    except:
        opteration.refresh_column_content(browser)
        result = False
    assert result == True


@pytest.mark.dependency()
def test_15(browser):
    """ 精华校验
        步骤：1、点击精华按钮
            2、判断精华是否成功
        预期：1、点击成功
            2、信息设置精华成功
    """
    opteration = Column_Content(browser)
    page = Information_page(browser)
    try:
        # 点击精华按钮
        page.information_essence_button.click()
        # 点击OK按钮
        page.ok_button.click()
        time.sleep(1)
        # 获取精华图标元素
        result = page.information_essence_sign.is_displayed()
    except:
        opteration.refresh_column_content(browser)
        result = False
    assert result == True


@pytest.mark.dependency(depends=["test_case/information/test_2_column_management.py::test_07"], scope='session')
@pytest.mark.dependency(depends=["test_07"])
def test_end(browser):
    """
        ======栏目内容菜单结束测试.....=======
        步骤：1、点击栏目管理
            2、删除栏目
        预期：栏目删除成功
    """
    page = Information_page(browser)
    opteration = Column_Content(browser)
    opteration_column = Column_Management(browser)
    office_method = Office_method(browser)
    # 点击栏目内容
    page.column_content.click()
    time.sleep(1)
    # 查询信息
    opteration.query_information("自动化信息")
    time.sleep(1)
    # 批量删除信息
    office_method.batch_delete()
    time.sleep(4)
    # 点击栏目管理
    page.Column_management.click()
    time.sleep(2)
    # 删除栏目
    opteration_column.delete_column(browser)
    time.sleep(1)
    # 删除栏目
    opteration_column.delete_column(browser)
    # 登出
    office_method.logout()


if __name__ == '__main__':
    pytest.main()