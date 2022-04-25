from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from homepages.home import Home
from homepages.select import Selectt
from homepages.search import Search
import pytest

from homepages.testdata import Test


class TestLogin:

    #################Select Currency####################################

    def test_changecurrency(self, setup):
        self.driver = setup
        self.lp = Home(self.driver)
        self.lp.script()
        self.lp.sendemailinfo(Test.THE_USER_NAME,Test.THE_EMAIL,Test.TEXT_AREA)
        self.driver.quit()

