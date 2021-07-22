import unittest
data={
            'user':'111',
            'psw':'222'
        }
class  Test_01(unittest.TestCase):
    def setUp(self):
        print('开始1')

    def tearDown(self):
        print('结束1')

    def test_01(self):
        data1={
            'user':'111',
            'psw':'222'
        }
        self.assertEqual(data,data1)
if __name__ == '__main__':
    suit=unittest.TestSuite()
    suit.addTest(Test_01('test_01'))
    runner=unittest.TextTestRunner()
    runner.run(suit)
