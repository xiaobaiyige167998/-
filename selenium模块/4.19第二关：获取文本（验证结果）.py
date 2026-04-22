from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Edge()
url = 'file:///C:/Users/HP/Desktop/test_page.html'
driver.get(url)

# 填写账号
driver.find_element(By.XPATH,'/html/body/input[1]').send_keys('111')
# 填写密码
driver.find_element(By.XPATH,'/html/body/input[2]').send_keys('66566')
# 点击登录
driver.find_element(By.XPATH,'/html/body/button').click()
# 获取登录后的文本
text = driver.find_element(By.XPATH,'/html/body/p').text
if text == '登录成功！':
    print('通过')
