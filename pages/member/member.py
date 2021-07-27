from typing import List
from selenium.webdriver.remote.webelement import WebElement
from pages.common import Common
from pages.member.member_locators import MemberPageLocators


class MemberPage(object):

    def __init__(self, driver):
        self.driver = driver
        self.common = Common(driver=self.driver, page_elements=MemberPageLocators)
        self.common.load_page()

    def sort_price_high_to_low(self) -> None:
        sort_flow = (MemberPageLocators.SORT_DROPDOWN_BUTTON,
                     MemberPageLocators.SORT_PRICE_HIGH_TO_LOW)
        for element in sort_flow:
            self.common.find_and_click_on_element(element=element)

    def get_all_prices(self) -> List[WebElement]:
        self.common.wait_for_grid_to_be_updated()
        return self.common.get_all_price_elements()
