from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from homepages.login import Login
from homepages.select import Selectt
from homepages.search import Search
import pytest

from homepages.testdata import Test


class TestRegister:

    #################Select Currency####################################

    def test_reg(self, setup):
        self.driver = setup
        self.lp = Login(self.driver)
        self.lp.setusername(Test.fname,Test.lname,Test.email,Test.password,Test.conpass)
        self.driver.quit()

