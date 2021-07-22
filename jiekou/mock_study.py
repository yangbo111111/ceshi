import mock
import requests
import unittest
url = 'http://www.imooc.com/login'
data = {
    'username':'111111',
    'password':'222222'
}
def post_request(url,data):
    res= requests.post(url=url,data=data).json()
    return res
def get_request(url,data):
    res=requests.get(url,params=data)
    return res
class TestLogin(unittest.TestCase):
    def setUp(self):
        print("开始")
    def tearDown(self):
        print('结束')

    def test_01(self):
        url='http://www.imooc.com/login/register'
        data = {
            'username': '111111',
            'password': '222222'
        }
        sucess_test=mock.Mock(return_value=data)
        post_request=sucess_test
        res=post_request
        self.assertEqual('666666',res())
if __name__ == '__main__':
    unittest.main()
