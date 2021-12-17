# Program to open web pages in Chrome, Mozilla and Firefox browsers (Launching web browsers)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service

import os
cwd=os.getcwd()
driver_path_chrome= cwd +"\\"+"Drivers"+"\\"+"chromedriver.exe"
driver_path_firefox= cwd +"\\"+"Drivers"+"\\"+"geckodriver.exe"
driver_path_edge= cwd +"\\"+"Drivers"+"\\"+"msedgedriver.exe"
''' 
# commented code
 
driver=webdriver.Chrome(executable_path="C:\\Users\\user\\PycharmProjects\\SeleniumWithPython\\Browser Drivers\\chromedriver.exe")
driver.get("https://google.com")
driver.maximize_window()
print(driver.title)
driver.close()

'''
# chrome

s=Service(driver_path_chrome)
driver=webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://demo.opencart.com/")
pageTitle= driver.title
print(pageTitle)
driver.close()


# Mozilla

s1=Service(driver_path_firefox)
driver=webdriver.Firefox(service=s1)
driver.maximize_window()
driver.get("https://demo.opencart.com/")
print(driver.title)
driver.close()

# Microsoft soft edge

s2=Service(driver_path_edge)
driver=webdriver.Edge(service=s2)
driver.maximize_window()
driver.get("https://demo.opencart.com/")
print(driver.title)
driver.close()