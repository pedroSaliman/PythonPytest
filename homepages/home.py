from webdriver_manager import driver

from homepages.base import Base
from selenium.webdriver.common.by import By

from homepages.testdata import Test


class Home(Base):
    def __init__(self, driver):
        super().__init__(driver)

    btn=(By.LINK_TEXT,"Contact us")
    fullname=(By.ID,"FullName")
    email=(By.ID,"Email")
    txtarea=(By.ID,"Enquiry")
    senemail=(By.NAME,"send-email")



    def script(self):
      self.driver.execute_script("scroll(0,2550)")
      self.click(self.btn)
    def sendemailinfo(self,thefullname,theemail,thetextarea):
        self.type(self.fullname, thefullname)
        self.type(self.email, theemail)
        self.type(self.txtarea, thetextarea)
        self.click(self.senemail)




