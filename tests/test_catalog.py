import random
from pages.catalog.catalog import CatalogPage
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
        filtered_brands = self.catalog_page.get_filtered_brands_dropdown()
        self.assertIn(brand, filtered_brands,
                      msg="FAILED - '{}' Brand has not appeared under dropdown"
                      .format(self._testMethodName))

        self.catalog_page.click_on_nike()
        brands = self.catalog_page.get_all_brand_names()
        self.assertTrue(all(appeared_brand == brand for appeared_brand in brands),
                        msg="FAILED - '{}' Not all brands are '{}' in '{}'"
                        .format(self._testMethodName, brand, brands))

    @TestBase.wrap_test
    def test_price_filter(self):
        """
        Test for price filter from 20 to 50
        """
        price_from = 20
        price_to = 50
        self.catalog_page.filter_by_price(price_from, price_to)
        from_field_value = float(self.catalog_page.get_from_value())
        to_field_value = float(self.catalog_page.get_to_value())
        self.assertEqual(from_field_value, price_from,
                         msg="FAILED - '{}' Filtered value is not appeared for 'from' field"
                         .format(self._testMethodName))
        self.assertEqual(to_field_value, price_to,
                         msg="FAILED - '{}' Filtered value is not appeared for 'to' field"
                         .format(self._testMethodName))
        prices = self.catalog_page.get_all_price_values()
        self.assertTrue(all(price_from <= price <= price_to for price in prices),
                        msg="FAILED - '{}' Filtered items' prices don't belong to ['{}'-'{}'] range -- '{}'"
                        .format(self._testMethodName, price_from, price_to, prices))

    @TestBase.wrap_test
    def test_brand_filter_dropdown(self):
        """
        Test for brand filter by 'Nik' and all brands under dropdown menu contains it
        """
        search_for = "Nik"
        search_tmp = "n"
        self.catalog_page.filter_by_brand(brand=search_for)
        brands = self.catalog_page.get_filtered_brands_dropdown()
        self.assertTrue(all(search_tmp.lower() in str(brand).lower() for brand in brands),
                        msg="FAILED - '{}' Not all brands in '{}' are contained '{}'"
                        .format(self._testMethodName, brands, search_for))

    @TestBase.wrap_test
    def test_catalogue_filter(self):
        """
        Test catalogue filter for “Women” -> “Shoes” -> “Heels” -> “High-heels”
        """
        self.catalog_page.click_on_catalogue_woman_shoes_heels_highheels()

        hrefs = self.catalog_page.get_catalogue_filtered_hrefs()
        random_href = random.choice(hrefs)
        self.assertIn(self.catalog_page.locators.search_href, random_href,
                      msg="FAILED - '{}' Random element doesn't belong to 'high-heels'"
                      .format(self._testMethodName))
