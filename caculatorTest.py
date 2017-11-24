from caculator import Count
import unittest
#测试两个整数相加
class TestCount(unittest.TestCase):
    #定义启动项
    def setUp(self):
        print("test start")
    #定义测试用例1
    def test__add(self):
        j = Count(2,3)
        self.assertEqual(j.add(),5)#增加断言方法
    #定义测试用例2
    def test_add2(self):
        j = Count(41,76)
        self.assertAlmostEquals(j.add(),117)
    def tearDown(self):
        print("test end")
if __name__ == '__main__':
    # 构建测试集
    suite = unittest.TestSuite()
    suite.addTest(TestCount("test_add2"))
    #执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)


