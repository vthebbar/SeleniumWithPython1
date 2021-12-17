# To take screenshots
from datetime import datetime
from random import random

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
import time

cwd=os.getcwd()
s=Service(cwd+"\\"+"Drivers"+"\\"+"chromedriver.exe")
driver=webdriver.Chrome(service=s)

driver.get("https://demo.opencart.com/")
driver.maximize_window()

print(datetime.now())
# Method -1
driver.save_screenshot(cwd+"\\"+"ProjectFiles"+"\\"+"Snapshots"+"\\"+"OC_"+str(datetime.now().strftime("%Y%m%d-%H%M%S%f"))+".png")

# Method -2
driver.get_screenshot_as_file(cwd+"\\"+"ProjectFiles"+"\\"+"Snapshots"+"\\"+"OC_"+str(datetime.now().strftime("%Y%m%d-%H%M%S%f"))+".png")

driver.close()