# Unit Test with more than 1 method

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import  os
cwd=os.getcwd()
path=cwd.replace("UnitTestFramework","Drivers")
print(path)

class Display(unittest.TestCase):
    def test_google(self):
        s = Service(path + "\\" + "chromedriver.exe")
        self.driver=webdriver.Chrome(service=s)
        self.driver.get("https://google.com")
        self.title=self.driver.title
        print("Page Title=",self.title)

    def test_yahoo(self):
        s = Service(path + "\\" + "chromedriver.exe")
        self.driver=webdriver.Chrome(service=s)
        self.driver.get("https://yahoo.com")
        self.title=self.driver.title
        print("Page title=", self.title)

if __name__ == "__main__":
    unittest.main()