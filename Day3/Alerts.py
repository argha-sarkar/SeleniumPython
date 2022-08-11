import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

s = Service('C:/Drivers/chromedriver_win32/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.maximize_window()
url = 'https://testautomationpractice.blogspot.com/'
driver.get(url)

driver.find_element(By.XPATH, '//*[@id="HTML9"]/div[1]/button').click()

time.sleep(5)

# Alert(driver).accept() # Automatic alert press Ok
Alert(driver).dismiss()  # Automatic alert press Cancel
