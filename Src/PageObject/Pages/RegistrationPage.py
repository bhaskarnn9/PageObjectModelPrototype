import sys
from selenium.webdriver.common.by import By
from Src.PageObject.Locators import Locator

sys.path.append(sys.path[0] + "/....")


class RegistrationAcc(object):
    def __init__(self, driver):
        self.driver = driver
        self.business_name = driver.find_element(By.XPATH, Locator.business_name)
        self.company_type = driver.find_element(By.XPATH, Locator.company_type)
        self.state = driver.find_element(By.XPATH, Locator.state)
        self.first_name = driver.find_element(By.XPATH, Locator.first_name_box)
        self.middle_name = driver.find_element(By.XPATH, Locator.middle_name_box)
        self.last_name = driver.find_element(By.XPATH, Locator.last_name_box)
        self.email_address = driver.find_element(By.XPATH, Locator.email_address_box)
        self.continue_button = driver.find_element(By.XPATH, Locator.continue_button)

    def get_business_name_box(self):
        return self.business_name

    def get_company_type_box(self):
        return self.company_type

    def get_state_box(self):
        return self.state

    def get_first_name_box(self):
        return self.first_name

    def get_middle_name_box(self):
        return self.middle_name

    def get_last_name_box(self):
        return self.last_name

    def get_email_address_box(self):
        return self.email_address

    def get_continue_button(self):
        return self.continue_button
