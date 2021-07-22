"""
created: 202009028 by yb
description: 信息统计模块用例
Modification History:
1、2020-9-28 yb创建了此文件
"""


from page.information.information_page import Information_page
from test_function.information.column_management_function import Column_Management
from test_function.information.information_statistics import Information_Statistics
from test_function.office_function import Office_method
import pytest
import time


@pytest.mark.dependency()
def test_01(browser):
    """
    ======信息统计菜单开始测试.....=======
    发布量统计页面校验
        步骤：1、登录系统，点击信息、信息统计
            2、页面元素校验
        预期：
            1、进入信息统计列表
            2、页面元素存在
    """
    opteration = Information_Statistics(browser)
    page = Information_page(browser)
    try:
        # 进入信息统计页面
        opteration.star_information_statistics(browser)
        result = page.release_query_open_button.is_displayed()
    except:
        opteration.refresh_information_statistics(browser)
        result = False
    assert result == True


@pytest.mark.dependency(depends=["test_case/information/test_2_column_management.py::test_03", "information/test_3_column_content.py::test_03"],
                        scope='session')
@pytest.mark.dependency(["test_01"])
def test_02(browser):
    """
    发布量统计查询校验
        步骤：1、查询发布人
            2、验证查询是否正确
        预期：
            1、查询成功
            2、查询结果正确
    """
    opteration = Information_Statistics(browser)
    page = Information_page(browser)
    # 登录人姓名
    login_name = page.login_name.text
    try:
        # 增加栏目和信息
        opteration.add_colunm_information(browser, 1)
        # 点击信息统计菜单
        page.information_statistics.click()
        # 发布人查询
        opteration.query_publisher(login_name, page.statistics_publish_publisher_query, page.release_query_button)
        time.sleep(1)
        # 获取第一条数据发布人名称
        name = page.publish_first_publisher_name.text
    except:
        opteration.refresh_information_statistics(browser)
        name = False
    assert name == login_name


@pytest.mark.dependency(depends=["test_case/information/test_3_column_content.py::test_03"], scope='session')
@pytest.mark.dependency(["test_02"])
def test_03(browser):
    """
    发布量统计量准确校验
        步骤：1、获取发布量
            2、发布信息
            3、发布量是否加一
        预期：
            1、获取成功
            2、发布完成
            3、发布量正确
    """
    opteration = Information_Statistics(browser)
    page = Information_page(browser)
    try:
        # 获取发布量
        release = page.publish_release.text
        # 增加信息
        opteration.add_colunm_information(browser, 0)
        # 点击信息统计菜单
        page.information_statistics.click()
        # 登录人姓名
        login_name = page.login_name.text
        # 查询发布人
        opteration.query_publisher(login_name, page.statistics_publish_publisher_query, page.release_query_button)
        time.sleep(1)
        # 获取发布量
        new_release = page.publish_release.text
        # 判断元素是否+1
        if int(new_release) == int(release) + 1:
            result = True
        else:
            result = False
    except:
        opteration.refresh_information_statistics(browser)
        result = False
    assert result == True


@pytest.mark.dependency()
def test_04(browser):
    """
    精华统计页面校验
        步骤：1、点击精华量统计页签
            2、获取页面元素
        预期：
            1、进入精华量统计页面
            2、获取元素成功
    """
    opteration = Information_Statistics(browser)
    page = Information_page(browser)
    try:
        # 点击精华量统计页签
        page.essence_statistics.click()
        result = page.essence_query_open_button.is_displayed()
    except:
        opteration.refresh_information_statistics(browser)
        result = False
    assert result == True


@pytest.mark.dependency(depends=["test_case/information/test_3_column_content.py::test_15"], scope='session')
@pytest.mark.dependency(["test_04"])
def test_05(browser):
    """
    精华统计页面查询校验
        步骤：1、查询发布人
            2、验证查询是否正确
        预期：
            1、查询成功
            2、查询结果正确
    """
    opteration = Information_Statistics(browser)
    page = Information_page(browser)
    # 登录人姓名
    login_name = page.login_name.text
    try:
        # 精华信息
        opteration.essence_information("自动化信息")
        # 点击信息统计菜单
        page.information_statistics.click()
        # 点击精华量统计页签
        page.essence_statistics.click()
        # 发布人查询
        opteration.query_publisher(login_name, page.statistics_essence_publisher_query, page.essence_query_button)
        time.sleep(1)
        # 获取第一条数据发布人名称
        name = page.essence_first_publisher_name.text
    except:
        opteration.refresh_information_statistics(browser)
        name = False
    assert name == login_name


@pytest.mark.dependency(depends=["test_case/information/test_3_column_content.py::test_15"], scope='session')
@pytest.mark.dependency(["test_01"])
def test_06(browser):
    """
    精华统计量准确校验
        步骤：1、获取精华量
            2、精华信息
            3、精华量是否加一
        预期：
            1、获取成功
            2、精华成功
            3、精华量正确
    """
    opteration = Information_Statistics(browser)
    page = Information_page(browser)
    try:
        # 获取精华量
        release = page.essence_release.text
        # 精华信息
        opteration.essence_information("精华信息")
        # 点击信息统计菜单
        page.information_statistics.click()
        # 点击精华量统计页签
        page.essence_statistics.click()
        # 登录人姓名
        login_name = page.login_name.text
        # 查询发布人
        opteration.query_publisher(login_name, page.statistics_essence_publisher_query, page.essence_query_button)
        time.sleep(1)
        # 获取精华量
        new_release = page.essence_release.text
        # 判断元素是否+1
        if int(new_release) == int(release) + 1:
            result = True
        else:
            result = False
    except:
        opteration.refresh_information_statistics(browser)
        result = False
    assert result == True


@pytest.mark.dependency(depends=["test_case/information/test_2_column_management.py::test_07"], scope='session')
@pytest.mark.dependency(["test_01"])
def test_end(browser):
    """
    ======信息统计菜单结束测试.....=======
            步骤：删除信息和栏目
    """
    opteration_column = Column_Management(browser)
    office_method = Office_method(browser)
    page = Information_page(browser)
    # 点击信息
    page.information.click()
    # 点击栏目树第一个栏目
    page.information_frist_column.click()
    time.sleep(1)
    # 批量删除
    office_method.batch_delete()
    time.sleep(4)
    # 点击栏目管理
    page.Column_management.click()
    time.sleep(2)
    # 删除栏目
    opteration_column.delete_column(browser)
    time.sleep(1)
    # 登出
    office_method.logout()


if __name__ == '__main__':
    pytest.main()