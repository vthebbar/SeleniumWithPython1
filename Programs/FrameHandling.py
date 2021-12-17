# Frame Handling

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import os
cwd=os.getcwd()

s=Service(cwd+"\\"+"Drivers"+"\\"+"chromedriver.exe")
driver=webdriver.Chrome(service=s)

driver.get("https://chercher.tech/practice/frames")
driver.maximize_window()
driver.implicitly_wait(2)

driver.switch_to.frame("frame1")
driver.switch_to.frame("frame3")
driver.find_element(By.ID,"a").click()

driver.switch_to.default_content()
driver.switch_to.frame("frame2")
element=driver.find_element(By.ID,"animals")
dropdown=Select(element)

dropdown.select_by_value("avatar")
print("Selected avatar")
time.sleep(2)
driver.close()