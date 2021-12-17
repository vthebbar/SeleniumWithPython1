# To illustrate the use of Webdriver conditional commands

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

from selenium.webdriver.common.by import By
import os
cwd=os.getcwd()
driver_path=cwd+"\\"+"Drivers"+"\\"+"chromedriver.exe"
s=Service(driver_path)

driver=webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://demo.opencart.com/index.php?route=account/register")

First_Name=driver.find_element(By.NAME,"firstname")
print("First Name field displayed- ",First_Name.is_displayed())
print("First Name field enabled-",First_Name.is_enabled())

Subscribe_Yes=driver.find_element(By.XPATH,"//*[@id='content']/form/fieldset[3]/div/div/label[1]/input")
print("New Letter Subscribe YES Radio button-",Subscribe_Yes.is_selected())

Subscribe_No=driver.find_element(By.XPATH,"//*[@id='content']/form/fieldset[3]/div/div/label[2]/input")
print("New Letter Subscribe NO Radio button-",Subscribe_No.is_selected())

driver.close()