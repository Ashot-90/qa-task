from pages.member.member import MemberPage
from tests.test_base import TestBase


class TestMemberPage(TestBase):

    _report = []

    def setUp(self):
        super().setUp()
        self.member_page = MemberPage(driver=self.driver)

    @TestBase.wrap_test
    def test_sort_price_high_to_low(self):
        """
        Test for price sort from high to low
        """
        self.member_page.sort_price_high_to_low()
        prices = list()
        for price in self.member_page.common.get_all_price_values():
            text = str(price.text)
            if '£' in text or '€' in text:
                prices.append(self.member_page.common.truncate_price_value(text))
        self.assertTrue(all(float(prices[i]) >= float(prices[i + 1]) for i in range(len(prices) - 1)),
                        msg="FAILED - '{}'".format(self._testMethodName))
