from caculator import Count
import unittest

#定义加法单元测试类
class TestAdd(unittest.TestCase):
    def setUp(self):
        print("测试用例开始")
    def tearDown(self):
        print("测试用例结束")
    def test_add(self):
        j = Count(2,3)
        self.assertEqual(j.add(),5)
    def test_add2(self):
        j = Count(41,76)
        self.assertEqual(j.add(),117)
if __name__ == '__main__':
    unittest.main()