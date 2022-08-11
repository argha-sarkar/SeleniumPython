import time
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

s = Service('C:/Drivers/chromedriver_win32/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://www.expedia.com/")
wait = WebDriverWait(driver, 10)

WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//a[@aria-controls='wizard-flight-pwa']//span"))).click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@aria-controls='wizard-flight-tab-oneway']//span"))).click()
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='location-field-leg1-origin']"))).send_keys("Delhi")
time.sleep(10)
WebDriverWait(driver, 10).until(EC.visibility_of_any_elements_located((By.XPATH, "//input[@id='location-field-leg1-destination']"))).send_keys("New York")

NYC = wait.until(driver.find_element(By.ID, 'location-field-leg1-destination')).send_keys("NYC")  # destination

button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="d1-btn"]')))
button.send_keys('18/08/2022')


driver.find_element(By.XPATH, "//*[@id='wizard-flight-pwa-1']/div[3]/div[2]/button").click()
