import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
url = 'https://the-internet.herokuapp.com/checkboxes'
driver.get(url)

element = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/form/input')
driver.execute_script("arguments[0].click();", element)
print('js点击成功')
time.sleep(5)

# # driver.find_element(By.XPATH,'/html/body/div[2]/div/div/form/input').click()
# print('普通点击成功')
# # time.sleep(3)