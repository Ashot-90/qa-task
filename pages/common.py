from functools import wraps
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.common_locators import CommonPageLocators
from datetime import datetime
from selenium import webdriver
import os


class Common(object):

    portal = os.environ['PORTAL']
    chrome_driver_path = './chromedriver'

    def __init__(self, driver, page_elements):
        self.driver = driver
        self.page_elements = page_elements

    def load_page(self):
        url = self.page_elements.URL
        self.driver.get(url)
        self.driver.maximize_window()
        try:
            wait = WebDriverWait(self.driver, timeout=10)
            self.accept_all_cookies()
            # For .DE no questionnaire
            if self.portal != 'DE':
                load_completed = wait.until(
                    EC.text_to_be_present_in_element(CommonPageLocators.QUESTIONNAIRE,
                                                     CommonPageLocators.QUESTIONNAIRE_TEXT))
                if load_completed:
                    self.find_and_click_on_element(element=CommonPageLocators.CLOSE_QUESTIONNAIRE_BUTTON)
            else:
                wait.until(
                    EC.presence_of_element_located(self.page_elements.GRID))
        except TimeoutException:
            Common.take_screenshot(driver=self.driver,
                                   test_name='some_test')
            raise TimeoutException("Error: Timed out waiting for page load")

    def accept_all_cookies(self):
        element = WebDriverWait(self.driver, 30).until(
                            EC.element_to_be_clickable(CommonPageLocators.ACCEPT_ALL_COOKIES))
        self.wait_for_stop_element_move(element)
        self.find_and_click_on_element(element=CommonPageLocators.ACCEPT_ALL_COOKIES)

    def wait_for_stop_element_move(self, element):
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

    def get_all_price_elements(self):
        return self.driver. \
            find_element(*self.page_elements.GRID). \
            find_elements(*self.page_elements.ALL_PRICES)

    def wait_for_grid_to_be_updated(self):
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
                if already_sorted == 20:
                    break
            attempt += 1
            self.driver.implicitly_wait(0.1)
            if attempt == timeout_after:
                raise TimeoutException(msg="Error: Timed out waiting for widget update")

    def wait_to_be_updated(self, function):
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

    def find_and_click_on_element(self, element):
        element = self.driver.find_element(*element)
        element.click()

    @staticmethod
    def test_wrapper(test_function):
        @wraps(test_function)
        def wrapper(test):
            try:
                test_function(test)
                print("PASSED - '{}'".format(test._testMethodName))
            except Exception as ex:
                print("FAILED - '{}'".format(test._testMethodName))
                Common.take_screenshot(driver=test.driver,
                                       test_name=test._testMethodName)
                raise ex
        return wrapper

    @staticmethod
    def take_screenshot(driver, test_name):
        date_time = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
        screenshot_file = "screenshot_{}_{}.png".format(test_name, date_time)
        print("Taking screenshot {}".format(screenshot_file))
        driver.save_screenshot(screenshot_file)

    @staticmethod
    def truncate_price_value(price: str):
        return price.replace('£', '').replace('€', '').replace(',', '.').strip()

    @staticmethod
    def create_driver():
        return webdriver.Chrome(executable_path=r'{}'.format(Common.chrome_driver_path),
                                options=Common.get_chrome_options())

    @staticmethod
    def get_chrome_options():
        options = webdriver.ChromeOptions()
        try:
            os.environ['DOCKER_RUN']
        except KeyError:
            return options
        else:
            options.add_argument("--headless")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--disable-gpu")
            options.binary_location = '/usr/bin/google-chrome'
            chrome_prefs = {}
            options.experimental_options["prefs"] = chrome_prefs
            chrome_prefs["profile.default_content_settings"] = {"images": 2}
            return options
