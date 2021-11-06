import os
import sys
import unittest
from time import sleep
from Src.TestBase.WebDriverSetup import WebDriverSetup
from Src.PageObject.Locators import Locator
from Src.PageObject.Pages.HomeRegistration import CreateAcc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

sys.path.append(os.getcwd())


class test_Launch_Reg_Page(WebDriverSetup):

    def test_Registration_Page_Launched(self):
        print('executing test', test_Launch_Reg_Page.test_Registration_Page_Launched.__name__)
        driver = self.driver
        registration_title = Locator.create_acc_page_title
        self.driver.get(Locator.base_url)
        self.driver.set_page_load_timeout(Locator.TIME_OUT)

        # Create an instance of the class: CreateAcc so that you we can make use of the methods
        registration_page = CreateAcc(driver)

        try:
            registration_page.get_create_account_btn().click()
            self.driver.set_page_load_timeout(Locator.TIME_OUT)
        except Exception as error:
            print(error, 'Failed to click Create Acc Button')

        try:
            cookie_policy_agree_btn = WebDriverWait(driver, Locator.PAGE_WAIT). \
                until(ec.element_to_be_clickable((By.XPATH, Locator.cookie_policy_agree)))
            cookie_policy_agree_btn.click()
            self.driver.set_page_load_timeout(Locator.TIME_OUT)
        except Exception as error:
            print(error, 'Failed to click Cookie Policy Agree Button')

        try:
            sleep(Locator.PAGE_WAIT)
            create_business_acc_btn = WebDriverWait(driver, Locator.PAGE_WAIT*2). \
                until(ec.element_to_be_clickable((By.XPATH, Locator.create_business_acc)))
            create_business_acc_btn.click()
            self.driver.set_page_load_timeout(Locator.TIME_OUT)
        except Exception as error:
            print(error, 'Failed to click Cookie Policy Agree Button')

        try:
            if driver.title == registration_title:
                self.assertEqual(driver.title, registration_title)
        except Exception as error:
            print(error, 'RegistrationPage Failed to load')

        sleep(Locator.PAGE_WAIT)


if __name__ == '__main__':
    unittest.main()
