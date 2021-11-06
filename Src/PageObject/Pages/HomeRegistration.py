import sys
from selenium.webdriver.common.by import By
from Src.PageObject.Locators import Locator

sys.path.append(sys.path[0] + "/....")


class CreateAcc(object):
    def __init__(self, driver):
        self.driver = driver
        self.create_account_btn = driver.find_element(By.XPATH, Locator.create_new_account)

    def get_create_account_btn(self):
        return self.create_account_btn
