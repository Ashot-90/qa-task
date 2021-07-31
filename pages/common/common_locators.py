from typing import Tuple
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
    __REJECT_ALL_COOKIES = (By.XPATH, '//*[@id="onetrust-reject-all-handler"]')
    __MANAGE_ALL_COOKIES = (By.XPATH, '//*[@id="onetrust-pc-btn-handler"]')
    __COOKIES_GROUP_BUTTON = (By.XPATH, '//*[@id="onetrust-button-group"]')
    __GRID = (By.CLASS_NAME, "feed-grid")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def questionnaire_text(self) -> str:
        return self.__QUESTIONNAIRE_TEXT

    @questionnaire_text.getter
    def get_questionnaire_text(self) -> str:
        return self.__QUESTIONNAIRE_TEXT

    @property
    def close_questionnaire_button(self) -> Tuple:
        return self.__CLOSE_QUESTIONNAIRE_BUTTON

    @close_questionnaire_button.getter
    def get_close_questionnaire_button(self) -> WebElement:
        return self.driver.find_element(*self.__CLOSE_QUESTIONNAIRE_BUTTON)

    @property
    def questionnaire(self) -> Tuple:
        return self.__QUESTIONNAIRE

    @questionnaire.getter
    def get_questionnaire(self) -> WebElement:
        WebDriverWait(self.driver, timeout=10).until(
            exp_cond.text_to_be_present_in_element(self.__QUESTIONNAIRE,
                                                   self.__QUESTIONNAIRE_TEXT))
        return self.driver.find_element(*self.__QUESTIONNAIRE)

    @property
    def accept_all_cookies_button(self) -> Tuple:
        return self.__ACCEPT_ALL_COOKIES

    @accept_all_cookies_button.getter
    def get_accept_all_cookies_button(self) -> WebElement:
        WebDriverWait(self.driver, 30).until(
            exp_cond.element_to_be_clickable(self.__ACCEPT_ALL_COOKIES))
        return self.driver.find_element(*self.__ACCEPT_ALL_COOKIES)

    @property
    def reject_all_cookies_button(self) -> Tuple:
        return self.__REJECT_ALL_COOKIES

    @reject_all_cookies_button.getter
    def get_reject_all_cookies_button(self) -> WebElement:
        return self.driver.find_element(*self.__REJECT_ALL_COOKIES)

    @property
    def manage_all_cookies_button(self) -> Tuple:
        return self.__MANAGE_ALL_COOKIES

    @manage_all_cookies_button.getter
    def get_manage_all_cookies_button(self) -> WebElement:
        return self.driver.find_element(*self.__MANAGE_ALL_COOKIES)

    @property
    def cookies_group_buttons(self) -> Tuple:
        return self.__COOKIES_GROUP_BUTTON

    @cookies_group_buttons.getter
    def get_cookies_group_buttons(self) -> WebElement:
        return self.driver.find_element(*self.__COOKIES_GROUP_BUTTON)

    @property
    def grid_widget(self) -> Tuple:
        return self.__GRID

    @cookies_group_buttons.getter
    def get_grid_widget(self) -> WebElement:
        WebDriverWait(self.driver, 30).until(
            exp_cond.presence_of_element_located(self.__GRID))
        return self.driver.find_element(*self.__GRID)
