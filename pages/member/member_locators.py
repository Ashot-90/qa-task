from selenium.webdriver.common.by import By
from pages.common import Common
from pages.common_locators import CommonPageLocators


class MemberPageLocators(CommonPageLocators):
    if Common.portal == 'DE':
        URL = "https://www.vinted.de/member/64679137"
        SEARCH_HREF = '/damen/schuhe/absatzschuhe/high-heels-and-pumps/'
    elif Common.portal == 'UK':
        URL = "https://www.vinted.co.uk/member/64678795"
        SEARCH_HREF = '/women/shoes/heels/high-heels/'
    SORT_DROPDOWN_BUTTON = (By.XPATH, "//*[contains(@id, 'Profile-react-component')]//div/div/div[3]/div[3]/div/div[2]/div[2]/div[2]/div/button")
    SORT_PRICE_HIGH_TO_LOW = (By.XPATH, '//div/div/div[3]/div[3]/div/div[2]/div[2]/div[2]/div/div/div/div/ul/li[2]')
    #SORT_PRICE_HIGH_TO_LOW = (By.XPATH, "//input[@name='sort_by'][@type='radio'][@value='price_high_to_low']")
    ALL_PRICES = (By.XPATH, "//*[contains(@id, 'Profile-react-component')]//div/div/div/div[2]/div/div/div[1]/div[1]/div/div/div/div[1]/span")
