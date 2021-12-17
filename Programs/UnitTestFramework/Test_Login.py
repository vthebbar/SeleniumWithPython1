# Test case to generate HTML report
'''
Steps/Methods:-
1) Launch browser
2) Verify home page title
3) Verify Login
4) Logout
5) close browser
'''

import unittest
from selenium import webdriver
import time
import HtmlTestRunner
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import os


class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cwd = os.getcwd()
        path = cwd.replace("UnitTestFramework", "Drivers")
        s = Service(path + "\\" + "chromedriver.exe")
        cls.driver = webdriver.Chrome(service=s)
        cls.driver.maximize_window()

    def test_PageTitle(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.assertEqual("OrangeHRM", self.driver.title, "Page title is not matching")

    def test_Login(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element(By.ID,"txtUsername").send_keys("Admin")
        self.driver.find_element(By.ID,"txtPassword").send_keys("admin123")
        self.driver.find_element(By.ID,"btnLogin").click()

    def test_Logout(self):
        action=ActionChains(self.driver)
        welcome=self.driver.find_element(By.ID,"welcome")
        logout=self.driver.find_element(By.ID, "welcome-menu")
        action.move_to_element(welcome).click().move_to_element(logout).click().perform()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        print("Test completed.")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="..\\Reports"))
