import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service('C:/Drivers/chromedriver_win32/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.maximize_window()
url = 'file:///C:/Users/Argha/Desktop/table1.html'
driver.get(url)

cols = len(driver.find_elements(By.XPATH, '/html/body/table/tbody/tr[1]/th'))
rows = len(driver.find_elements(By.XPATH, '/html/body/table/tbody/tr'))

print(cols)
print(rows)
print("Name" + "                 " + "Add" + "                 " + "Con")

for r in range(2, rows + 1):
    for c in range(1, cols + 1):
        value = driver.find_element(By.XPATH, "/html/body/table/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(value, end='                ')
    print()
