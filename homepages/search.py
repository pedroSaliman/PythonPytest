from time import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


class Search:
    search = "small-searchterms"
    searchbtn = "search-box-button"
    productlink = "//h2[@class='product-title']/child::a"
    wishlistbtn = "//div[@class='add-to-wishlist']/child::button"
    wishclick = "//a[contains(text(),'wishlist')]"
    quantity = "qty-input"
    updatecart = "updatecart"

    def __init__(self, driver):
        self.driver = driver

    def searchclick(self, text):
        self.driver.find_element_by_id(self.search).send_keys(text)
        self.driver.find_element_by_class_name(self.searchbtn).click()
        self.driver.find_element_by_xpath(self.productlink).click()
        self.driver.find_element_by_xpath(self.wishlistbtn).click()
        # wait = WebDriverWait(self.driver, 10)
        # element = wait.until(EC.element_to_be_clickable((self.wishclick, 'someid')))
        self.driver.implicitly_wait(10)

        self.driver.find_element_by_xpath(self.wishclick).click()
        self.driver.find_element_by_class_name(self.quantity).clear()
        self.driver.find_element_by_class_name(self.quantity).send_keys("4")
        self.driver.find_element_by_id(self.updatecart).click()









