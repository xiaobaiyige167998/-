from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Edge()
url = 'file:///C:/Users/HP/Desktop/test_page.html'
driver.get(url)

# 点击+输入
driver.find_element(By.ID,'username').send_keys('1679988903')
driver.find_element(By.ID,'password').send_keys('wwww')
e = driver.find_element(By.ID,'login-btn')
# driver.find_element(By.ID,'login-btn').click()
driver.execute_script("arguments[0].click()",e)
time.sleep(2)

# 主页面
main_window = driver.current_window_handle

# 获取文本
print(driver.find_element(By.ID, 'message').text)

# 获取属性
print(driver.find_element(By.ID, 'new-window').get_attribute('href'))

# 窗口切换
driver.find_element(By.ID,'new-window').click()
handles = driver.window_handles
for handle in handles:
    if handle != main_window:
        driver.switch_to.window(handle)
time.sleep(6)
driver.switch_to.window(main_window)
# iframe切换
driver.switch_to.frame('myframe')
WebDriverWait(driver,timeout=3).until(EC.element_to_be_clickable((By.ID,'frame-btn'))).click()
print(WebDriverWait(driver, timeout=3).until(EC.presence_of_element_located((By.ID, 'frame-text'))).text)
time.sleep(2)
