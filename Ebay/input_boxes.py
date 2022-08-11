# https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service('C:/Drivers/chromedriver_win32/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.maximize_window()
url = 'https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407'
driver.get(url)

input_boxes = driver.find_elements(By.CLASS_NAME, "text_field")
print(len(input_boxes))

status = driver.find_element(By.ID, "RESULT_TextField-1").is_displayed()
print("Displayed or Not: ", status)

status = driver.find_element(By.ID, "RESULT_TextField-1").is_enabled()
print('Enabled or Not: ', status)

driver.find_element(By.ID, "RESULT_TextField-1").send_keys("AJ")
driver.find_element(By.ID, "RESULT_TextField-2").send_keys("SR")
driver.find_element(By.ID, "RESULT_TextField-3").send_keys("7872379071")
driver.find_element(By.ID, "RESULT_TextField-4").send_keys("IND")
driver.find_element(By.ID, "RESULT_TextField-5").send_keys("BNG")
driver.find_element(By.ID, "RESULT_TextField-6").send_keys("aj@45.com")

gender = driver.find_element(By.XPATH, '//*[@id="q26"]/table/tbody/tr[1]/td/label')
gender.click()