from typing import Type, List, Tuple
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.android.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.common import common_config
from pages.common.common_locators import CommonPageLocators
from datetime import datetime
from selenium import webdriver
import os


class Common(object):
    __chrome_driver_path = common_config.COMMON_CONFIG['chrome_driver_path']
    __ff_driver_path = common_config.COMMON_CONFIG['ff_driver_path']

    def __init__(self, driver: WebDriver, page_elements: Type[CommonPageLocators]):
        self.driver = driver
        self.page_elements = page_elements

    def __close_questionnaire(self) -> None:
        wait = WebDriverWait(self.driver, timeout=10)
        load_completed = wait.until(
            EC.text_to_be_present_in_element(CommonPageLocators.QUESTIONNAIRE,
                                             CommonPageLocators.QUESTIONNAIRE_TEXT))
        if load_completed:
            self.find_and_click_on_element(element=CommonPageLocators.CLOSE_QUESTIONNAIRE_BUTTON)

    def __accept_all_cookies(self) -> None:
        element = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(CommonPageLocators.ACCEPT_ALL_COOKIES))
        self.wait_for_stop_element_move(element)
        self.find_and_click_on_element(element=CommonPageLocators.ACCEPT_ALL_COOKIES)

    def load_page(self) -> None:
        url = self.page_elements.URL
        self.driver.get(url)
        self.driver.maximize_window()
        try:
            wait = WebDriverWait(self.driver, timeout=10)
            self.__accept_all_cookies()
            # For .DE no questionnaire
            if common_config.PORTAL != 'DE':
                self.__close_questionnaire()
            wait.until(
                EC.presence_of_element_located(self.page_elements.GRID))
        except TimeoutException:
            Common.take_screenshot(driver=self.driver,
                                   test_name='load_page')
            raise TimeoutException("Error: Timed out waiting for page load")

    def wait_for_stop_element_move(self, element: WebElement) -> None:
        attempt = 1
        timeout_after = 100
        previous_location = {}
        while True:
            current_location = dict(element.location)
            if current_location == previous_location:
                break
            previous_location = current_location
            self.driver.implicitly_wait(1)
            attempt += 1
            if attempt == timeout_after:
                raise TimeoutException(msg="Error: Timed out waiting for element location change")

    def get_all_price_elements(self) -> List[WebElement]:
        return self.driver.find_elements(*self.page_elements.ALL_PRICES)

    def get_all_price_values(self) -> List[float]:
        self.wait_for_grid_to_be_updated()
        return [float(self.truncate_price_value(price_element.text)) for price_element in self.get_all_price_elements()
                if '£' in price_element.text or '€' in price_element.text != '']

    def wait_for_grid_to_be_updated(self) -> None:
        attempt = 1
        timeout_after = 200
        items = self.get_all_price_elements()
        already_sorted = 1
        while True:
            new_items = self.get_all_price_elements()
            if items != new_items:
                break
            else:
                already_sorted += 1
                if already_sorted == 50:
                    break
            attempt += 1
            self.driver.implicitly_wait(0.1)
            if attempt == timeout_after:
                raise TimeoutException(msg="Error: Timed out waiting for widget update")

    def wait_to_be_updated(self, function) -> None:
        attempt = 1
        timeout_after = 200
        items = function()
        while True:
            new_items = function()
            if items != new_items:
                break
            attempt += 1
            self.driver.implicitly_wait(0.1)
            if attempt == timeout_after:
                raise TimeoutException(msg="Error: Timed out waiting for widget update")

    def find_and_click_on_element(self, element: Tuple) -> None:
        element = self.driver.find_element(*element)
        element.click()

    # def move_to_element_and_click(self, element):
    #     self.driver.execute_script("arguments[0].click();", self.driver.find_element(*element))
    #     #actions = webdriver.ActionChains(self.driver)
    #     #actions.move_to_element(self.driver.find_element(*element)).click().perform()

    @staticmethod
    def take_screenshot(driver: WebDriver, test_name: str) -> None:
        date_time = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
        screenshot_file = "screenshot_{}_{}.png".format(test_name, date_time)
        print("Taking screenshot {}".format(screenshot_file))
        driver.save_screenshot("/".join((os.environ['RESULT_DIR'], screenshot_file)))

    @staticmethod
    def truncate_price_value(price: str) -> str:
        return price.replace('£', '').replace('€', '').replace(',', '.').strip()

    @staticmethod
    def create_driver() -> WebDriver:
        if common_config.BROWSER == "Chrome":
            return webdriver.Chrome(executable_path=r'{}'.format(Common.__chrome_driver_path),
                                    options=Common.get_chrome_options())
        else:
            return webdriver.Firefox(executable_path=r'{}'.format(Common.__ff_driver_path),
                                     options=Common.get_ff_options())

    @staticmethod
    def get_ff_options():
        options = webdriver.FirefoxOptions()
        if common_config.DOCKER_RUN:
            options.add_argument("--headless")
            options.add_argument("--window-size=1920,1080")
        else:
            options.add_argument("-private")
        return options

    @staticmethod
    def get_chrome_options():
        options = webdriver.ChromeOptions()
        if common_config.DOCKER_RUN:
            options.add_argument("--headless")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1920,1080")
            options.binary_location = '/usr/bin/google-chrome'
            chrome_prefs = {}
            options.experimental_options["prefs"] = chrome_prefs
            chrome_prefs["profile.default_content_settings"] = {"images": 2}
        return options
