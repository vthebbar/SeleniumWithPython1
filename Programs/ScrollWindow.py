# To scroll the window (3 ways to scroll)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import time
import os

cwd=os.getcwd()

s=Service(cwd+"\\"+"Drivers"+"\\"+"chromedriver.exe")
driver=webdriver.Chrome(service=s)

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()
driver.implicitly_wait(2)

# scroll based on pixel
driver.execute_script("window.scrollBy(0,708)")
time.sleep(2)
# driver.close()


driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()
driver.implicitly_wait(2)

# scroll till element
element=driver.find_element(By.XPATH,"//*[@id='content']/div[2]/div[2]/table[1]/tbody/tr[86]/td[2]")
driver.execute_script("arguments[0].scrollIntoView();",element)
time.sleep(2)

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()
driver.implicitly_wait(2)

# scroll till the end of page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(2)

driver.close()

print("Sucessful")