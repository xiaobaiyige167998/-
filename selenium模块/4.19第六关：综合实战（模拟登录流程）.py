from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# 打开页面
driver = webdriver.Edge()
url = 'file:///C:/Users/HP/Desktop/test_page.html'
driver.get(url)

# 主窗口
main_window = driver.current_window_handle

# 输入用户名密码
driver.find_element(By.XPATH,'/html/body/input[1]').send_keys('54188')
driver.find_element(By.XPATH,'/html/body/input[2]').send_keys('54188')

# 点击登录
driver.find_element(By.XPATH,'/html/body/button').click()
dl = driver.find_element(By.XPATH,'/html/body/p').text

# 验证登录成功
if dl == '登录成功！':
    print('成功')


# 点击新窗口
driver.find_element(By.XPATH,'/html/body/a').click()
# 切换窗口并打印标题
handles = driver.window_handles
for handle in handles:
    if handle!=main_window:
        driver.switch_to.window(handle)
        title = driver.title
        print(title)
        break

# 回到主页面
driver.switch_to.window(main_window)

# 进入 iframe
driver.switch_to.frame('myframe')

# 点击按钮
WebDriverWait(driver,timeout=5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/button'))).click()
text = WebDriverWait(driver,timeout=5).until(EC.presence_of_element_located((By.ID,'frame-text'))).text
# 验证 iframe 操作成功
if text == '你点击了iframe按钮':
    print('iframe操作成功')