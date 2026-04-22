from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 第一种写法
driver = webdriver.Edge()
url = 'file:///C:/Users/HP/Desktop/test_page.html'
driver.get(url)
admin = driver.find_element(By.XPATH,'/html/body/input[1]')
admin.clear()
admin.send_keys('admin')
password = driver.find_element(By.XPATH,'/html/body/input[2]')
password.click()
password.send_keys('123456')
time.sleep(2)
password.clear()
time.sleep(2)
driver.find_element(By.XPATH,'/html/body/button').click()
time.sleep(5)