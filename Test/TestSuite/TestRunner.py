import os
import sys

from HtmlTestRunner import HTMLTestRunner
from get_project_root import root_path

sys.path.append(sys.path[0] + "/....")
sys.path.append(os.getcwd())

from unittest import TestLoader, TestSuite
from Test.Scripts.test_Launch_Home_Page import test_Launch_Home_Page
from Test.Scripts.test_launch_registration_page import test_Launch_Reg_Page
from Test.Scripts.test_institution_registration_page import test_Institution_Reg_Page

if __name__ == '__main__':
    launch_test = TestLoader().loadTestsFromTestCase(test_Launch_Home_Page)
    launch_test2 = TestLoader().loadTestsFromTestCase(test_Launch_Reg_Page)
    launch_test3 = TestLoader().loadTestsFromTestCase(test_Institution_Reg_Page)

    # Test Suite is used since there are multiple test cases
    suite = TestSuite([launch_test, launch_test2, launch_test3])

    test_runner = HTMLTestRunner(output=root_path(ignore_cwd=False) + '/Results', combine_reports=True,
                                 report_name="MyReportTest", add_timestamp=True)

    test_runner.run(suite)
