from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

s = Service('C:/Drivers/chromedriver_win32/chromedriver.exe')
driver = webdriver.Chrome(service=s)
url = 'https://demo.automationtesting.in/Windows.html'
driver.get(url)

print(driver.title)
print(driver.current_url)

driver.find_element(By.XPATH, "//*[@id='Tabbed']/a/button").click()
time.sleep(5)

# driver.close()   # close focus browser

driver.quit()  # closes all the browser
