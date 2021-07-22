"""
created: 202009017 by yb
description: 我的发布模块用例
Modification History:
1、2020-9-17 yb创建了此文件
"""


from page.information.information_page import Information_page
from test_function.information.column_content_function import Column_Content
from test_function.information.column_management_function import Column_Management
from test_function.information.my_post_function import My_post
from test_function.office_function import Office_method
from test_function.information.drafts_function import Drafts
import pytest
import time

@pytest.mark.dependency(depends=["test_case/information/test_2_column_management.py::test_03", "information/test_3_column_content.py::test_03"],
                        scope='session')
@pytest.mark.dependency()
def test_init(browser):
    """
    ======我的发布菜单开始测试.....=======
        步骤：1、登录系统，点击信息、栏目管理
            2、增加栏目和信息
    """
    opteration = My_post(browser)
    opteration.add_my_information(browser, 1)


@pytest.mark.dependency(["test_init"])
def test_01(browser):
    """我的发布列表校验
        步骤：1、点击我的内容、我的发布
            2、判断发布的信息是否存在
        预期：1、进入我的发布列表
            2、新建信息存在
    """
    page = Information_page(browser)
    opteration = My_post(browser)
    try:
        # 进入我的发布
        opteration.star_my_post()
        time.sleep(1)
        # 获取第一条信息标题
        information_name = page.my_information_frist_name.text
    except:
        opteration.refresh_my_post(browser)
        information_name = False
    assert information_name == "自动化信息"


@pytest.mark.dependency(["test_init"])
def test_02(browser):
    """我的发布列表查询校验
        步骤：1、输入信息标题查询
            2、验证查询是否正确
        预期：1、查询成功
            2、查询结果正确
    """
    page = Information_page(browser)
    opteration = Column_Content(browser)
    opteration_mypost = My_post(browser)
    try:
        # 查询信息
        opteration.query_information("自动化信息")
        time.sleep(1)
        # 获取第一条信息标题
        information_name = page.my_information_frist_name.text
    except:
        opteration_mypost.refresh_my_post(browser)
        information_name = False
    assert information_name == "自动化信息"


@pytest.mark.dependency(["test_init"])
def test_03(browser):
    """修改信息校验
        步骤：1、输入信息标题查询
            2、点击修改按钮
            3、标题元素是否存在
        预期：1、查询成功
            2、弹出修改页面
            3、标题元素存在
    """
    page = Information_page(browser)
    opteration = Column_Content(browser)
    opteration_mypost = My_post(browser)
    try:
        opteration.modify_information("修改自动化信息", "复制信息内容", 0, browser)
        result = page.information_name.is_displayed()
        # 关闭页面
        page. modify_information_close_button.click()
    except:
        opteration_mypost.refresh_my_post(browser)
        result = False
    assert result == True


@pytest.mark.dependency(["test_init"])
def test_04(browser):
    """修改信息校验
        步骤：1、输入信息标题查询
            2、修改信息
            3、验证查询是否正确
        预期：1、查询成功
            2、修改成功
            3、查询结果正确
    """
    page = Information_page(browser)
    opteration = Column_Content(browser)
    opteration_mypost = My_post(browser)
    try:
        opteration.modify_information("修改自动化信息", "复制信息内容", 1, browser)
        # 查询信息
        opteration.query_information("修改自动化信息")
        time.sleep(1)
        # 获取第一条信息标题
        information_name = page.my_information_frist_name.text
    except:
        opteration_mypost.refresh_my_post(browser)
        information_name = False
    assert information_name == "修改自动化信息"


@pytest.mark.dependency(["test_03"])
def test_05(browser):
    """
        信息查看校验
        步骤：1、点击信息
            2、校验查看页面标题是否正确
        预期：1、弹出信息查看页面
            2、查看正确
    """
    page = Information_page(browser)
    opteration_mypost = My_post(browser)
    try:
        # 点击信息标题
        page.my_information_frist_name.click()
        time.sleep(2)
        # 获取信息标题
        information_name = page.see_information_title.text
        # 点击信息关闭按钮
        page.see_information_close_button.click()
    except:
        opteration_mypost.refresh_my_post(browser)
        information_name = False
    assert information_name == "修改自动化信息"


@pytest.mark.dependency(["test_init"])
def test_06(browser):
    """ 信息删除校验
        步骤：1、删除信息
            2、查询信息是否存在
        预期：1、信息删除成功
            2、信息不存在
    """
    page = Information_page(browser)
    opteration_mypost = My_post(browser)
    try:
        # 删除信息
        opteration_mypost.delete_information()
        time.sleep(4)
        # 获取查询结果
        result = page.no_information_query_result.text
    except:
        opteration_mypost.refresh_my_post(browser)
        result = False
    assert result == "无搜索结果"


