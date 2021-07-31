import unittest
from functools import wraps
from allure_commons.types import AttachmentType
from pages.common.common import Common
import allure


class TestBase(unittest.TestCase):

    def setUp(self):
        self.driver = Common.create_driver()

    def tearDown(self):
        self.driver.close()

    @staticmethod
    def wrap_test(test_function):
        @wraps(test_function)
        def wrapper(test):
            with allure.step(title=test.__doc__):
                try:
                    test.setUp()
                    test_function(test)
                    test.tearDown()
                    print("PASSED - '{}'".format(test._testMethodName))
                except Exception as ex:
                    print("FAILED - '{}'".format(test._testMethodName))
                    screenshot_path = Common.take_screenshot(driver=test.driver,
                                                             test_name=test._testMethodName)
                    allure.attach(open(file=screenshot_path,
                                       mode='rb').read(),
                                  name=test._testMethodName,
                                  attachment_type=AttachmentType.PNG)
                    raise ex
        return wrapper


if __name__ == "__main__":
    unittest.main()
