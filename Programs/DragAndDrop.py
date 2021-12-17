# To illustrate drag and drop

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from seletools.actions import drag_and_drop
import os
import time
cwd=os.getcwd()

s=Service(cwd+"\\"+"Drivers"+"\\"+"chromedriver.exe")
driver=webdriver.Chrome(service=s)
driver.get("https://chercher.tech/practice/drag-and-drop-example")
driver.maximize_window()
#driver.switch_to.frame(1)

src=driver.find_element(By.ID,"div1")
tgt=driver.find_element(By.ID,"div2")

#action=drag_and_drop(driver)

#action.click_and_hold(src).move_to_element(tgt).release(tgt).perform()
drag_and_drop(driver,src,tgt)
#driver.close()