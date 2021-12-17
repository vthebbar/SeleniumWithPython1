# To illustrate the use of input text box
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
cwd=os.getcwd()
driver_path=cwd+"\\"+"Drivers"+"\\"+"chromedriver.exe"

s=Service(driver_path)
driver=webdriver.Chrome(service=s)
driver.get("https://demo.opencart.com/index.php?route=account/register")
driver.maximize_window()
driver.implicitly_wait(2)

# count the number of input text boxes

input_text_boxes=driver.find_elements(By.CSS_SELECTOR,"input[type=text]")
print("Number of input TEXT boxes=",len(input_text_boxes))

# Verify the condition displayed ? enabled ?

displayed=driver.find_element(By.NAME,"firstname").is_displayed()
print("Displayed=", displayed)
enabled=driver.find_element(By.NAME,"firstname").is_enabled()
print("Enabled=", enabled)

# key in the value

driver.find_element(By.NAME,"firstname").send_keys("vishwa")
time.sleep(4)

print("Success")
driver.close()