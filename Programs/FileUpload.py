# To illustrate file upload

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import time
import os

cwd=os.getcwd()
s=Service(cwd+"\\"+"Drivers"+"\\"+"chromedriver.exe")

driver=webdriver.Chrome(service=s)
driver.get("https://www.w3schools.com/howto/tryit.asp?filename=tryhow_html_file_upload_button")
driver.maximize_window()
path=cwd+"/"+"ProjectFiles"+"/"+"Uploadfile.txt"
driver.switch_to.frame(1)
driver.find_element(By.ID,"myFile").send_keys(path)
driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()
time.sleep(1)
result=driver.find_element(By.XPATH,"/html/body/p").text
print(result)
driver.close()