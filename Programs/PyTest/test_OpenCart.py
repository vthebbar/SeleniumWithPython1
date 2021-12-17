# To illustrate the use of pytest-html to generate html report

from selenium import webdriver
from selenium.webdriver.common.service import Service
from selenium.webdriver.common.by import By
import pytest
import pytest_html



class TestOC:

    @pytest.fixture()
    def setup(self):
        # statements before yield will be executed before every method
        self.driver = webdriver.Chrome()
        # if we copy drives inside python->Scripts folder then webdriver.chrome() can be called without any parameter
        self.driver.maximize_window()
        yield
        # statements after yield will be executed after every method
        self.driver.close()

    def test_LoginPageTitle(self,setup):
        self.driver.get("https://demo.opencart.com/index.php?route=account/login")
        assert self.driver.title == "Account Login1"


    def test_Login(self, setup):
        self.driver.get("https://demo.opencart.com/index.php?route=account/login")
        self.driver.find_element(By.ID,"input-email").send_keys("vtest@gmail.com")
        self.driver.find_element(By.ID,"input-password").send_keys("1234")
        self.driver.find_element(By.XPATH,"//*[@id='content']/div/div[2]/div/form/input").click()
        assert self.driver.title == "My Account"

    def test_Register(self,setup):
        pytest.skip("Method not read- skipped")
