import random
from pages.catalog.catalog import CatalogPage
from pages.catalog.catalog_locators import CatalogPageLocators
from tests.test_base import TestBase


class TestCatalogPage(TestBase):

    _report = []

    def setUp(self):
        super().setUp()
        self.catalog_page = CatalogPage(driver=self.driver)

    @TestBase.wrap_test
    def test_brand_filter_nike(self):
        """
        Test for brand filter by 'Ni' and all filtered items have "Nike" brand
        """
        self.catalog_page.filter_by_brand(brand="Nike")
        self.assertTrue(any(menu_item.text == "Nike" for menu_item in self.catalog_page.get_brand_filtered_dropdown()),
                        msg="FAILED - '{}' 'Nike' has not appeared under dropdown".format(self._testMethodName))

        self.catalog_page.click_on_nike()
        brands = {brand.text for brand in self.catalog_page.get_all_brand_names() if brand.text != ''}
        self.assertEqual(len(brands), 1,
                         msg="FAILED - '{}' Not all brands are 'Nike'".format(self._testMethodName))

    @TestBase.wrap_test
    def test_price_filter_20_50(self):
        """
        Test for price filter from 20 to 50
        """
        self.catalog_page.filter_by_price(20, 50)
        from_field_value = str(self.catalog_page.get_filter_by_price_from_element().get_attribute('value'))
        to_field_value = str(self.catalog_page.get_filter_by_price_to_element().get_attribute('value'))
        self.assertEqual(float(self.catalog_page.common.truncate_price_value(from_field_value)), 20,
                         msg="FAILED - '{}' Filtered value for 'from' field is not appeared".format(
                             self._testMethodName))
        self.assertEqual(float(self.catalog_page.common.truncate_price_value(to_field_value)), 50,
                         msg="FAILED - '{}' Filtered value for 'to' field is not appeared".format(self._testMethodName))
        self.assertTrue(all(20 <= float(self.catalog_page.common.truncate_price_value(price.text)) <= 50
                            for price in self.catalog_page.common.get_all_price_values()),
                        msg="FAILED - '{}' Filtered items don't belong to [20-50] range".format(self._testMethodName))

    @TestBase.wrap_test
    def test_brand_filter_nike_2(self):
        """
        Test for brand filter by 'Nik' and all brands under dropdown menu contains it
        """
        search_for = "Nik"
        search_for_test_pass = "n"
        self.catalog_page.filter_by_brand(brand=search_for)
        self.assertTrue(all(search_for_test_pass in str(menu_item.text).lower()
                            for menu_item in self.catalog_page.get_brand_filtered_dropdown()),
                        msg="FAILED - '{}' Not all brands are contained 'Nik'".format(self._testMethodName))

    @TestBase.wrap_test
    def test_catalogue_filter(self):
        """
        Test catalogue filter for “Women” -> “Shoes” -> “Heels” -> “High-heels”
        """
        self.catalog_page.click_on_catalogue_woman_shoes_heels_highheels()

        elements = self.catalog_page.get_catalogue_filtered_hrefs()
        random_element = random.choice(elements)
        self.assertIn(CatalogPageLocators.SEARCH_HREF,
                      random_element.get_attribute('href'),
                      msg="FAILED - '{}' Random element doesn't belong to 'high-heels'".format(self._testMethodName))
