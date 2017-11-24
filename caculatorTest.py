from caculator import Count
import unittest
#测试两个整数相加
class TestCount(unittest.TestCase):
    #定义启动
    def setUp(self):
        print("test start")
    #定义单元测试
    def test__add(self):
        j = Count(2,3)
        self.assertEqual(j.add(),5)#增加断言方法
    def tearDown(self):
        print("test end")
if __name__ == '__main__':
    unittest.main()

