from pages.member.member import MemberPage
from tests.test_base import TestBase


class TestMemberPage(TestBase):

    def setUp(self):
        super().setUp()
        self.member_page = MemberPage(driver=self.driver)

    @TestBase.wrap_test
    def test_price_sort(self):
        """
        Test for price sort from high to low
        """
        self.member_page.sort_price_high_to_low()
        prices = self.member_page.common.get_all_price_values()
        self.assertTrue(all(prices[i] >= prices[i + 1] for i in range(len(prices) - 1)),
                        msg="FAILED - '{}' Prices sorted incorrectly ".format(self._testMethodName))
