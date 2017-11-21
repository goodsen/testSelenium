class login():
    #登录,修改接口需要驱动、用户名和密码等参数
    def user_logIn(self,driver,username,password):
        driver.find_element_by_id("shortAccount").clear()
        driver.find_element_by_id("shortAccount").send_keys(username)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(password)
        driver.find_element_by_xpath(".//*[@id='loginForm']/div[6]/input").click()
    #退出
    def user_logOut(self,driver):
        driver.find_element_by_id("login").click()
        driver.quit()
