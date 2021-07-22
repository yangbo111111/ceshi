"""
created: 202009010 by yb
description: 草稿箱模块用例
Modification History:
1、2020-9-10 yb创建了此文件
"""
from page.information.information_page import Information_page
from test_function.information.column_content_function import Column_Content
from test_function.information.column_management_function import Column_Management
from test_function.information.drafts_function import Drafts
from test_function.office_function import Office_method
import pytest
import time

@pytest.mark.dependency(depends=["test_case/information/test_2_column_management.py::test_03", "information/test_3_column_content.py::test_12"],
                        scope='session')
@pytest.mark.dependency()
def test_init(browser):
    """
    ======草稿箱菜单开始测试.....=======
        步骤：1、登录系统，点击信息、栏目管理
            2、增加栏目、复制信息
    """
    opteration_drafts = Drafts(browser)
    opteration_drafts.add_drafts_information(browser, 1)


@pytest.mark.dependency(["test_init"])
def test_01(browser):
    """草稿箱列表校验
        步骤：1、点击我的内容、草稿箱
            2、判断复制信息是否存在
        预期：1、进入草稿箱列表
            2、复制信息存在
    """
    page = Information_page(browser)
    opteration = Drafts(browser)
    try:
        # 进入草稿箱
        opteration.star_drafts()
        time.sleep(1)
        # 获取第一条信息标题
        information_name = page.my_information_frist_name.text
    except:
        opteration.refresh_drafts(browser)
        information_name = False
    assert information_name == "【复制】自动化信息"


@pytest.mark.dependency(["test_init"])
def test_02(browser):
    """草稿箱列表查询校验
        步骤：1、输入信息标题查询
            2、验证查询是否正确
        预期：1、查询成功
            2、查询结果正确
    """
    page = Information_page(browser)
    opteration = Column_Content(browser)
    opteration_drafts = Drafts(browser)
    try:
        # 查询信息
        opteration.query_information("【复制】自动化信息")
        time.sleep(1)
        # 获取第一条信息标题
        information_name = page.my_information_frist_name.text
    except:
        opteration_drafts.refresh_drafts(browser)
        information_name = False
    assert information_name == "【复制】自动化信息"


@pytest.mark.dependency(["test_02"])
def test_03(browser):
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
    opteration_drafts = Drafts(browser)
    try:
        opteration_drafts.modify_information("修改自动化信息", "复制信息内容", 1, browser)
        # 查询信息
        opteration.query_information("修改自动化信息")
        time.sleep(2)
        # 获取第一条信息标题
        information_name = page.my_information_frist_name.text
    except:
        opteration_drafts.refresh_drafts(browser)
        information_name = False
    assert information_name == "修改自动化信息"


@pytest.mark.dependency(["test_03"])
def test_04(browser):
    """
        信息查看校验
        步骤：1、点击信息
            2、校验查看页面标题是否正确
        预期：1、弹出信息查看页面
            2、查看正确
    """
    page = Information_page(browser)
    opteration_drafts = Drafts(browser)
    try:
        # 点击信息标题
        page.my_information_frist_name.click()
        time.sleep(1)
        # 获取信息标题
        information_name = page.see_information_title.text
        # 点击信息关闭按钮
        page.see_information_close_button.click()
    except:
        opteration_drafts.refresh_drafts(browser)
        information_name = False
    assert information_name == "修改自动化信息"


@pytest.mark.dependency(["test_04"])
def test_05(browser):
    """ 信息删除校验
        步骤：1、删除信息
            2、查询信息是否存在
        预期：1、信息删除成功
            2、信息不存在
    """
    page = Information_page(browser)
    opteration_drafts = Drafts(browser)
    try:
        # 删除信息
        opteration_drafts.delete_information()
        time.sleep(4)
        # 获取查询结果
        result = page.no_information_query_result.text
    except:
        opteration_drafts.refresh_drafts(browser)
        result = False
    assert result == "无搜索结果"


@pytest.mark.dependency()
def test_06(browser):
    """ 信息批量删除校验
        步骤：1、选择信息，点击批量删除按钮
            2、删除信息
            3、查询信息是否存在
        预期：1、信息被选中删除
            2、信息删除成功
            3、信息不存在
    """
    opteration = Column_Content(browser)
    opteration_drafts = Drafts(browser)
    page = Information_page(browser)
    office_method = Office_method(browser)
    try:
        # 复制信息
        opteration_drafts.add_drafts_information(browser, 0)
        opteration_drafts.star_drafts()
        time.sleep(1)
        opteration.query_information("【复制】自动化信息")
        # 点击批量删除按钮
        office_method.batch_delete()
        time.sleep(2)
        # 获取查询结果
        result = page.no_information_query_result.text
    except:
        opteration_drafts.refresh_drafts(browser)
        result = False
    assert result == "无搜索结果"


@pytest.mark.dependency(depends=["test_case/information/test_3_column_content.py::test_12"], scope='session')
@pytest.mark.dependency()
def test_07(browser):
    """ 草稿信息发布校验
        步骤：1、复制信息
            2、发布复制信息
        预期：1、信息复制成功
            2、信息发布成功
    """
    opteration_drafts = Drafts(browser)
    page = Information_page(browser)
    try:
        # 复制信息
        opteration_drafts.add_drafts_information(browser, 0)
        # 进入草稿箱
        opteration_drafts.star_drafts()
        # 点击发布按钮
        page.drafts_release_button.click()
        # 点击确定按钮
        page.ok_button.click()
        # 获取成功提示语
        tips = page.success_tips.text
    except:
        opteration_drafts.refresh_drafts(browser)
        tips = False
    assert tips == "发布成功"


@pytest.mark.dependency(depends=["test_case/information/test_3_column_content.py::test_12"], scope='session')
@pytest.mark.dependency()
def test_08(browser):
    """ 草稿信息发布校验
        步骤：1、复制信息
            2、批量发布发布复制信息
        预期：1、信息复制成功
            2、信息批量发布成功
    """
    opteration = Column_Content(browser)
    opteration_drafts = Drafts(browser)
    page = Information_page(browser)
    try:
        # 复制信息
        opteration_drafts.add_drafts_information(browser, 0)
        # 进入草稿箱
        opteration_drafts.star_drafts()
        # 查询信息
        opteration.query_information("【复制】自动化信息")
        # 批量发布信息
        opteration_drafts.batch_release()
        # 获取成功提示语
        tips = page.success_tips.text
    except:
        opteration.refresh_column_content(browser)
        tips = False
    assert tips == "发布成功"


@pytest.mark.dependency(depends=["test_case/information/test_2_column_management.py::test_07"], scope='session')
@pytest.mark.dependency()
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
    # 删除栏目
    opteration_column.delete_column(browser)
    time.sleep(1)
    # 删除栏目
    opteration_column.delete_column(browser)
    # 登出
    office_method.logout()


if __name__ == '__main__':
    pytest.main()