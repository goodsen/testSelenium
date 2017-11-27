from caculator import Count
import unittest

class TestAdd(unittest.TestCase):
    def setUp(self):
        print("test add start")
    def test_add(self):
        j = Count(2,3)
        self.assertEqual(j.add(),5)
    def test_add2(self):
        j = Count(41,76)
        self.assertEqual(j.add(),117)
    def tearDown(self):
        print("测试结束，没有错误")