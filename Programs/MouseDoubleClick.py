# To illustrate the Mouse Double click

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import os

cwd=os.getcwd()

s=Service(cwd+"\\"+"Drivers"+"\\"+"chromedriver.exe")
driver=webdriver.Chrome(service=s)

driver.get("https://mousetester.com/")
driver.maximize_window()

element=driver.find_element(By.XPATH,"//*[@id='clickMe']/p")
action=ActionChains(driver)
action.double_click(element).perform()
print("Double click done")
time.sleep(5)

driver.close()