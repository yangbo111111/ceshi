import unittest
import os
# from UnittetCase_test.test_case01 import Test_01
# from UnittetCase_test.testcase_02 import Test_02
# from UnittetCase_test.testcase_03 import Test_03
# case_01=unittest.TestLoader().loadTestsFromTestCase(Test_01)
# case_02=unittest.TestLoader().loadTestsFromTestCase(Test_02)
# case_03=unittest.TestLoader().loadTestsFromTestCase(Test_03 )
# suote=unittest.TestSuite([case_01,case_02,case_03])
# unittest.TextTestRunner().run(suote)
case_path=os.getcwd()
discover=unittest.defaultTestLoader.discover(case_path)
unittest.TextTestRunner().run(discover)