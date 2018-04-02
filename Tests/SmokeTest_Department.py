import unittest
import time
from selenium import webdriver

class SmokeTest_Department(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()

    def tearDown(self):
        self.driver.close()

    def test_Dpetartment_Add(self):
        DeptMenuItem=self.driver.find_element_by_xpath("/html/body[@class='skin-blue sidebar-mini']/div[@class='wrapper']/aside[@class='main-sidebar']/section[@class='sidebar']/ul[@class='sidebar-menu tree']/li[@class='treeview menu-open']/ul[@class='treeview-menu']/li[1]/a")
        DeptMenuItem.click()
        AddButton=self.driver.find_element_by_xpath("/html/body[@class='skin-blue sidebar-mini']/div[@class='wrapper']/div[@class='content-wrapper']/section[@class='content container-fluid']/div[@class='row']/div[@class='col-xs-12']/div[@class='box']/div[@class='box-body']/table[@id='example2']/thead[@id='thead']/tr/th[4]/a")
        AddButton.click()
        NameInput=self.driver.find_element_by_xpath("/html/body[@class='skin-blue sidebar-mini']/div[@class='wrapper']/div[@class='content-wrapper']/section[@class='content container-fluid']/div[@class='row']/div[@class='col-xs-12']/div[@class='box']/div[@class='box-body']/table[@id='example2']/tfoot[@id='tfoot']/tr/td[2]/input")
        NameInput.send_keys("Test")
        DescriptionInput=self.driver.find_element_by_xpath("/html/body[@class='skin-blue sidebar-mini']/div[@class='wrapper']/div[@class='content-wrapper']/section[@class='content container-fluid']/div[@class='row']/div[@class='col-xs-12']/div[@class='box']/div[@class='box-body']/table[@id='example2']/tfoot[@id='tfoot']/tr/td[3]/input")
        DescriptionInput.send("Descrption")