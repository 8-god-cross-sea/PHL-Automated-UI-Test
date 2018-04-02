import unittest
import time
from selenium import webdriver

class SmokeTest_Department(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()

    def tearDown(self):
        self.driver.close()

