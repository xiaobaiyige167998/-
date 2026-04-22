from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Edge()
url = 'file:///C:/Users/HP/Desktop/test_page.html'
driver.get(url)

address = driver.find_element(By.XPATH,'/html/body/input[1]')
address.send_keys('666')
text = driver.find_element(By.XPATH,'/html/body/input[1]').get_attribute('value')
print(text)