
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium import webdriver

from homepages.base import Base




class Hover(Base):
    # selectEuro="customerCurrency"

    # comp = (By.XPATH,"//body/div[6]/div[2]/ul[1]/li[1]/a[1]")
    comp="//body/div[6]/div[2]/ul[1]/li[1]/a[1]"
    desk = "//body/div[6]/div[2]/ul[1]/li[1]/ul[1]/li[1]/a[1]"


      ####################################
    def __init__(self,driver):
        self.driver = driver





    def thehover(self):
       self.actions = ActionChains(self.driver)
       self.actions.move_to_element(self.driver.find_element(By.XPATH,self.comp)).perform()
       self.actions.move_to_element(self.driver.find_element(By.XPATH,self.desk)).click().perform()