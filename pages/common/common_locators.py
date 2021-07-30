from selenium.webdriver.common.by import By


class CommonPageLocators(object):
    URL = None
    ALL_PRICES = None
    CLOSE_QUESTIONNAIRE_BUTTON = (By.XPATH, "/html/body/div[13]/div/div/div/div[1]/div/div[3]/button")
    QUESTIONNAIRE = (By.XPATH, "/html/body/div[13]/div/div/div")
    QUESTIONNAIRE_TEXT = 'Where do you live?'
    ACCEPT_ALL_COOKIES = (By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
    REJECT_ALL_COOKIES = (By.XPATH, '//*[@id="onetrust-reject-all-handler"]')
    MANAGE_ALL_COOKIES = (By.XPATH, '//*[@id="onetrust-pc-btn-handler"]')
    COOKIES_GROUP_BUTTON = (By.XPATH, '//*[@id="onetrust-button-group"]')
    GRID = (By.CLASS_NAME, "feed-grid")
