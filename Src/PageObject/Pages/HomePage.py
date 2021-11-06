import sys
from selenium.webdriver.common.by import By
from Src.PageObject.Locators import Locator

sys.path.append(sys.path[0] + "/....")


class Home(object):
    def __init__(self, driver):
        self.driver = driver
        self.logo = driver.find_element(By.XPATH, Locator.logo)
        self.error_msg = driver.find_element(By.XPATH, Locator.error_msg)

    def get_error_msg(self):
        return self.error_msg

    def get_home_page_logo(self):
        return self.logo

