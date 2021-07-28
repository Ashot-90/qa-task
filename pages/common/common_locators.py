import os
from selenium.webdriver.common.by import By
from pages.catalog import catalog_config
from pages.member import member_config


class CommonPageLocators(object):
    URL = None
    ALL_PRICES = None
    PORTAL = os.environ['PORTAL']
    if PORTAL == 'DE':
        CATALOG_CONFIG = catalog_config.config_de
        CATALOG_MEMBER = member_config.config_de
    elif PORTAL == 'UK':
        CATALOG_CONFIG = catalog_config.config_uk
        CATALOG_MEMBER = member_config.config_uk
    CLOSE_QUESTIONNAIRE_BUTTON = (By.XPATH, "/html/body/div[13]/div/div/div/div[1]/div/div[3]/button")
    QUESTIONNAIRE = (By.XPATH, "/html/body/div[13]/div/div/div")
    QUESTIONNAIRE_TEXT = 'Where do you live?'
    ACCEPT_ALL_COOKIES = (By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
    REJECT_ALL_COOKIES = (By.XPATH, '//*[@id="onetrust-reject-all-handler"]')
    MANAGE_ALL_COOKIES = (By.XPATH, '//*[@id="onetrust-pc-btn-handler"]')
    COOKIES_GROUP_BUTTON = (By.XPATH, '//*[@id="onetrust-button-group"]')
    GRID = (By.CLASS_NAME, "feed-grid")
