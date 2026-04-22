from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Edge()
url = 'https://the-internet.herokuapp.com/iframe'
driver.get(url)
# # 点击会出现新窗口的标签
# driver.find_element(By.XPATH,'/html/body/div[2]/div/div/a').click()
# # 获取所有窗口句柄
# handles = driver.window_handles
# # 切换到新窗口，一般为第二个
# driver.switch_to.window(handles[1])
# 切入 iframe
driver.switch_to.frame('mce_0_ifr')
name = WebDriverWait(driver,timeout=5).until(EC.element_to_be_clickable((By.XPATH,'/html/body/p'))).text
print(name)
time.sleep(4)
driver.quit()