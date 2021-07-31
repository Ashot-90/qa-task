from typing import List
from pages.common.common import CommonPage
from pages.member.member_locators import MemberPageLocators


class MemberPage(CommonPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = MemberPageLocators(driver=self.driver)
        super().load_page(self.locators.url)

    def sort_price_high_to_low(self) -> None:
        self.locators.sort_dropwdown_button.click()
        self.locators.sort_price_high_to_low_button.click()

    def get_all_price_values(self) -> List[float]:
        super().wait_for_grid_to_be_updated(self.locators)
        return super().truncate_all_price_values(self.locators)
