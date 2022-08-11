import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service('C:/Drivers/chromedriver_win32/chromedriver.exe')
driver = webdriver.Chrome(service=s)
url = 'https://demo.automationtesting.in/Windows.html'
driver.get(url)  # /FR
print(driver.title)

url1 = 'https://www.google.com/'
driver.get(url1)  # TT
time.sleep(5)
print(driver.title)

driver.back()
print(driver.title)

driver.forward()
print(driver.title)

driver.close()