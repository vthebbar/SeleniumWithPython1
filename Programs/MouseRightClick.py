# To illustrate mouse right click

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import os
import time
cwd=os.getcwd()

s=Service(cwd+"\\"+"Drivers"+"\\"+"chromedriver.exe")
driver=webdriver.Chrome(service=s)
driver.get("http://automationpractice.com/index.php")
driver.maximize_window()

element = driver.find_element(By.XPATH,"//*[@id='header_logo']/a/img")
action=ActionChains(driver)
action.context_click(element).perform()
time.sleep(4)
driver.close()
