import unittest
from pages.common import Common
from pages.member.member import MemberPage


class TestMemberPage(unittest.TestCase):

    def setUp(self):
        self.driver = Common.create_chrome_driver()
        self.member_page = MemberPage(driver=self.driver)

    def tearDown(self):
        self.driver.close()

    @Common.test_wrapper
    def test_sort_price_high_to_low(self):
        """
        Test for price sort from high to low
        """
        self.member_page.sort_price_high_to_low()
        prices = list()
        for price in self.member_page.get_all_prices():
            text = str(price.text)
            if '£' in text or '€' in text:
                prices.append(self.member_page.common.truncate_price_value(text))
        self.assertTrue(all(float(prices[i]) >= float(prices[i + 1]) for i in range(len(prices) - 1)),
                        msg="FAILED - '{}'".format(self._testMethodName))


if __name__ == "__main__":
    unittest.main()
