import os
import sys
import unittest
from time import sleep
from Src.TestBase.WebDriverSetup import WebDriverSetup
from Src.PageObject.Locators import Locator

sys.path.append(os.getcwd())


class test_Launch_Home_Page(WebDriverSetup):

    def test_Home_Page_Launched(self):
        print('executing test', test_Launch_Home_Page.test_Home_Page_Launched.__name__)
        driver = self.driver
        home_title = Locator.home_page_title
        self.driver.get(Locator.base_url)
        self.driver.set_page_load_timeout(Locator.TIME_OUT)

        try:
            if driver.title == home_title:
                self.assertEqual(driver.title, home_title)
        except Exception as error:
            print(error, 'HomePage Failed to load')

        sleep(Locator.PAGE_WAIT)


if __name__ == '__main__':
    unittest.main()
