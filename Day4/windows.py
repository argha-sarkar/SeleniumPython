import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service('C:/Drivers/chromedriver_win32/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.maximize_window()
url = 'https://demo.automationtesting.in/Windows.html'
driver.get(url)

driver.find_element(By.XPATH, '//*[@id="Tabbed"]/a/button').click()
print(driver.current_window_handle)  # parent window CDwindow-D7D87072E15EF0AFA1E73D9878AE3BEC
handles = driver.window_handles  # returns all the handel value of opend window

for handel in handles:
    driver.switch_to.window(handel)
    print(driver.title)
    if driver.title == "Frames & windows":
        driver.close()


time.sleep(5)
driver.quit()
