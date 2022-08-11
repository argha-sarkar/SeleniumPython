from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service('C:/Drivers/chromedriver_win32/chromedriver.exe')
driver = webdriver.Chrome(service=s)
url = 'https://demo.guru99.com/test/newtours/'
driver.get(url)

usr_ele = driver.find_element(By.NAME, 'userName')
print(usr_ele.is_displayed())
print(usr_ele.is_enabled())

pas = driver.find_element(By.NAME, 'password')
print(pas.is_displayed())
print(pas.is_enabled())

usr_ele.send_keys('mercury')
pas.send_keys('mercury')

driver.find_element(By.NAME, 'submit').click()

roundtrip = driver.find_element(By.CSS_SELECTOR, 'input[value=roundtrip]')
print("Status of trip",roundtrip.is_selected())

onetrip = driver.find_element(By.CSS_SELECTOR, 'input[value=oneway]')
print("This is the one way radio button",onetrip.is_selected())

