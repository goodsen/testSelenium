from caculator import Count
import unittest

class MyTest(unittest.TestCase):
    def setUp(self):
        print("测试开始")
    def tearDown(self):
        print("测试结束")

class TestAdd(MyTest):
    def test_add(self):
        j = Count(2,3)
        self.assertEqual(j.add(),5)
    def test_add2(self):
        j = Count(41,76)
        self.assertEqual(j.add(),117)
class TestSub(MyTest):
    def test_sub(self):
        j = Count(2,3)
        self.assertEqual(j.sub(),-1)
    def test_sub2(self):
        j = Count(71,46)
        self.assertEqual(j.sub(),25)
if __name__ == '__main__':
    unittest.main()
