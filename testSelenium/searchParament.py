from selenium import webdriver

search_text = ['python','中文','text']
for text in search_text:
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.get("http://casicloud.com/search?q=")
    driver.find_element_by_xpath(".//*[@id='keyword']").send_keys(text)
    driver.find_element_by_xpath("html/body/div[2]/div[2]/div/div[2]/a").click()
    driver.quit()