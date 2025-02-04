import allure
from data.constants import Search
from data.links import URL
from pages.search_modal import SearchModal


@allure.epic('Search')
class TestSearch:
    @allure.description('Can close the search modal. Check placeholder text in the search input')
    def test_search_modal(self, driver, check):
        page = SearchModal(driver, URL.MAIN_PAGE)
        page.open_page()

        placeholder = page.click_header_search()
        page.close_search_modal()
        is_modal_closed = page.is_search_modal_closed()
        with check:
            assert placeholder == Search.SEARCH_FIELD_PLACEHOLDER, 'Check placeholder text in the search field'
        with check:
            assert is_modal_closed is True, 'Search modal is not closed'

    @allure.description('Can clear the search field')
    def test_search_input_field(self, driver):
        page = SearchModal(driver, URL.MAIN_PAGE)
        page.open_page()

        search_query = 'hoody'

        page.click_header_search()
        page.enter_search_query(search_query)
        empty_search_field = page.clear_search_field()
        assert empty_search_field, 'Search field is not cleared'

    @allure.step('Recent searches appears after searching and can be cleared')
    def test_recent_searches(self, driver, check):
        page = SearchModal(driver, URL.MAIN_PAGE)
        page.open_page()

        search_query = 'hoody'

        page.click_header_search()
        page.enter_search_query(search_query)
        view_all_name = page.click_view_all_link()
        page.click_header_search()
        recent_search_item_text = page.get_recent_search_item_text()
        recent_search_item_link = page.get_recent_search_item_link()
        is_searches_cleared = page.clear_recent_searches()
        with check:
            assert view_all_name == search_query, 'Product name in the View all link does not match the search query'
        with check:
            assert recent_search_item_text == search_query, 'Recent search item and the search query are different'
        with check:
            assert recent_search_item_link == f'{URL.MAIN_PAGE}search?q={search_query}'
        with check:
            assert is_searches_cleared, 'Recent searches is not cleared'

    @allure.description('Recently viewed appears and can be cleared')
    def test_recently_viewed(self, driver, check):
        page = SearchModal(driver, URL.PDP)
        page.open_page()

        page.click_header_search()
        recently_viewed_link = page.get_recently_viewed_link()
        is_viewed_cleared = page.clear_recently_viewed()
        with check:
            assert recently_viewed_link == URL.PDP, 'Recently viewed link is not correct'
        with check:
            assert is_viewed_cleared, 'Recently viewed is not cleared'

    @allure.description('Check the error message for negative search')
    @allure.tag('negative')
    def test_negative_search(self, driver):
        page = SearchModal(driver, URL.MAIN_PAGE)
        page.open_page()

        search_query = '@#$%^'

        page.click_header_search()
        page.enter_search_query(search_query)
        error_text = page.get_no_results_error_text()
        assert error_text == Search.NO_RESULTS_ERROR(search_query), 'Check the no results error text'
