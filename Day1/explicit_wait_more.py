import time
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

s = Service('C:/Drivers/chromedriver_win32/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.implicitly_wait(5)
driver.maximize_window()
url = "https://www.fakeflighttickets.com/"
driver.get(url)

driver.find_element(By.XPATH, '//*[@id="___gatsby"]/div[2]/div[1]/form/div[1]/div[1]/div/label').click()

time.sleep(10)
driver.find_element(By.XPATH, '//*[@id="___gatsby"]/div[2]/div[1]/form/div[2]/div[1]/div/input').send_keys("BOM")

time.sleep(10)
driver.find_element(By.XPATH, '//*[@id="___gatsby"]/div[2]/div[1]/form/div[2]/div[2]/div/input').send_keys("DEL")

time.sleep(2)
# driver.find_element(By.XPATH, '//*[@id="___gatsby"]/div[2]/div[1]/form/div[2]/div[3]/div/div/input').clear()
driver.find_element(By.XPATH, '//*[@id="___gatsby"]/div[2]/div[1]/form/div[2]/div[3]/div/div/input').send_keys('26 Aug, 2022')


time.sleep(2)
# driver.find_element(By.XPATH, '//*[@id="___gatsby"]/div[2]/div[1]/form/div[2]/div[4]/div/div/input').clear()
# driver.find_element(By.XPATH, '//*[@id="___gatsby"]/div[2]/div[1]/form/div[2]/div[4]/div/div/input').send_keys('07 Sep, 2022')

driver.find_element(By.XPATH, '//*[@id="___gatsby"]/div[2]/div[1]/form/div[5]/button').click()