# To illustrate file download in chrome

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
import time

cwd=os.getcwd()

chromeoptions=Options()
chromeoptions.add_experimental_option("prefs",{"download.default_directory":cwd+"\\"+"ProjectFiles"+"\\"+"Downloads"})

s=Service(cwd+"\\"+"Drivers"+"\\"+"chromedriver.exe")
driver=webdriver.Chrome(service=s,options=chromeoptions)

driver.get("http://demo.automationtesting.in/FileDownload.html")
driver.maximize_window()

element1=driver.find_element(By.ID,"textbox")
driver.execute_script("arguments[0].scrollIntoView()",element1)
element1.send_keys("Text file contents")
driver.find_element(By.ID,"createTxt").click()
time.sleep(1)
driver.find_element(By.ID,"link-to-download").click()
time.sleep(1)

element2=driver.find_element(By.ID,"pdfbox")
element2.send_keys("PDF file contents")
driver.find_element(By.ID,"createPdf").click()
time.sleep(1)
driver.find_element(By.ID,"pdf-link-to-download").click()

time.sleep(4)
driver.close()

