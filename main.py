import multiprocessing
from tests.test_member import TestMemberPage
from tests.test_catalog import TestCatalogPage

TESTS_1 = (
    TestMemberPage.test_price_sort,
)

TESTS_2 = (
    TestCatalogPage.test_price_filter,
    TestCatalogPage.test_brand_filter,
    TestCatalogPage.test_catalogue_filter,
    TestCatalogPage.test_brand_filter_dropdown
)


class Main(object):

    @staticmethod
    def run():
        cpu_count = multiprocessing.cpu_count()
        print("CPU Count is '{}'".format(cpu_count))
        test_catalog_page = TestCatalogPage()
        test_member_page = TestCatalogPage()
        pool = multiprocessing.Pool(processes=cpu_count)
        for test_function in TESTS_1:
            Main.__add_to_pool(pool, test_function, test_member_page)
        for test_function in TESTS_2:
            Main.__add_to_pool(pool, test_function, test_catalog_page)
        pool.close()
        pool.join()

    @staticmethod
    def __add_to_pool(pool: multiprocessing.Pool, function, page_object):
        print("Adding '{}' function to pool".format(function.__name__))
        pool.apply_async(func=function,
                         args=(page_object,))


if __name__ == "__main__":
    main = Main()
    main.run()
