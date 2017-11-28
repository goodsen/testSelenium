import unittest

#设置用例启动方法
def setUpModule():
    print("test module start >>>>>>>>>>>>>")
#设置用例结束方法
def tearDownModule():
    print("test module end   >>>>>>>>>>>>>")
#Test单元测试类
class Test(unittest.TestSuite):
    @classmethod
    def setUpClass(cls):
        print("test class start======>")
    @classmethod
    def tearDownClass(cls):
        print("test class end =======>")
    def setUp(self):
        print("test case start-->")
    def tearDown(self):
        print("test case end  -->")
    def test_case(self):
        print("test case1")
    def test_case2(self):
        print("test case2")
if __name__ == '__main__':
    unittest.main()