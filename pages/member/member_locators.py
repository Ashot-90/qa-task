from selenium.webdriver.common.by import By
from pages.common_locators import CommonPageLocators


class MemberPageLocators(CommonPageLocators):
    URL = CommonPageLocators.CATALOG_MEMBER['url']
    SORT_DROPDOWN_BUTTON = (By.XPATH, "//*[contains(@id, 'Profile-react-component')]//div/div/div[3]/div[3]/div/div[2]/div[2]/div[2]/div/button")
    SORT_PRICE_HIGH_TO_LOW = (By.XPATH, '//div/div/div[3]/div[3]/div/div[2]/div[2]/div[2]/div/div/div/div/ul/li[2]')
    #SORT_PRICE_HIGH_TO_LOW = (By.XPATH, "//input[@name='sort_by'][@type='radio'][@value='price_high_to_low']")
    ALL_PRICES = (By.XPATH, "//*[contains(@id, 'Profile-react-component')]//div/div/div/div[2]/div/div/div[1]/div[1]/div/div/div/div[1]/span")
