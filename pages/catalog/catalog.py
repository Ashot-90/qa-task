from pages.catalog.catalog_locators import CatalogPageLocators
from pages.common import Common


class CatalogPage(object):

    def __init__(self, driver):
        self.driver = driver
        self.common = Common(driver=self.driver, page_elements=CatalogPageLocators)
        self.common.load_page()

    def filter_by_brand(self, brand):
        self.common.find_and_click_on_element(element=CatalogPageLocators.BRAND_DROPDOWN_BUTTON)
        field = self.driver.find_element(*CatalogPageLocators.BRAND_INPUT)
        field.clear()
        field.send_keys(brand)

    def get_filter_by_price_from_element(self):
        return self.driver.find_element(*CatalogPageLocators.PRICE_FROM)

    def get_filter_by_price_to_element(self):
        return self.driver.find_element(*CatalogPageLocators.PRICE_TO)

    def filter_by_price(self, from_price, to_price):
        self.common.find_and_click_on_element(element=CatalogPageLocators.PRICE_DROPDOWN_BUTTON)
        from_price_field = self.get_filter_by_price_from_element()
        from_price_field.clear()
        from_price_field.send_keys(from_price)

        to_price_field = self.get_filter_by_price_to_element()
        to_price_field.clear()
        to_price_field.send_keys(to_price)
        to_price_field.send_keys(u'\ue007')

    def click_on_catalogue_woman_shoes_heels_highheels(self):
        locator_flow = (CatalogPageLocators.CATALOGUE_DROPDOWN_BUTTON,
                        CatalogPageLocators.CATALOGUE_WOMAN,
                        CatalogPageLocators.CATALOGUE_WOMAN_SHOES,
                        CatalogPageLocators.CATALOGUE_WOMAN_SHOES_HEELS,
                        CatalogPageLocators.CATALOGUE_WOMAN_SHOES_HEELS_HIGHHEELS)
        for locator in locator_flow:
            self.common.find_and_click_on_element(element=locator)

    def _get_all_brand_filtered_dropdown(self):
        return self.driver.find_elements(*CatalogPageLocators.FILTERED_LIST)

    def get_all_href_elements(self):
        return self.driver.find_elements(*CatalogPageLocators.ALL_HREFS)

    def click_on_nike(self):
        self.common.find_and_click_on_element(element=CatalogPageLocators.NIKE_CHECK_BOX)

    def _get_all_brand_elements(self):
        return self.driver. \
            find_element(*CatalogPageLocators.GRID). \
            find_elements(*CatalogPageLocators.ALL_BRANDS)

    def get_all_brand_names(self):
        self.common.wait_for_grid_to_be_updated()
        return self._get_all_brand_elements()

    def get_all_price_values(self):
        self.common.wait_for_grid_to_be_updated()
        return self.common.get_all_price_elements()

    def get_catalogue_filtered_hrefs(self):
        self.common.wait_for_grid_to_be_updated()
        return self.get_all_href_elements()

    def get_brand_filtered_dropdown(self):
        self.common.wait_to_be_updated(function=self._get_all_brand_filtered_dropdown)
        return self._get_all_brand_filtered_dropdown()

