# To illustrate the use of implicit wait

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
cwd=os.getcwd()
driver_path=cwd+"\\"+"Drivers"+"\\"+"chromedriver.exe"

s=Service(driver_path)
driver=webdriver.Chrome(service=s)
driver.get("http://automationpractice.com/")
driver.maximize_window()

driver.implicitly_wait(10) # implicit wait

driver.find_element(By.CLASS_NAME,"login").click()
driver.close()