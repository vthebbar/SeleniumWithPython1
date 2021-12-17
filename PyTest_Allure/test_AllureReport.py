# To illustrate the generation of Allure report using selenium+Pytest+Allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By

import pytest
import allure

class TestOC:

    @pytest.fixture()
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        yield
        self.driver.close()

    @allure.severity(allure.severity_level.NORMAL)
    def test_LoginPageTitle(self, setup):  # Fail This
        self.driver.get("https://demo.opencart.com/index.php?route=account/login")
        login_page_title= self.driver.title
        if login_page_title == "Account Login1":
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="testLogintitle", attachment_type=AttachmentType.PNG)
            assert False

    @allure.severity(severity_level=allure.severity_level.CRITICAL)
    def test_Login(self, setup):   # Pass this
        self.driver.get("https://demo.opencart.com/index.php?route=account/login")
        self.driver.find_element(By.ID,"input-email").send_keys("vtest@gmail.com")
        self.driver.find_element(By.ID,"input-password").send_keys("1234")
        self.driver.find_element(By.XPATH,"//*[@id='content']/div/div[2]/div/form/input").click()
        title_after_login = self.driver.title
        if title_after_login == "My Account":
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="testLogin",attachment_type=AttachmentType.PNG)
            assert False

    @allure.severity(allure.severity_level.MINOR)
    def test_Register(self, setup):  # Skip this
        pytest.skip("Method not ready - skip it")

