# To illustrate browser's Back and Forward arrows to navigate
# steps -> open google.com , on same tab open yahoo.com, <- go back and go forward ->
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os
cwd=os.getcwd()
driver_path=cwd+"\\"+"Drivers"+"\\"+"chromedriver.exe"

s=Service(driver_path)
driver=webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://google.com")
print(driver.title)
time.sleep(2)

driver.get("https://yahoo.com")
print(driver.title)
time.sleep(2)

driver.back()
time.sleep(2)
print(driver.title)

driver.forward()
time.sleep(2)
print(driver.title)

driver.close()