#coding = utf -8
from selenium import webdriver
import unittest,time
import HTMLTestRunner

#定义百度测试类
class Baidu(unittest.TestCase):
    #启动方法（配置浏览器、url、隐藏等待时间）
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.base_url = "http://www.baidu.com"
    #定义搜索方法
    def test_baidu_search(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("kw").send_keys("HTMLTestRunner")
        driver.find_element_by_id("su").click()
        time.sleep(2)
        driver.close()
    #方法结束
    def tearDown(self):
        self.driver.quit()
#主方法执行测试用例集
if __name__ == "__main__":
    testunit = unittest.TestSuite()
    testunit.addTest(Baidu("test_baidu_search"))


    #定义报告存放路径
    fp = "E:\\result.html"
    fp_result = open(fp ,"wb")

    #定义测试报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp_result,title="百度搜索测试报告",description ="用例执行情况")

    runner.run(testunit)#运行测试用例
    fp_result.close()#关闭报告文件