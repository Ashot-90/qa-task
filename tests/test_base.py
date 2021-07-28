import unittest
from functools import wraps
from pages.common.common import Common


class TestBase(unittest.TestCase):

    _report = None
    _separator_line = "###################################################"

    @classmethod
    def setUpClass(cls):
        cls._report.append("Test Run Report -> Class '{}'".format(cls.__name__))
        cls._report.append(TestBase._separator_line)

    @classmethod
    def tearDownClass(cls):
        cls._report.append(TestBase._separator_line)
        print('\n'.join(cls._report))

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
                test._report.append("PASSED - '{}'".format(test._testMethodName))
            except Exception as ex:
                test._report.append("FAILED - '{}'".format(test._testMethodName))
                Common.take_screenshot(driver=test.driver,
                                       test_name=test._testMethodName)
                raise ex
        return wrapper


if __name__ == "__main__":
    unittest.main()
