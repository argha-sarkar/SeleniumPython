from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# driver = webdriver.Chrome(executable_path ="C:\Drivers\chromedriver_win32\chromedriver.exe")

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.get("https://demo.guru99.com/test/newtours/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
# print(driver.page_source)
driver.close()