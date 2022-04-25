from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from homepages.select import Selectt
from homepages.search import Search
import pytest

from homepages.testdata import Test


class TestLogin:

    #################Select Currency####################################

    def test_changecurrency(self, setup):
        self.driver = setup
        self.lp = Selectt(self.driver)
        self.lp.selectchose(Test.EURO)
        self.driver.quit()


