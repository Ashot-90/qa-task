from typing import List
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from pages.catalog.catalog_locators import CatalogPageLocators
from pages.common.common import CommonPage


class CatalogPage(CommonPage):

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.locators = CatalogPageLocators(self.driver)
        super().load_page(self.locators.get_url)

    def __get_all_brand_filtered_dropdown(self) -> List[WebElement]:
        return self.locators.get_filtered_list

    def filter_by_brand(self, brand: str) -> None:
        self.locators.get_brand_dropwdown_button.click()
        field = self.locators.get_brand_input
        field.clear()
        field.send_keys(brand)

    def get_from_value(self) -> str:
        return super().truncate_price_value(self.locators.get_price_from_field.get_attribute('value'))

    def get_to_value(self) -> str:
        return super().truncate_price_value(self.locators.get_price_to_field.get_attribute('value'))

    def filter_by_price(self, from_price: int, to_price: int) -> None:
        self.locators.get_price_dropwdown_button.click()
        from_price_field = self.locators.get_price_from_field
        from_price_field.clear()
        from_price_field.send_keys(from_price)

        to_price_field = self.locators.get_price_to_field
        to_price_field.clear()
        to_price_field.send_keys(to_price)
        to_price_field.send_keys(Keys.ENTER)

    def click_on_catalogue_woman_shoes_heels_highheels(self) -> None:
        self.locators.get_catalog_dropwdown_button.click()
        self.locators.get_catalog_woman_button.click()
        self.locators.get_catalog_woman_shoes_button.click()
        self.locators.get_catalog_woman_shoes_heels_button.click()
        self.locators.get_catalog_woman_shoes_heels_highheels_button.click()

    def click_on_nike(self) -> None:
        self.locators.get_nike_check_box.click()

    def get_all_brand_names(self) -> List[str]:
        super().wait_for_grid_to_be_updated(self.locators)
        return [brand.text for brand in self.locators.get_all_brands if brand.text != '']

    def get_all_price_values(self) -> List[float]:
        super().wait_for_grid_to_be_updated(self.locators)
        return super().truncate_all_price_values(self.locators)

    def get_catalogue_filtered_hrefs(self) -> List[str]:
        super().wait_for_grid_to_be_updated(self.locators)
        return [element.get_attribute('href') for element in self.locators.get_all_hrefs]

    def get_filtered_brands_dropdown(self) -> List[str]:
        super().wait_to_be_updated(function=self.__get_all_brand_filtered_dropdown)
        return [menu_item.text for menu_item in self.__get_all_brand_filtered_dropdown()]
