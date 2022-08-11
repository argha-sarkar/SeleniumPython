# https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


s = Service('C:/Drivers/chromedriver_win32/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.maximize_window()
url = 'https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407'
driver.get(url)
wait = WebDriverWait(driver, 20)

# Working with the radio Button
status = driver.find_element(By.XPATH, '//*[@id="q26"]/table/tbody/tr[1]/td/label').is_selected();
print(status)

wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="q26"]/table/tbody/tr[1]/td/label'))).click()
time.sleep(10)
status = driver.find_element(By.XPATH, '//*[@id="q26"]/table/tbody/tr[1]/td/label').is_selected();
print(status)


# Working with check Boxes
driver.find_element(By.XPATH, '//*[@id="q15"]/table/tbody/tr[1]/td/label').click()
driver.find_element(By.XPATH, '//*[@id="q15"]/table/tbody/tr[7]/td/label').click()


status = driver.find_element(By.XPATH, '//*[@id="q15"]/table/tbody/tr[1]/td/label').is_selected();

print(status)