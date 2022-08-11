from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service('C:/Drivers/chromedriver_win32/chromedriver.exe')
driver = webdriver.Chrome(service=s)
url = "https://demo.guru99.com/test/newtours/index.php"
driver.get(url)

driver.implicitly_wait(10)

assert "Welcome: Mercury Tours" in driver.title  # verify title
driver.find_element(By.NAME, 'userName').send_keys("mercury")
driver.find_element(By.NAME, 'password').send_keys("mercury")
driver.find_element(By.NAME, 'submit').click()
