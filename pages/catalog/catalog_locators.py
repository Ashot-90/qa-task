from selenium.webdriver.common.by import By
from pages.common import Common
from pages.common_locators import CommonPageLocators


class CatalogPageLocators(CommonPageLocators):
    if Common.portal == 'DE':
        URL = "https://www.vinted.de/catalog"
        SEARCH_HREF = '/damen/schuhe/absatzschuhe/high-heels-and-pumps/'
    elif Common.portal == 'UK':
        URL = "https://www.vinted.co.uk/catalog"
        SEARCH_HREF = '/women/shoes/heels/high-heels/'
    BRAND_DROPDOWN_BUTTON = (By.XPATH, "//div[3]/div/div/div/div[4]/div/button")
    PRICE_DROPDOWN_BUTTON = (By.XPATH, "//div[3]/div/div/div/div[5]/div/button")
    CATALOGUE_DROPDOWN_BUTTON = (By.XPATH, "//div[3]/div/div/div/div[1]/div/button")
    CATALOGUE_WOMAN = (By.XPATH, "//div[3]/div/div/div/div[1]/div/div/div/div/div/ul/li[1]/div/div[2]/div/span")
    CATALOGUE_WOMAN_SHOES = (By.XPATH, "//div[3]/div/div/div/div[1]/div/div/div/div/div[3]/ul/li[3]/div/div[2]/div/span")
    CATALOGUE_WOMAN_SHOES_HEELS = (By.XPATH, "//div[3]/div/div/div/div[1]/div/div/div/div/div[3]/ul/li[3]/div/div/div")
    CATALOGUE_WOMAN_SHOES_HEELS_HIGHHEELS = (By.XPATH, "//div[3]/div/div/div/div[1]/div/div/div/div/div[3]/ul/li[2]/div/div[2]/label")
    PRICE_FROM = (By.ID, "price_from")
    PRICE_TO = (By.ID, "price_to")
    BRAND_INPUT = (By.ID, "brand_keyword")
    FILTERED_LIST = (By.XPATH, "//div[3]/div/div/div/div[4]/div/div/div/div/div/ul/li")
    NIKE_CHECK_BOX = (By.XPATH, '//div[3]/div/div/div/div[4]/div/div/div/div/div/ul/li[1]/div/div[2]/label')
    ALL_BRANDS = (By.XPATH, './/*//div/div/div/div[3]/div/div/div[2]/div[1]/div/div/div/div[2]/span')
    ALL_PRICES = (By.XPATH, ".//*//div/div/div/div[3]/div/div/div[1]/div[1]/div/div/div/div[1]/span")
    ALL_HREFS = (By.XPATH, "//*[contains(@id, 'Catalog-react-component')]//div/div/div/div[2]/a")
