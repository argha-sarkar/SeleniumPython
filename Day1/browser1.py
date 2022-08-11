from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service('C:/Drivers/chromedriver_win32/chromedriver.exe')
browser = webdriver.Chrome(service=s)
url = 'https://demo.guru99.com/test/newtours/'
browser.get(url)


print(browser.current_url)
print(browser.title)
browser.close()