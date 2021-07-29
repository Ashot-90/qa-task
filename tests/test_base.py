import unittest
from functools import wraps
from pages.common.common import Common


class TestBase(unittest.TestCase):

    def setUp(self):
        self.driver = Common.create_driver()

    def tearDown(self):
        self.driver.close()

    @staticmethod
    def wrap_test(test_function):
        @wraps(test_function)
        def wrapper(test):
            try:
                test_function(test)
            except Exception as ex:
                Common.take_screenshot(driver=test.driver,
                                       test_name=test._testMethodName)
                raise ex
        return wrapper


if __name__ == "__main__":
    unittest.main()
