import allure
from pages.product_listing_page import ProductListingPage
from data.links import URL


@allure.epic('PLP')
class TestPLP:
    @allure.description('Can sort by price asc/desc')
    def test_sorting_by_price(self, driver, check):
        page = ProductListingPage(driver, URL.PLP)
        page.open_page()

        with check:
            assert page.sort_by_price_asc(), 'Sorting by price asc is incorrect'
        with check:
            assert page.sort_by_price_desc(), 'Sorting by price desc is incorrect'

    @allure.description('Can load more products after clicking the Load More button')
    def test_load_more(self, driver):
        page = ProductListingPage(driver, URL.PLP)
        page.open_page()

        assert page.load_more(), 'Product list does not increase after clicking the Load More button'

    @allure.description('Can load all products after clicking the View All button')
    def test_view_all_products(self, driver):
        page = ProductListingPage(driver, URL.PLP)
        page.open_page()

        assert page.view_all_products(), 'Quantity of all products does not match the products quantity on PLP'

    @allure.description('Can sort by NEW')
    def test_sorting_by_newest(self, driver):
        page = ProductListingPage(driver, URL.PLP)
        page.open_page()

        page.sort_by_newest()
        number_of_new_products, are_products_sorted = page.check_sorted_by_newest()
        assert number_of_new_products > 0, 'No new products'
        assert are_products_sorted, 'New products are not listed first'

    @allure.description('Can filter by price range')
    def test_price_filter(self, driver, check):
        page = ProductListingPage(driver, URL.PLP)
        page.open_page()

        min_price, max_price = page.select_price_filter()
        price_list_acs, price_list_desc = page.get_price_list()
        with check:
            assert price_list_acs[0] >= min_price, 'The min price on PLP does not match the min price filter'
        with check:
            assert price_list_desc[0] <= max_price, 'The max price on PLP does not match the max price filter'

    @allure.description('Can reset filters via Clear All button')
    def test_clear_all(self, driver):
        page = ProductListingPage(driver, URL.PLP)
        page.open_page()

        unfiltered_products_count = page.get_total_product_count_value()
        # CHECK IF THE TOTAL QUANTITY OF PRODUCTS CHANGES AFTER APPLYING FILTERS
        page.select_price_filter()
        filtered_products_count = page.get_total_product_count_value()
        assert unfiltered_products_count > filtered_products_count, \
            'Total product count is not changed after applying filters'
        # CHECK IF THE TOTAL QUANTITY OF PRODUCTS RESTORED AFTER RESETTING FILTERS
        page.clear_all_filters()
        products_count_after_resetting_filters = page.get_total_product_count_value()
        assert products_count_after_resetting_filters == unfiltered_products_count, \
            'Check total product count after resetting filters'
