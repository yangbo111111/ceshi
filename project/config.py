

class RunConfig:
    """
    运行测试配置
    """
    # 运行测试用例的目录或文件
    cases_path = "./test_case/"

    # 配置浏览器驱动类型(chrome/firefox/chrome-headless/firefox-headless)。
    driver_type = "chrome"

    # 配置运行的 URL
    url = "http://192.168.0.120:8000/flexoffice/web/dist/modules/login/login.html"
    # url = "http://192.168.7.55:7410/defaultroot/"


    # 失败重跑次数
    rerun = "1"

    # 当达到最大失败数，停止执行
    max_fail = "5"


