# To illustrate the use of Explicit wait
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as exp
import os
cwd=os.getcwd()
driver_path= cwd+"\\"+"Drivers"+"\\"+"chromedriver.exe"

s=Service(driver_path)
driver=webdriver.Chrome(service=s)
driver.get("http://automationpractice.com")
driver.maximize_window()

# Explicit Wait
waits=WebDriverWait(driver,10)
element = waits.until(exp.element_to_be_clickable((By.CLASS_NAME, "login")))
element.click()

print("Successful")
driver.close()



