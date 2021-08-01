from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from pages.base.base import BasePage
from pages.common import common_config
from pages.common.common_locators import CommonPageLocators
from datetime import datetime
from selenium import webdriver


class CommonPage(BasePage):
    __chrome_driver_path = common_config.COMMON_CONFIG['chrome_driver_path']
    __ff_driver_path = common_config.COMMON_CONFIG['ff_driver_path']

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.locators = CommonPageLocators(driver=self.driver)

    def __close_questionnaire(self) -> None:
        widget = self.locators.questionnaire
        self.locators.close_questionnaire_button.click()

    def __accept_all_cookies(self) -> None:
        element = self.locators.accept_all_cookies_button
        self.wait_for_stop_element_move(element)
        self.locators.accept_all_cookies_button.click()

    def load_page(self, url: str) -> None:
        self.driver.get(url)
        self.driver.maximize_window()
        try:
            self.__accept_all_cookies()
            # For .DE no questionnaire
            if common_config.PORTAL != 'DE':
                self.__close_questionnaire()
            widget = self.locators.grid_widget
        except TimeoutException:
            CommonPage.take_screenshot(driver=self.driver,
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

    def wait_for_grid_to_be_updated(self, locators) -> None:
        attempt = 1
        timeout_after = 200
        items = locators.all_prices
        already_sorted = 1
        while True:
            new_items = locators.all_prices
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

    def truncate_all_price_values(self, locators):
        return [float(self.truncate_price_value(price_element.text)) for price_element in locators.all_prices
                if price_element.text != '' and ('£' in price_element.text or '€' in price_element.text)]

    # def move_to_element_and_click(self, element):
    #     self.driver.execute_script("arguments[0].click();", self.driver.find_element(*element))
    #     #actions = webdriver.ActionChains(self.driver)
    #     #actions.move_to_element(self.driver.find_element(*element)).click().perform()

    @staticmethod
    def take_screenshot(driver: WebDriver, test_name: str) -> str:
        date_time = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
        screenshot_name = "screenshot_{}_{}.png".format(test_name, date_time)
        screenshot_path = "/".join((common_config.RESULT_DIR, screenshot_name))
        print("Taking screenshot {}".format(screenshot_name))
        driver.save_screenshot(screenshot_path)
        return screenshot_path

    @staticmethod
    def truncate_price_value(price: str) -> str:
        return price.replace('£', '').replace('€', '').replace(',', '.').strip()

    @staticmethod
    def create_driver() -> WebDriver:
        if common_config.BROWSER == "Chrome":
            return webdriver.Chrome(executable_path=r'{}'.format(CommonPage.__chrome_driver_path),
                                    options=CommonPage.get_chrome_options())
        else:
            return webdriver.Firefox(executable_path=r'{}'.format(CommonPage.__ff_driver_path),
                                     options=CommonPage.get_ff_options())

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
