import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

s = Service('C:/Drivers/chromedriver_win32/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.maximize_window()
url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
driver.get(url)

time.sleep(10)

driver.find_element(By.XPATH, '//input[@name="username"]').send_keys("Admin")
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input').send_keys('admin123')
driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()

time.sleep(10)

admin = driver.find_element(By.XPATH, '//li[@class="oxd-main-menu-item-wrapper"]')
usermgmt = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/span')
time.sleep(10)
usrers = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li/a')

actions = ActionChains(driver)
actions.move_to_element(admin).move_to_element(usermgmt).move_to_element(usrers).click().perform()

