from selenium import webdriver
from testSelenium.public import login#public是登录、退出的脚本

'''
driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("http://cas.casicloud.com/login?service=http%3A%2F%2F"
           "in.casicloud.com%2Floginc%3Fservice%3D%252Fsso%252F"
           "login.jsp%253Fredirect%253Dhttp%25253A%25252F%25252F"
           "172.17.60.214%25252Floginc%25253Fret%25253D"
           "http%2525253A%2525252F%2525252F172.17.60.214%2525252F")
#调用登录模块
login().user_logIn(driver)

#调用退出模块
login().user_logOut(driver)
'''
class loginTest():
    #主方法
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.get("http://cas.casicloud.com/login?service=http%3A%2F%2F"
                        "in.casicloud.com%2Floginc%3Fservice%3D%252Fsso%252F"
                        "login.jsp%253Fredirect%253Dhttp%25253A%25252F%25252F"
                        "172.17.60.214%25252Floginc%25253Fret%25253D"
                        "http%2525253A%2525252F%2525252F172.17.60.214%2525252F")
    #用户登录
    def test_admin_login(self):
        username = '18618411965'
        password = '123456'

