from typing import List
from selenium.webdriver.android.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from pages.catalog.catalog_locators import CatalogPageLocators
from pages.common.common import Common


class CatalogPage(object):

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.common = Common(driver=self.driver, page_elements=CatalogPageLocators)
        self.common.load_page()

    def __get_filter_by_price_from_element(self) -> WebElement:
        return self.driver.find_element(*CatalogPageLocators.PRICE_FROM)

    def __get_filter_by_price_to_element(self) -> WebElement:
        return self.driver.find_element(*CatalogPageLocators.PRICE_TO)

    def __get_all_brand_filtered_dropdown(self) -> List[WebElement]:
        return self.driver.find_elements(*CatalogPageLocators.FILTERED_LIST)

    def filter_by_brand(self, brand: str) -> None:
        self.common.find_and_click_on_element(element=CatalogPageLocators.BRAND_DROPDOWN_BUTTON)
        field = self.driver.find_element(*CatalogPageLocators.BRAND_INPUT)
        field.clear()
        field.send_keys(brand)

    def get_from_value(self) -> str:
        return self.common.truncate_price_value(self.__get_filter_by_price_from_element().get_attribute('value'))

    def get_to_value(self) -> str:
        return self.common.truncate_price_value(self.__get_filter_by_price_to_element().get_attribute('value'))

    def filter_by_price(self, from_price: int, to_price: int) -> None:
        self.common.find_and_click_on_element(element=CatalogPageLocators.PRICE_DROPDOWN_BUTTON)
        from_price_field = self.__get_filter_by_price_from_element()
        from_price_field.clear()
        from_price_field.send_keys(from_price)

        to_price_field = self.__get_filter_by_price_to_element()
        to_price_field.clear()
        to_price_field.send_keys(to_price)
        to_price_field.send_keys(Keys.ENTER)

    def click_on_catalogue_woman_shoes_heels_highheels(self) -> None:
        locator_flow = (CatalogPageLocators.CATALOGUE_DROPDOWN_BUTTON,
                        CatalogPageLocators.CATALOGUE_WOMAN,
                        CatalogPageLocators.CATALOGUE_WOMAN_SHOES,
                        CatalogPageLocators.CATALOGUE_WOMAN_SHOES_HEELS,
                        CatalogPageLocators.CATALOGUE_WOMAN_SHOES_HEELS_HIGHHEELS)
        for locator in locator_flow:
            self.common.find_and_click_on_element(element=locator)

    def click_on_nike(self) -> None:
        self.common.find_and_click_on_element(element=CatalogPageLocators.NIKE_CHECK_BOX)

    def get_all_brand_names(self) -> List[str]:
        self.common.wait_for_grid_to_be_updated()
        return [brand.text for brand in self.driver.find_elements(*CatalogPageLocators.ALL_BRANDS) if brand.text != '']

    def get_catalogue_filtered_hrefs(self) -> List[str]:
        self.common.wait_for_grid_to_be_updated()
        return [element.get_attribute('href') for element in self.driver.find_elements(*CatalogPageLocators.ALL_HREFS)]

    def get_filtered_brands_dropdown(self) -> List[str]:
        self.common.wait_to_be_updated(function=self.__get_all_brand_filtered_dropdown)
        return [menu_item.text for menu_item in self.__get_all_brand_filtered_dropdown()]
