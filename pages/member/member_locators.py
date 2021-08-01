from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from pages.common import common_config
from pages.common.common_locators import CommonPageLocators


class MemberPageLocators(CommonPageLocators):
    __URL = common_config.CATALOG_MEMBER['url']
    __SORT_DROPDOWN_BUTTON = (By.XPATH, "//*[contains(@id, 'Profile-react-component')]//div/div/div[3]/div[3]/div/div[2]/div[2]/div[2]/div/button")
    __SORT_PRICE_HIGH_TO_LOW = (By.XPATH, '//div/div/div[3]/div[3]/div/div[2]/div[2]/div[2]/div/div/div/div/ul/li[2]')
    #__SORT_PRICE_HIGH_TO_LOW = (By.XPATH, "//input[@name='sort_by'][@type='radio'][@value='price_high_to_low']")
    __ALL_PRICES = (By.XPATH, "//*[contains(@id, 'Profile-react-component')]//div/div/div/div[2]/div/div/div[1]/div[1]/div/div/div/div[1]/span")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    url = property(fget=lambda self: self.__URL)
    all_prices = property(fget=lambda self: self.find_elements(self.__ALL_PRICES))
    sort_dropwdown_button = property(fget=lambda self: self.find_element(self.__SORT_DROPDOWN_BUTTON))
    sort_price_high_to_low_button = property(fget=lambda self: self.find_element(self.__SORT_PRICE_HIGH_TO_LOW))
