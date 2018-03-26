import unittest
import time
from selenium import webdriver


class SmokeTest_Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("C:\webdrivers\chromedriver.exe")

    def test_login_as_Administrator(self):
        driver = self.driver
        driver.get("http://phl.kaitohh.com/login.html")
        time.sleep(5)
        UsernameEdit = driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/input")
        UsernameEdit.text = "Admin"
        PasswordEdit = driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/input")
        PasswordEdit.send_keys("Admin")
        SignInButton = driver.find_element_by_xpath("//*[@id=\"loginBTN\"]")
        SignInButton.click()
        # Assertion
        # should be logged in as administrator

    def test_login_as_User(self):
        driver = self.driver
        driver.get("http://phl.kaitohh.com/login.html")
        UsernameEdit = driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/input")
        UsernameEdit.text = "User"
        PasswordEdit = driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/input")
        PasswordEdit.send_keys("User")
        SignInButton = driver.find_element_by_xpath("//*[@id=\"loginBTN\"]")
        SignInButton.click()
        # Assertion
        # should be logged in as User

    def tearDown(self):
        self.driver.close()
