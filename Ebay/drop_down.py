from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

s = Service('C:/Drivers/chromedriver_win32/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.maximize_window()
url = 'https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407'
driver.get(url)

elem = driver.find_element(By.ID, "RESULT_RadioButton-9")
drp = Select(elem)

# drp.select_by_visible_text("Morning")

# drp.select_by_index(2)  # Afternoon

drp.select_by_value("Radio-2") #Evening

# Count Number options
print(len(drp.options))

# Capture All options and print them as Output

all_opt = drp.options
for option in all_opt:
    print(option.text)
