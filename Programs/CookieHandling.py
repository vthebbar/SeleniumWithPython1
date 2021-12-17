# To Handle cookies

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
import time

cwd=os.getcwd()
s=Service(cwd+"\\"+"Drivers"+"\\"+"chromedriver.exe")
driver=webdriver.Chrome(service=s)

driver.get("https://www.flipkart.com/")

cookies=driver.get_cookies()
print("Total cookies=",len(cookies))
print("Cookie are:")
print(cookies)

print("******")
# add cookies
cookie={'name':'test','value':'1234'}
driver.add_cookie(cookie)
cookies=driver.get_cookies()
print("Total cookies=",len(cookies))
print("Cookie are:")
print(cookies)

print("*********")
# delete a cookie
driver.delete_cookie('test')
time.sleep(2)
cookies=driver.get_cookies()
print("Total cookies=",len(cookies))
print("Cookie are:")
print(cookies)

print("*******")
# delete all cookies

driver.delete_all_cookies()
time.sleep(2)
cookies=driver.get_cookies()
print("After all deleted-Total cookies=",len(cookies))
print("Cookie are:")
print(cookies)

driver.close()