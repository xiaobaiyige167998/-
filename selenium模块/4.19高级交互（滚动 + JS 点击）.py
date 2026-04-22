from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()
url = 'https://the-internet.herokuapp.com/infinite_scroll'
driver.get(url)
for i in range(3):
    driver.execute_script("window.scrollto(0, document.body.scrollHeight);")
    time.sleep(2)

print("已完成滚动")