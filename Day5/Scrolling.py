import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service('C:/Drivers/chromedriver_win32/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.maximize_window()
url = 'https://www.countries-ofthe-world.com/flags-of-the-world.html'
driver.get(url)

# 1. Scroll down the page by pixel
# driver.execute_script("window.scrollBy(0,500)", "")

# 2. scroll down the page till element found
# flag = driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[2]/table[1]/tbody/tr[86]/td[1]/img')
# driver.execute_script("arguments[0].scrollIntoView();", flag)

# 3. scroll to end of the page
driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
