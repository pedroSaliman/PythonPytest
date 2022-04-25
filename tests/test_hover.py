from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from homepages.home import Home
from homepages.hover import Hover
from homepages.select import Selectt
from homepages.search import Search
import pytest

from homepages.testdata import Test


class TestHover:

    #####################################################

    def test_dohover(self, setup):
        self.driver = setup
        self.lp = Hover(self.driver)
        self.lp.thehover()
        self.driver.quit()