@pytest.mark.dependency(depends=["test_case/information/test_3_column_content.py::test_03"], scope='session')
@pytest.mark.dependency()
def test_07(browser):
    """ 同步信息校验
        步骤：1、新建信息
            2、选择信息，点击同步按钮
            3、判断同步是否成功
        预期：1、新建信息成功
            2、信息被同步
            3、同步成功
    """
    page = Information_page(browser)
    opteration_mypost = My_post(browser)
    try:
        # 新建信息
        opteration_mypost.add_my_information(browser, 0)
        time.sleep(1)
        # 同步信息
        opteration_mypost.synchronization_information("自动化栏目")
        time.sleep(1)
        # 获取同步成功提示语
        success_tips = page.success_tips.text
    except:
        opteration_mypost.refresh_my_post(browser)
        success_tips = False
    assert success_tips == "同步成功"


@pytest.mark.dependency(["test_06"])
def test_08(browser):
    """ 复制信息校验
        步骤：1、选择信息，点击复制按钮
            2、判断复制是否成功
        预期：1、信息被复制
            2、复制成功
    """
    page = Information_page(browser)
    opteration_mypost = My_post(browser)
    try:
        # 复制信息
        opteration_mypost.copy_information("自动化栏目")
        time.sleep(1)
        # 获取复制成功提示语
        success_tips = page.success_tips.text
    except:
        opteration_mypost.refresh_my_post(browser)
        success_tips = False
    assert success_tips == "已复制至草稿箱"


@pytest.mark.dependency(["test_06"])
def test_09(browser):
    """ 移动信息校验
        步骤：1、选择信息，点击移动按钮
            2、判断复移动是否成功
        预期：1、信息被移动
            2、移动成功
    """
    page = Information_page(browser)
    opteration_mypost = My_post(browser)
    try:
        # 同步信息
        opteration_mypost.move_information("移动栏目")
        time.sleep(1)
        # 获取移动成功提示语
        success_tips = page.success_tips.text
    except:
        opteration_mypost.refresh_my_post(browser)
        success_tips = False
    assert success_tips == "移动成功"


@pytest.mark.dependency(depends=["test_case/information/test_3_column_content.py::test_03"], scope='session')
@pytest.mark.dependency()
def test_10(browser):
    """  批量复制校验
        步骤：1、新建信息，批量复制
            2、判断复制是否成功
        预期：1、信息被复制
            2、信息复制成功
    """
    page = Information_page(browser)
    opteration_mypost = My_post(browser)
    try:
        # 新建信息
        opteration_mypost.add_my_information(browser, 0)
        time.sleep(1)
        # 选择信息点击批量复制按钮
        opteration_mypost.batch_copy_information("自动化栏目")
        time.sleep(1)
        # 获取复制成功提示语
        success_tips = page.success_tips.text
    except:
        opteration_mypost.refresh_my_post(browser)
        success_tips = False
    assert success_tips == "已复制至草稿箱"


@pytest.mark.dependency(depends=["test_case/information/test_3_column_content.py::test_03"], scope='session')
@pytest.mark.dependency()
def test_11(browser):
    """  批量移动校验
        步骤：1、新建信息，批量移动
            2、判断移动是否成功
        预期：1、信息被移动
            2、信息移动成功
    """
    page = Information_page(browser)
    opteration_mypost = My_post(browser)
    try:
        # 新建信息
        opteration_mypost.add_my_information(browser, 0)
        time.sleep(1)
        # 选择信息点击批量移动按钮
        opteration_mypost.batch_move_information("自动化栏目")
        time.sleep(1)
        # 获取移动成功提示语
        success_tips = page.success_tips.text
    except:
        opteration_mypost.refresh_my_post(browser)
        success_tips = False
    assert success_tips == "移动成功"


@pytest.mark.dependency()
def test_12(browser):
    """ 信息批量删除校验
        步骤：1、选择信息，点击批量删除按钮
            2、删除信息
            3、查询信息是否存在
        预期：1、信息被选中删除
            2、信息删除成功
            3、信息不存在
    """
    opteration = Column_Content(browser)
    opteration_mypost = My_post(browser)
    page = Information_page(browser)
    office_method = Office_method(browser)
    try:
        # 查询信息
        opteration.query_information("自动化信息")
        # 点击批量删除按钮
        office_method.batch_delete()
        time.sleep(2)
        # 获取查询结果
        result = page.no_information_query_result.text
    except:
        opteration_mypost.refresh_my_post(browser)
        result = False
    assert result == "无搜索结果"


@pytest.mark.dependency(depends=["test_case/information/test_2_column_management.py::test_07"], scope='session')
@pytest.mark.dependency()
def test_end(browser):
    """
        ======我的发布菜单结束测试.....=======
        步骤：1、删除草稿箱信息
            2、删除栏目
        预期：删除成功
    """
    page = Information_page(browser)
    opteration = Column_Content(browser)
    opteration_column = Column_Management(browser)
    office_method = Office_method(browser)
    opteration_drafts = Drafts(browser)
    # 进入草稿箱
    opteration_drafts.star_drafts()
    # 查询信息
    opteration.query_information("自动化")
    # 批量删除
    office_method.batch_delete()
    time.sleep(4)
    # 点击栏目管理
    page.Column_management.click()
    # 删除栏目
    opteration_column.delete_column(browser)
    time.sleep(1)
    # 删除栏目
    opteration_column.delete_column(browser)
    # 登出
    office_method.logout()


if __name__ == '__main__':
    pytest.main()