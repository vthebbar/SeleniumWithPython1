# Work with links

import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
cwd = os.getcwd()

s = Service(cwd+"\\"+"Drivers"+"\\"+"chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("http://automationpractice.com/")
driver.maximize_window()
driver.implicitly_wait(4)

# count number of links (a - anchor tags) in a page
links = driver.find_elements(By.TAG_NAME,"a")
print("Number of links in this page=",len(links))

# print all links in this page
print("Links in the page are:")
for l in links:
    print(l.text)


# click on link - Approach 1 using partial link text
# driver.find_element(By.PARTIAL_LINK_TEXT,"Cont").click()

# click on link - Approach 1 using  link text
driver.find_element(By.LINK_TEXT,"Contact us").click()

driver.close()