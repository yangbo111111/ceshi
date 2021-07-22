import unittest
data={
            'user':'111',
            'psw':'222'
        }
class  Test_03(unittest.TestCase):
    def setUp(self):
        print('开始3')

    def tearDown(self):
        print('结束3')

    def test_01(self):
        data1={
            'user':'111',
            'psw':'222'
        }
        self.assertEqual(data,data1)

