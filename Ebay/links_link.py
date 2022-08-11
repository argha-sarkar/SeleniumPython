from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service('C:/Drivers/chromedriver_win32/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.maximize_window()
url = 'https://demo.guru99.com/test/newtours/'
driver.get(url)

links = driver.find_elements(By.TAG_NAME, "a")
print("Number of Links Present in the webpage: ", len(links))  # How many links present in a page

for link in links:
    print(link.text)

# Clicking Link
# driver.find_element(By.LINK_TEXT, "REGISTER").click()

driver.find_element(By.PARTIAL_LINK_TEXT, "REG").click()
