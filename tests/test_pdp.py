import allure
from data.links import URL
from pages.product_page import ProductPage


@allure.epic('Product page')
class TestPDP:
    @allure.description('Can auto scroll to the reviews section when clicking the reviews button')
    def test_scroll_to_reviews(self, driver):
        page = ProductPage(driver, URL.PDP)
        page.open_page()

        page.click_rating_button()
        assert page.is_reviews_title_in_viewport() is True, 'The page was not scrolled to the reviews section'

    @allure.description('Can open and close the more reviews sheet')
    def test_more_reviews(self, driver):
        page = ProductPage(driver, URL.PDP)
        page.open_page()

        page.click_more_reviews_button()
        assert page.is_reviews_sheet_open() is True, 'More reviews sheet is not open'

        page.close_review_sheet()
        assert page.is_reviews_sheet_open() is False, 'More reviews sheet is not closed'

    @allure.description('Can open and close the size guide sheet')
    def test_size_guide(self, driver):
        page = ProductPage(driver, URL.PDP)
        page.open_page()

        page.open_size_guide()
        assert page.is_size_guide_open() is True, 'Size guide sheet is not open'

        page.close_size_guide()
        assert page.is_size_guide_open() is False, 'Size guide sheet is not closed'

    @allure.description('Can change the product color')
    def test_change_product_color(self, driver, check):
        page = ProductPage(driver, URL.PDP)
        page.open_page()

        default_color = page.get_product_color_text()
        default_image = page.get_product_image_src()
        current_color, current_image = page.select_random_color()
        with check:
            assert default_color != current_color, 'Product color is not changed'
        with check:
            assert default_image != current_image, 'Product image is not changed'

    @allure.description('Can select a size; error appears if size is not selected')
    def test_select_size(self, driver):
        page = ProductPage(driver, URL.PDP)
        page.open_page()

        # Check if error appears when adding a product to the cart without selecting a size
        page.add_to_bag()
        size_error = page.get_size_error_text()
        assert size_error == 'Please select a size', 'Check the not selected size error text'

        # Check if a size can be selected and the error has disappeared
        page.select_random_size()
        assert page.is_size_error_present() is False, 'Size error is still present after selecting the size'

    @allure.description('Login prompt modal can be open and closed when clicking the add to wishlist for not auth user')
    def test_login_prompt(self, driver):
        page = ProductPage(driver, URL.PDP)
        page.open_page()

        page.click_add_to_wishlist_button()
        assert page.is_login_prompt_open() is True, 'Login prompt does not appears'

        page.close_login_prompt()
        assert page.is_login_prompt_open() is False, 'Login prompt is not closed after clicking the close icon'

    @allure.description('Can copy the current page URL using Share button')
    def test_share_button(self, driver, check):
        page = ProductPage(driver, URL.PDP)
        page.open_page()

        expected_url = page.click_share_button()
        current_url = page.get_current_url()
        with check:
            assert expected_url == current_url, 'Page URL was not copied'
        with check:
            assert page.link_copied_toast_appears(), 'Toast does not appear'
        with check:
            assert page.link_copied_toast_disappears(), 'Toast does not disappear after 3 seconds'

    @allure.description('Can scroll the image carousel using Up and Down buttons')
    def test_image_slider_buttons(self, driver, check):
        page = ProductPage(driver, URL.PDP)
        page.open_page()

        value_before, value_after_down, value_after_up = page.check_image_slider()
        with check:
            assert value_before < value_after_down, 'The image gallery was not scrolled down'
        with check:
            assert value_after_up < value_after_down, 'The image gallery was not scrolled up'
