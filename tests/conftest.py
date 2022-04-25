
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from homepages.testdata import Test


@pytest.fixture()
def setup():
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(Test.BASE_URL)
        driver.maximize_window()

        return driver
