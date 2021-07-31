from selenium.webdriver.remote.webdriver import WebDriver


class BasePage(object):
    def __init__(self, driver: WebDriver):
        self.driver = driver
