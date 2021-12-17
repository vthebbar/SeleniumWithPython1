# To illustrate the dropdown actions
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
import os
cwd=os.getcwd()
driver_path= cwd+"\\"+"Drivers"+"\\"+"chromedriver.exe"

s=Service(driver_path)
driver=webdriver.Chrome(service=s)

driver.get("https://demo.opencart.com/index.php?route=product/category&path=20_27")
driver.maximize_window()
driver.implicitly_wait(2)

element = driver.find_element(By.ID, "input-sort")
drp = Select(element)

# count number of options in dropdown

all_options=drp.options
print("Number of dropdown options=", len(all_options))

# List of options
print("Options in dropdown list are:")
for option in all_options:
    print(option.text)

# select the drop down

# by index - method 1
#drp.select_by_index(1)

# by visible text - method 2
# drp.select_by_visible_text("Name (Z - A)")

# by value - method 3
drp.select_by_value("https://demo.opencart.com/index.php?route=product/category&path=20_27&sort=p.price&order=ASC")

time.sleep(5)
driver.close()