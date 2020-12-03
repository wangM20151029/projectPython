from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
from pages.LoginPage import LoginPage

driver = webdriver.Chrome()
driver.get("http://test.sobot.com/console/login")
loginPage = LoginPage()
loginPage.__init__(driver)
loginPage.login("wangmin_test@sobot.com","123456sobot")