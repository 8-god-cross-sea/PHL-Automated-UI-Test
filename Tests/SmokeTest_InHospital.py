import unittest
import time
from selenium import webdriver

class SmokeTest_InHospital(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()

    def tearDown(self):
        self.driver.close()

