from lib2to3.pgen2 import driver
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from  homepages.base import Base
class Selectt(Base):
    # selectEuro="customerCurrency"



      ####################################
    def __init__(self,driver):
        self.driver=driver



    def selectchose(self,text):
       self.s=Select(self.driver.find_element_by_id("customerCurrency"))
       self.s.select_by_visible_text(text)