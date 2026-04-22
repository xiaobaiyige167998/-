import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Edge()
url = 'file:///C:/Users/HP/Desktop/test_page.html'
driver.get(url)

# 点击+输入
# driver.find_element(By.ID,'username').send_keys('1566')
# driver.find_element(By.ID,'password').send_keys('666')
# driver.find_element(By.ID,'login-btn').click()
# time.sleep(2)

# 主窗口
main_window = driver.current_window_handle

# 获取文本
print(WebDriverWait(driver, timeout=2).until(EC.presence_of_element_located((By.ID, 'message'))).text)

# 获取属性值
print(
    WebDriverWait(driver, timeout=2).until(EC.presence_of_element_located((By.ID, 'new-window'))).get_attribute('href'))

# 窗口切换
WebDriverWait(driver,timeout=2).until(EC.element_to_be_clickable((By.ID,'new-window'))).click()
handles = driver.window_handles
for handle in handles:
    if handle!=main_window:
        driver.switch_to.window(handle)
time.sleep(6)
driver.switch_to.window(main_window)
time.sleep(3)

# iframe切换
driver.switch_to.frame('myframe')
driver.find_element(By.ID,'frame-btn').click()
# 从iframe切换到主界面
driver.switch_to.default_content()
time.sleep(2)


# js点击
dj = driver.find_element(By.ID,'login-btn')
driver.execute_script('arguments[0].click();',dj)
time.sleep(3)
print('js点击成功')


driver.quit()