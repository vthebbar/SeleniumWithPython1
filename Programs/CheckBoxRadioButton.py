# To illustrate using check box and radio button

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os
cwd=os.getcwd()
driver_path=cwd+"\\"+"Drivers"+"\\"+"chromedriver.exe"

s=Service(driver_path)
driver=webdriver.Chrome(service=s)

driver.get("https://demo.opencart.com/index.php?route=account/register")
driver.maximize_window()
driver.implicitly_wait(2)

driver.execute_script("window.scrollTo(1200,1500);")

# Radio buttons
Yes_status=driver.find_element(By.XPATH, "//*[@id='content']/form/fieldset[3]/div/div/label[1]/input").is_selected()
print("Radio button -Subscribe Yes status=", Yes_status)

No_status=driver.find_element(By.XPATH, "//*[@id='content']/form/fieldset[3]/div/div/label[2]/input").is_selected()
print("Radio button -Subscribe No status=", No_status)

driver.find_element(By.XPATH, "//*[@id='content']/form/fieldset[3]/div/div/label[1]/input").click()

# Check box

Check_box_status=driver.find_element(By.CSS_SELECTOR,"input[name='agree']").is_selected()
print("Check box selected =", Check_box_status)

driver.find_element(By.CSS_SELECTOR,"input[name='agree']").click()

print("****After selection*****")

Yes_status=driver.find_element(By.XPATH, "//*[@id='content']/form/fieldset[3]/div/div/label[1]/input").is_selected()
print("Radio button -Subscribe Yes status=", Yes_status)

No_status=driver.find_element(By.XPATH, "//*[@id='content']/form/fieldset[3]/div/div/label[2]/input").is_selected()
print("Radio button -Subscribe No status=", No_status)

Check_box_status=driver.find_element(By.CSS_SELECTOR,"input[name='agree']").is_selected()
print("Check box selected =", Check_box_status)

driver.close()