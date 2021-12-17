# To illustrate window handling

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
import time

cwd=os.getcwd()
s=Service(cwd+"\\"+"Drivers"+"\\"+"chromedriver.exe")
driver=webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://yahoo.com")

driver.implicitly_wait(2)
driver.execute_script("window.scrollTo(10,1900)")  # to scroll the window
print(driver.current_window_handle)

driver.find_element(By.XPATH,"//*[@id='footer-wrapper']/div[1]/div/ul/li[1]/a").click()
print(driver.current_window_handle)

handles = driver.window_handles

print("Number of open browser windows=",len(handles))

for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)

driver.quit()