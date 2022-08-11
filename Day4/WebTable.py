import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service('C:/Drivers/chromedriver_win32/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.maximize_window()
url = 'https://demo.guru99.com/test/web-table-element.php#'
driver.get(url)

rows = len(driver.find_elements(By.XPATH, '//*[@id="leftcontainer"]/table/thead'))
cols = len(driver.find_elements(By.XPATH, '//*[@id="leftcontainer"]/table/thead/tr/th'))

print(rows)
print(cols)

rows = len(driver.find_elements(By.XPATH, '//*[@id="leftcontainer"]/table/tbody/tr'))
print(rows)




