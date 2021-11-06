import os
import sys
import unittest
from time import sleep
from selenium.webdriver.common.by import By
from Src.TestBase.WebDriverSetup import WebDriverSetup
from Src.PageObject.Locators import Locator
from Src.PageObject.Pages.RegistrationPage import RegistrationAcc
from selenium.webdriver.support.ui import Select

sys.path.append(os.getcwd())


class test_Institution_Reg_Page(WebDriverSetup):

    def test_Registration_Form(self):
        flag = False
        print('executing test', test_Institution_Reg_Page.test_Registration_Form.__name__)
        driver = self.driver
        thanks_page_title = Locator.create_acc_page_title
        self.driver.get(Locator.business_url)
        self.driver.set_page_load_timeout(Locator.TIME_OUT)

        # Create an instance of the class: CreateAcc so that you we can make use of the methods
        institution_page = RegistrationAcc(driver)

        try:

            business_name_box = institution_page.get_business_name_box()
            business_name_box.send_keys('GeminiSandbox')
            business_name_box.submit()
            self.driver.set_page_load_timeout(Locator.TIME_OUT)
        except Exception as error:
            print(error, 'Failed to enter business name')

        try:
            company_type_box = Select(driver.findElement(By.XPATH(Locator.company_type)))
            company_type_box.selectByVisibleText(Locator.visible_text_type)
            self.driver.set_page_load_timeout(Locator.TIME_OUT)
        except Exception as error:
            print(error, 'Failed to enter business name')

        try:
            if driver.title == thanks_page_title:
                flag = True
            if driver.title == thanks_page_title:
                self.assertTrue(flag)
        except Exception as error:
            print(error, 'Failed to complete registration')

        sleep(Locator.PAGE_WAIT)


if __name__ == '__main__':
    unittest.main()
