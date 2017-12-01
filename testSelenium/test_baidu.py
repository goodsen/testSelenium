from selenium import webdriver
import unittest,re,time
import HTMLTestRunner

class Baidu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.base_url = "http://www.baidu.com"
    def test_baidu_search(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("Kw").send_keys("HTMLTestRunner")
        driver.find_element_by_id("su").click()
        time.sleep(2)
        driver.close()
    def tearDown(self):
        self.driver.quit()
if __name__ == "__main__":
    testunit = unittest.TestSuite()
    testunit.addTest(Baidu("test_baidu_search"))


    #定义报告存放路径
    fp = open(r'E:\py3','wb')
    #file_result = open(file_path ,'wb')

    #定义测试报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title="百度搜索测试报告",description ="用例执行情况")

    runner.run(testunit)#运行测试用例
    fp.close()#关闭报告文件