# To illustrate mouse over action

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import time
import os

cwd=os.getcwd()

s=Service(cwd+"\\"+"Drivers"+"\\"+"chromedriver.exe")
driver=webdriver.Chrome(service=s)

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

driver.find_element(By.ID,"txtUsername").send_keys("Admin")
driver.find_element(By.ID,"txtPassword").send_keys("admin123")
driver.find_element(By.ID,"btnLogin").click()
driver.implicitly_wait(2)

Admin=driver.find_element(By.ID,"menu_admin_viewAdminModule")
User_management=driver.find_element(By.ID,"menu_admin_UserManagement")
Users=driver.find_element(By.ID,"menu_admin_viewSystemUsers")

action=ActionChains(driver)
action.move_to_element(Admin).move_to_element(User_management).move_to_element(Users).click().perform()

time.sleep(4)

driver.close()

