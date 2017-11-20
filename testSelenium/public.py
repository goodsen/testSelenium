class login():
    #登录
    def user_logIn(self,driver):
        driver.find_element_by_id("shortAccount").clear()
        driver.find_element_by_id("shortAccount").send_keys(username)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(password)
        driver.find_element_by_xpath(".//*[@id='loginForm']/div[6]/input").click()
    #退出
    def user_logOut(self,driver):
        driver.find_element_by_id("login").click()
        driver.quit()
