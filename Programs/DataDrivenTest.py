# To illustrate data driven test (Read from excel and write result to excel)
from selenium.webdriver import ActionChains

import Utility.ExcelUtility
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
import time

cwd=os.getcwd()
s=Service(cwd+"\\"+"Drivers"+"\\"+"chromedriver.exe")
driver=webdriver.Chrome(service=s)

# Test data path
path=cwd+"\\"+"ProjectFiles"+"\\"+"TestData.xlsx"

driver.get("https://demo.opencart.com/index.php?route=account/login")
driver.maximize_window()

rows= Utility.ExcelUtility.getRowCount(path,"Sheet1")

for r in range(2,rows+1):
    userid=Utility.ExcelUtility.readExcel(path,"Sheet1",r,1)
    password=Utility.ExcelUtility.readExcel(path,"Sheet1",r,2)

    driver.find_element(By.NAME,"email").send_keys(userid)
    driver.find_element(By.NAME,"password").send_keys(password)
    driver.find_element(By.XPATH,"//*[@id='content']/div/div[2]/div/form/input").click()

    if driver.title=="My Account":
        print("Login Successful")
        Utility.ExcelUtility.writeExcel(path,"Sheet1",r,3,"Pass")

        profile=driver.find_element(By.XPATH,"//*[@id='top-links']/ul/li[2]/a")
        logout=driver.find_element(By.XPATH,"//*[@id='top-links']/ul/li[2]/ul/li[5]/a")
        action=ActionChains(driver)
        action.move_to_element(profile).click().move_to_element(logout).click().perform()

        profile = driver.find_element(By.XPATH, "//*[@id='top-links']/ul/li[2]/a")
        login=driver.find_element(By.XPATH,"//*[@id='top-links']/ul/li[2]/ul/li[2]/a")
        action.move_to_element(profile).click().move_to_element(login).click().perform()

    else:
        print("Login Failed")
        Utility.ExcelUtility.writeExcel(path,"Sheet1",r,3,"Fail")
        driver.find_element(By.NAME, "email").clear()
        driver.find_element(By.NAME, "password").clear()


driver.close()