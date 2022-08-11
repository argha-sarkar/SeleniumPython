import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

s = Service('C:/Drivers/chromedriver_win32/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://www.ebay.com/")
wait = WebDriverWait(driver, 20)

wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@class='gh-tb ui-autocomplete-input']"))).send_keys("Mobile")
driver.find_element(By.ID, 'gh-btn').click()

element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="x-refine__group_1__0"]/ul/li[1]/div/a/div/div/div/span[2]')))
element.click()

time.sleep(3)
driver.quit()
