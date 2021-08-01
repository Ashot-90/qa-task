from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
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

    url = property(fget=lambda self: self.__URL)
    search_href = property(fget=lambda self: self.__SEARCH_HREF)
    all_prices = property(fget=lambda self: self.find_elements(self.__ALL_PRICES))
    brand_dropdown_button = property(fget=lambda self: self.find_element(self.__BRAND_DROPDOWN_BUTTON))
    price_dropdown_button = property(fget=lambda self: self.find_element(self.__PRICE_DROPDOWN_BUTTON))
    catalog_dropdown_button = property(fget=lambda self: self.find_element(self.__CATALOGUE_DROPDOWN_BUTTON))
    catalog_woman_button = property(fget=lambda self: self.find_element(self.__CATALOGUE_WOMAN))
    catalog_woman_shoes_button = property(fget=lambda self: self.find_element(self.__CATALOGUE_WOMAN_SHOES))
    catalog_woman_shoes_heels_button = property(fget=lambda self: self.find_element(self.__CATALOGUE_WOMAN_SHOES_HEELS))
    catalog_woman_shoes_heels_highheels_button = property(fget=lambda self: self.find_element(self.__CATALOGUE_WOMAN_SHOES_HEELS_HIGHHEELS))
    price_from_field = property(fget=lambda self: self.find_element(self.__PRICE_FROM))
    price_to_field = property(fget=lambda self: self.find_element(self.__PRICE_TO))
    brand_input = property(fget=lambda self: self.find_element(self.__BRAND_INPUT))
    filtered_list = property(fget=lambda self: self.find_elements(self.__FILTERED_LIST))
    nike_check_box = property(fget=lambda self: self.find_element(self.__NIKE_CHECK_BOX))
    all_brands = property(fget=lambda self: self.find_elements(self.__ALL_BRANDS))
    all_hrefs = property(fget=lambda self: self.find_elements(self.__ALL_HREFS))
