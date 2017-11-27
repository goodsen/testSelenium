from caculator import Count
import unittest

#定义加法单元测试类
class TestSub(unittest.TestCase):
    def setUp(self):
        print("测试用例开始")
    def tearDown(self):
        print("测试用例结束")
    def test_sub(self):
        j = Count(2,3)
        self.assertEqual(j.add(),5)
    def test_sub2(self):
        j = Count(2,3)
        self.assertEqual(j.sub(),-1)
if __name__ == '__main__':
    unittest.main()