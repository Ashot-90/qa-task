from typing import Tuple, List
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from pages.common import common_config
from pages.common.common_locators import CommonPageLocators


class CatalogPageLocators(CommonPageLocators):
    __URL = common_config.CATALOG_CONFIG['url']
    __SEARCH_HREF = common_config.CATALOG_CONFIG['search_href']
    __BRAND_DROPDOWN_BUTTON = (By.XPATH, "//*[contains(@id, 'Catalog-react-component')]//div[3]/div/div/div/div[4]/div/button")
    __PRICE_DROPDOWN_BUTTON = (By.XPATH, "//*[contains(@id, 'Catalog-react-component')]//div[3]/div/div/div/div[5]/div/button")
    __CATALOGUE_DROPDOWN_BUTTON = (By.XPATH, "//*[contains(@id, 'Catalog-react-component')]//div[3]/div/div/div/div[1]/div/button")
    __CATALOGUE_WOMAN = (By.XPATH, "//*[contains(@id, 'Catalog-react-component')]//div[3]/div/div/div/div[1]/div/div/div/div/div/ul/li[1]")
    __CATALOGUE_WOMAN_SHOES = (By.XPATH, "//*[contains(@id, 'Catalog-react-component')]//div[3]/div/div/div/div[1]/div/div/div/div/div[3]/ul/li[3]")
    __CATALOGUE_WOMAN_SHOES_HEELS = (By.XPATH, "//*[contains(@id, 'Catalog-react-component')]//div[3]/div/div/div/div[1]/div/div/div/div/div[3]/ul/li[3]")
    __CATALOGUE_WOMAN_SHOES_HEELS_HIGHHEELS = (By.XPATH, "//*[contains(@id, 'Catalog-react-component')]//div[3]/div/div/div/div[1]/div/div/div/div/div[3]/ul/li[2]")
    __PRICE_FROM = (By.ID, "price_from")
    __PRICE_TO = (By.ID, "price_to")
    __BRAND_INPUT = (By.ID, "brand_keyword")
    __FILTERED_LIST = (By.XPATH, "//*[contains(@id, 'Catalog-react-component')]//div[3]/div/div/div/div[4]/div/div/div/div/div/ul/li")
    __NIKE_CHECK_BOX = (By.XPATH, "//span[contains(text(), 'Nike')]")
    __ALL_BRANDS = (By.XPATH, "//*[contains(@id, 'Catalog-react-component')]//*//div/div/div/div[3]/div/div/div[2]/div[1]/div/div/div/div[2]/span")
    __ALL_PRICES = (By.XPATH, "//*[contains(@id, 'Catalog-react-component')]//*//div/div/div/div[3]/div/div/div[1]/div[1]/div/div/div/div[1]/span")
    __ALL_HREFS = (By.XPATH, "//*[contains(@id, 'Catalog-react-component')]//div/div/div/div[2]/a")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def url(self):
        return self.__URL

    @url.getter
    def get_url(self):
        return self.__URL

    @property
    def search_href(self):
        return self.__SEARCH_HREF

    @search_href.getter
    def get_search_href(self):
        return self.__SEARCH_HREF

    @property
    def all_prices(self):
        return self.__ALL_PRICES

    @all_prices.getter
    def get_all_prices(self) -> List[WebElement]:
        return self.driver.find_elements(*self.__ALL_PRICES)

    @property
    def brand_dropwdown_button(self) -> Tuple:
        return self.__BRAND_DROPDOWN_BUTTON

    @brand_dropwdown_button.getter
    def get_brand_dropwdown_button(self) -> WebElement:
        return self.driver.find_element(*self.__BRAND_DROPDOWN_BUTTON)

    @property
    def price_dropwdown_button(self) -> Tuple:
        return self.__PRICE_DROPDOWN_BUTTON

    @price_dropwdown_button.getter
    def get_price_dropwdown_button(self) -> WebElement:
        return self.driver.find_element(*self.__PRICE_DROPDOWN_BUTTON)

    @property
    def catalog_dropwdown_button(self) -> Tuple:
        return self.__CATALOGUE_DROPDOWN_BUTTON

    @catalog_dropwdown_button.getter
    def get_catalog_dropwdown_button(self) -> WebElement:
        return self.driver.find_element(*self.__CATALOGUE_DROPDOWN_BUTTON)

    @property
    def catalog_woman_button(self) -> Tuple:
        return self.__CATALOGUE_WOMAN

    @catalog_woman_button.getter
    def get_catalog_woman_button(self) -> WebElement:
        return self.driver.find_element(*self.__CATALOGUE_WOMAN)

    @property
    def catalog_woman_shoes_button(self) -> Tuple:
        return self.__CATALOGUE_WOMAN_SHOES

    @catalog_woman_shoes_button.getter
    def get_catalog_woman_shoes_button(self) -> WebElement:
        return self.driver.find_element(*self.__CATALOGUE_WOMAN_SHOES)

    @property
    def catalog_woman_shoes_heels_button(self) -> Tuple:
        return self.__CATALOGUE_WOMAN_SHOES_HEELS

    @catalog_woman_shoes_heels_button.getter
    def get_catalog_woman_shoes_heels_button(self) -> WebElement:
        return self.driver.find_element(*self.__CATALOGUE_WOMAN_SHOES_HEELS)

    @property
    def catalog_woman_shoes_heels_highheels_button(self) -> Tuple:
        return self.__CATALOGUE_WOMAN_SHOES_HEELS_HIGHHEELS

    @catalog_woman_shoes_heels_highheels_button.getter
    def get_catalog_woman_shoes_heels_highheels_button(self) -> WebElement:
        return self.driver.find_element(*self.__CATALOGUE_WOMAN_SHOES_HEELS_HIGHHEELS)

    @property
    def price_from_field(self) -> Tuple:
        return self.__PRICE_FROM

    @price_from_field.getter
    def get_price_from_field(self) -> WebElement:
        return self.driver.find_element(*self.__PRICE_FROM)

    @property
    def price_to_field(self) -> Tuple:
        return self.__PRICE_TO

    @price_to_field.getter
    def get_price_to_field(self) -> WebElement:
        return self.driver.find_element(*self.__PRICE_TO)

    @property
    def brand_input(self) -> Tuple:
        return self.__BRAND_INPUT

    @brand_input.getter
    def get_brand_input(self) -> WebElement:
        return self.driver.find_element(*self.__BRAND_INPUT)

    @property
    def filtered_list(self) -> Tuple:
        return self.__FILTERED_LIST

    @filtered_list.getter
    def get_filtered_list(self) -> List[WebElement]:
        return self.driver.find_elements(*self.__FILTERED_LIST)

    @property
    def nike_check_box(self) -> Tuple:
        return self.__NIKE_CHECK_BOX

    @nike_check_box.getter
    def get_nike_check_box(self) -> WebElement:
        return self.driver.find_element(*self.__NIKE_CHECK_BOX)

    @property
    def all_brands(self) -> Tuple:
        return self.__ALL_BRANDS

    @all_brands.getter
    def get_all_brands(self):
        return self.driver.find_elements(*self.__ALL_BRANDS)

    @property
    def all_hrefs(self) -> Tuple:
        return self.__ALL_HREFS

    @all_hrefs.getter
    def get_all_hrefs(self) -> List[WebElement]:
        return self.driver.find_elements(*self.__ALL_HREFS)
