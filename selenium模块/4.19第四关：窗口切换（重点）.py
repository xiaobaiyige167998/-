import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
url = 'file:///C:/Users/HP/Desktop/test_page.html'
driver.get(url)
# 记录主窗口位置
main_window = driver.current_window_handle

# 点击按钮
driver.find_element(By.XPATH,'/html/body/a').click()

# 获取所有窗口句柄
handles = driver.window_handles

# 切换窗口
driver.switch_to.window(handles[1])

# 获取标题
title = driver.title
print(title)

# 关闭窗口
driver.close()

# 返回主窗口
driver.switch_to.window(main_window)
time.sleep(3)