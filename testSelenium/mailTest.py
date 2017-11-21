from selenium import webdriver
from testSelenium.public import login#public是登录、退出的脚本

class loginTest():
    #主方法更改
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.get("http://cas.casicloud.com/login?service=http%3A%2F%2F"
                        "in.casicloud.com%2Floginc%3Fservice%3D%252Fsso%252F"
                        "login.jsp%253Fredirect%253Dhttp%25253A%25252F%25252F"
                        "172.17.60.214%25252Floginc%25253Fret%25253D"
                        "http%2525253A%2525252F%2525252F172.17.60.214%2525252F")
    #主账号用户登录
    def test__admin__login(self):
        username = '18618411965'
        password = '123456789'
        login().user_logIn(self.driver,username,password)
        self.driver.quit()
    #小号登录
    def test__guest__login(self):
        username = '15311480674'
        password = '123456'
        login.user_logIn(self.driver,username,password)
        self.driver.quit()
loginTest().test__admin__login()

