from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time

driver = webdriver.Chrome()
driver.get("http://test.sobot.com/console/login")
userName = driver.find_element_by_id("userEmail")
pwd = driver.find_element_by_id("userPassword")
loginOk = driver.find_element_by_class_name("reg_submit")

time.sleep(2)

userName.send_keys("wangmin_test@sobot.com")
pwd.send_keys("123456sobot")

loginOk.click()
time.sleep(2)

try:
    WebDriverWait(driver, 10).until(lambda driver: driver.title.lower().startswith("cheese!"))
    print(driver.title)
finally:
    driver.quit()
