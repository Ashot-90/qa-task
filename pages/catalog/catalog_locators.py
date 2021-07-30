from selenium.webdriver.common.by import By
from pages.common import common_config
from pages.common.common_locators import CommonPageLocators


class CatalogPageLocators(CommonPageLocators):
    URL = common_config.CATALOG_CONFIG['url']
    SEARCH_HREF = common_config.CATALOG_CONFIG['search_href']
    BRAND_DROPDOWN_BUTTON = (By.XPATH, "//*[contains(@id, 'Catalog-react-component')]//div[3]/div/div/div/div[4]/div/button")
    PRICE_DROPDOWN_BUTTON = (By.XPATH, "//*[contains(@id, 'Catalog-react-component')]//div[3]/div/div/div/div[5]/div/button")
    CATALOGUE_DROPDOWN_BUTTON = (By.XPATH, "//*[contains(@id, 'Catalog-react-component')]//div[3]/div/div/div/div[1]/div/button")
    CATALOGUE_WOMAN = (By.XPATH, "//*[contains(@id, 'Catalog-react-component')]//div[3]/div/div/div/div[1]/div/div/div/div/div/ul/li[1]")
    CATALOGUE_WOMAN_SHOES = (By.XPATH, "//*[contains(@id, 'Catalog-react-component')]//div[3]/div/div/div/div[1]/div/div/div/div/div[3]/ul/li[3]")
    CATALOGUE_WOMAN_SHOES_HEELS = (By.XPATH, "//*[contains(@id, 'Catalog-react-component')]//div[3]/div/div/div/div[1]/div/div/div/div/div[3]/ul/li[3]")
    CATALOGUE_WOMAN_SHOES_HEELS_HIGHHEELS = (By.XPATH, "//*[contains(@id, 'Catalog-react-component')]//div[3]/div/div/div/div[1]/div/div/div/div/div[3]/ul/li[2]")
    PRICE_FROM = (By.ID, "price_from")
    PRICE_TO = (By.ID, "price_to")
    BRAND_INPUT = (By.ID, "brand_keyword")
    FILTERED_LIST = (By.XPATH, "//*[contains(@id, 'Catalog-react-component')]//div[3]/div/div/div/div[4]/div/div/div/div/div/ul/li")
    NIKE_CHECK_BOX = (By.XPATH, "//span[contains(text(), 'Nike')]")
    ALL_BRANDS = (By.XPATH, "//*[contains(@id, 'Catalog-react-component')]//*//div/div/div/div[3]/div/div/div[2]/div[1]/div/div/div/div[2]/span")
    ALL_PRICES = (By.XPATH, "//*[contains(@id, 'Catalog-react-component')]//*//div/div/div/div[3]/div/div/div[1]/div[1]/div/div/div/div[1]/span")
    ALL_HREFS = (By.XPATH, "//*[contains(@id, 'Catalog-react-component')]//div/div/div/div[2]/a")
