# https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html


import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


s = Service('C:/Drivers/chromedriver_win32/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.maximize_window()
url = 'https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html'
driver.get(url)

driver.switch_to.frame("packageListFrame") # First Frame
driver.find_element(By.PARTIAL_LINK_TEXT, 'org.openqa.selenium.cli').click()
time.sleep(3)

driver.switch_to.default_content()
time.sleep(3)

driver.switch_to.frame("packageFrame")
driver.find_element(By.CLASS_NAME, "interfaceName").click()

driver.switch_to.default_content()
time.sleep(3)

driver.switch_to.frame("classFrame")
driver.find_element(By.XPATH, "/html/body/header/nav/div[1]/div[1]/ul/li[6]").click()