# Alert Handling

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
cwd=os.getcwd()

s = Service(cwd+"\\"+"Drivers"+"\\"+"chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
driver.maximize_window()
driver.find_element(By.NAME,"confirmation").click()
time.sleep(2)
a= driver.switch_to.alert.accept()
if a==None:
    print("Alert Accepted")
time.sleep(2)
driver.find_element(By.NAME,"confirmation").click()
time.sleep(2)
b = driver.switch_to.alert.dismiss()
if b==None:
    print("Alert Dismissed")
time.sleep(2)
driver.close()