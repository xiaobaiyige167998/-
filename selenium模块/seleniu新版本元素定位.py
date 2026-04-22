from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

# 1. ID定位（最稳定）
driver.find_element(By.ID, "kw")
# 2. name定位
driver.find_element(By.NAME, "wd")
# 3. XPath定位（万能，处理复杂场景）
driver.find_element(By.XPATH, "//input[@id='kw']")
# 4. CSS选择器（推荐，比XPath简洁）
driver.find_element(By.CSS_SELECTOR, "#kw")
# 5. class定位
driver.find_element(By.CLASS_NAME, "s_ipt")
# 6. 标签名定位
driver.find_element(By.TAG_NAME, "input")
# 7. 批量定位（找所有符合条件的元素）
driver.find_elements(By.CSS_SELECTOR, "a")

driver.quit()
