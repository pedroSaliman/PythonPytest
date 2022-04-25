from homepages.base import Base
from selenium import webdriver

from selenium.webdriver.common.by import By


class Login(Base):
    text_by_fname_id = (By.ID, "FirstName")
    text_lname = (By.ID, "LastName")
    btn_id = (By.ID, "register-button")
    gender_id = (By.ID, "gender-male")
    email = (By.ID, "Email")
    thepassword = (By.ID, "Password")
    theconpass = (By.ID, "ConfirmPassword")
    regbtn = (By.CLASS_NAME, "ico-register")
    result = (By.CLASS_NAME, "result")

    ####################################
    def __init__(self, driver):
        super().__init__(driver)

    def setusername(self, fname, lname, themail, password, conpass):
        self.click(self.regbtn)
        self.click(self.gender_id)
        # self.driver.find_element_by_id(self.gender_id).click()
        # self.driver.find_element_by_id(self.text_by_fname_id).send_keys(fname)
        self.type(self.text_by_fname_id, fname)
        self.type(self.text_lname, lname)
        self.type(self.email, themail)
        self.type(self.thepassword, password)
        self.type(self.theconpass, conpass)

        # self.driver.find_element_by_id(self.text_lname).send_keys(lname)
        # self.driver.find_element_by_id(self.email).send_keys(themail)
        # self.driver.find_element_by_id(self.thepassword).send_keys(password)
        # self.driver.find_element_by_id(self.theconpass).send_keys(conpass)
        # self.driver.find_element_by_id(self.btn_id).click()
        self.click(self.btn_id)








