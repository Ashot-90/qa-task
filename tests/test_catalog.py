import random
from pages.catalog.catalog import CatalogPage
from pages.catalog.catalog_locators import CatalogPageLocators
from tests.test_base import TestBase


class TestCatalogPage(TestBase):

    def setUp(self):
        super().setUp()
        self.catalog_page = CatalogPage(driver=self.driver)

    @TestBase.wrap_test
    def test_brand_filter(self):
        """
        Test for brand filter by 'Ni' and all filtered items have "Nike" brand
        """
        brand_filter = "Nik"
        brand = "Nike"
        self.catalog_page.filter_by_brand(brand=brand_filter)
        self.assertIn(brand, self.catalog_page.get_filtered_brands_dropdown(),
                      msg="FAILED - '{}' 'Nike' has not appeared under dropdown".format(self._testMethodName))

        self.catalog_page.click_on_nike()
        brands = set(self.catalog_page.get_all_brand_names())
        self.assertEqual(len(brands), 1,
                         msg="FAILED - '{}' Not all brands are 'Nike'".format(self._testMethodName))

    @TestBase.wrap_test
    def test_price_filter(self):
        """
        Test for price filter from 20 to 50
        """
        self.catalog_page.filter_by_price(20, 50)
        from_field_value = float(self.catalog_page.get_from_value())
        to_field_value = float(self.catalog_page.get_to_value())
        self.assertEqual(from_field_value, 20,
                         msg="FAILED - '{}' Filtered value is not appeared for 'from' field".format(
                             self._testMethodName))
        self.assertEqual(to_field_value, 50,
                         msg="FAILED - '{}' Filtered value is not appeared for 'to' field".format(self._testMethodName))
        self.assertTrue(all(20 <= price <= 50
                            for price in self.catalog_page.common.get_all_price_values()),
                        msg="FAILED - '{}' Filtered items don't belong to [20-50] range".format(self._testMethodName))

    @TestBase.wrap_test
    def test_brand_filter_dropdown(self):
        """
        Test for brand filter by 'Nik' and all brands under dropdown menu contains it
        """
        search_for = "Nik"
        search_tmp = "n"
        self.catalog_page.filter_by_brand(brand=search_for)
        self.assertTrue(all(search_tmp.lower() in str(brand).lower()
                            for brand in self.catalog_page.get_filtered_brands_dropdown()),
                        msg="FAILED - '{}' Not all brands are contained 'Nik'".format(self._testMethodName))

    @TestBase.wrap_test
    def test_catalogue_filter(self):
        """
        Test catalogue filter for “Women” -> “Shoes” -> “Heels” -> “High-heels”
        """
        self.catalog_page.click_on_catalogue_woman_shoes_heels_highheels()

        hrefs = self.catalog_page.get_catalogue_filtered_hrefs()
        random_href = random.choice(hrefs)
        self.assertIn(CatalogPageLocators.SEARCH_HREF, random_href,
                      msg="FAILED - '{}' Random element doesn't belong to 'high-heels'".format(self._testMethodName))
