# To illustrate the use of browser commands

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

from selenium.webdriver.common.by import By
import os
cwd=os.getcwd()
print("cwd=", cwd)
driver_path= cwd + "\\"+"Drivers"+"\\"+"chromedriver.exe"
print("path=",driver_path)
s=Service(driver_path)
driver=webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("http://www.seleniumframework.com/Practiceform/")
driver.find_element(By.XPATH, "//*[@id='content']/div[2]/div[2]/div/div[1]/div/p[4]/button").click()
time.sleep(5)
print(driver.title) # get page title
print(driver.current_url) # get current page URL
driver.close()  # closes currently focused browser tab ony

s1=Service(driver_path)
driver=webdriver.Chrome(service=s1)
driver.maximize_window()
driver.get("http://www.seleniumframework.com/Practiceform/")
driver.find_element(By.XPATH,"//*[@id='button1']").click()
time.sleep(5)
print(driver.title)
print(driver.current_url)
driver.quit() # closes all open browsers/tabs of this session

