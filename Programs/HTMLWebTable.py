# To handle HML web tables

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os

cwd=os.getcwd()
s=Service(cwd+"\\"+"Drivers"+"\\"+"chromedriver.exe")
driver=webdriver.Chrome(service=s)
driver.get("https://cosmocode.io/automation-practice-webtable/")
driver.maximize_window()
driver.implicitly_wait(2)

# count number of rows and columns in table

rows=len(driver.find_elements(By.XPATH,"//*[@id='countries']/tbody/tr"))
print("Number of rows=",rows)
cols=len(driver.find_elements(By.XPATH,"//*[@id='countries']/tbody/tr[1]/td"))
print("Number of columns=", cols)

# print table values

# print("Visited  "+"       Country "+"         Capital "+"       Currency   "+"      Language ")

for r in range(1,rows+1):
    for c in range(1,cols+1):
        if r!=1 and c == 1:
            chkbox = driver.find_element(By.XPATH,"//*[@id='countries']/tbody/tr["+str(r)+"]/td["+str(c)+"]").is_selected()
            print(chkbox,end=" ")
        table_item=driver.find_element(By.XPATH,"//*[@id='countries']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(table_item,end="          ")
    print()

driver.close()