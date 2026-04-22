import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
url = 'file:///C:/Users/HP/Desktop/test_page.html'
driver.get(url)

# 切换进入iframe
driver.switch_to.frame('myframe')

# 点击按钮
driver.find_element(By.XPATH, '/html/body/button').click()

# 获取点击按钮后的文本
text = driver.find_element(By.ID,'frame-text').text
print(text)

# 切换回主页面
driver.switch_to.default_content()
time.sleep(5)
