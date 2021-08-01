from typing import Tuple, List
from selenium.webdriver.support import expected_conditions as exp_cond
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from pages.base.base import BasePage
from selenium.webdriver.support.wait import WebDriverWait


class CommonPageLocators(BasePage):
    __CLOSE_QUESTIONNAIRE_BUTTON = (By.XPATH, "/html/body/div[13]/div/div/div/div[1]/div/div[3]/button")
    __QUESTIONNAIRE = (By.XPATH, "/html/body/div[13]/div/div/div")
    __QUESTIONNAIRE_TEXT = 'Where do you live?'
    __ACCEPT_ALL_COOKIES = (By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
    __COOKIES_GROUP_BUTTON = (By.XPATH, '//*[@id="onetrust-button-group"]')
    __GRID = (By.CLASS_NAME, "feed-grid")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    questionnaire_text = property(fget=lambda self: self.__QUESTIONNAIRE_TEXT)
    close_questionnaire_button = property(fget=lambda self: self.find_element(self.__CLOSE_QUESTIONNAIRE_BUTTON))
    questionnaire = property(fget=lambda self: self.get_questionnaire())
    accept_all_cookies_button = property(fget=lambda self: self.get_accept_all_cookies_button())
    grid_widget = property(fget=lambda self: self.get_grid_widget())

    def get_questionnaire(self) -> WebElement:
        WebDriverWait(self.driver, timeout=10).until(
            exp_cond.text_to_be_present_in_element(self.__QUESTIONNAIRE,
                                                   self.__QUESTIONNAIRE_TEXT))
        return self.find_element(self.__QUESTIONNAIRE)

    def get_accept_all_cookies_button(self) -> WebElement:
        WebDriverWait(self.driver, 30).until(
            exp_cond.element_to_be_clickable(self.__ACCEPT_ALL_COOKIES))
        return self.find_element(self.__ACCEPT_ALL_COOKIES)

    def get_grid_widget(self) -> WebElement:
        WebDriverWait(self.driver, 30).until(
            exp_cond.presence_of_element_located(self.__GRID))
        return self.find_element(self.__GRID)

    def find_element(self, locator: Tuple) -> WebElement:
        return self.driver.find_element(*locator)

    def find_elements(self, locator: Tuple) -> List[WebElement]:
        return self.driver.find_elements(*locator)
