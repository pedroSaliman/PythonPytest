from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from homepages.select import Selectt
from homepages.search import Search
import pytest

from homepages.testdata import Test


class TestLogin:

    #################Select Currency####################################

    def test_searchproduct(self, setup):
        self.driver = setup
        self.lp = Search(self.driver)
        self.lp.searchclick(Test.PRODUCT)
        self.driver.quit()

