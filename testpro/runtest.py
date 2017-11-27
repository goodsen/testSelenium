import  unittest

#加载测试文件
import testpro.testadd
import testpro.testsub

#构造测试集
suite = unittest.TestSuite()
suite.addTest(testpro.testadd("test_add"))
suite.addTest(testpro.testsub("test_add2"))

suite.addTest(testpro.testsub("test_add"))
suite.addTest(testpro.testsub("test_add2"))

if __name__ == '__main__':
    #执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)