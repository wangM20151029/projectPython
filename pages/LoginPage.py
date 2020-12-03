from selenium.webdriver.common.by import By
from selenium import webdriver
import time

class LoginPage():

    def __init__(self,driver):
        self.driver = driver

    def login(self,email,pwd):
        self.driver.find_element_by_id("userEmail").send_keys(email)
        self.driver.find_element_by_id("userPassword").send_keys(pwd)
        self.driver.find_element_by_class_name("reg_submit").click()

        time.sleep(2)
        res = self.driver.find_element_by_css_selector(".zc-menu>div.ng-binding").text
        #print("首页res：======"+res)
        assert "首页" == res

if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.get("http://test.sobot.com/console/login")
    LoginPage(driver).login("wangmin_test@sobot.com","123456sobot")