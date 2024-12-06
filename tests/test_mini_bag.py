import allure
import pytest
from data.constants import Bag
from pages.mini_bag import MiniBag


@allure.epic('Mini bag')
@pytest.mark.usefixtures('add_product_to_bag')
class TestMiniBag:
    @allure.description('Can change a product quantity')
    def test_select_product_quantity(self, driver):
        page = MiniBag(driver, driver.current_url)

        selected_quantity, displayed_quantity = page.select_quantity()
        product_price = page.get_product_price_value()
        subtotal_value = page.get_subtotal_value()
        assert selected_quantity == displayed_quantity, 'Displayed quantity is not equal to selected quantity'
        assert subtotal_value == product_price * displayed_quantity, 'The subtotal is incorrect'

    @allure.description('Can not apply the wrong discount code')
    def test_not_valid_discount_code(self, driver):
        code = 123
        page = MiniBag(driver, driver.current_url)

        page.enter_discount_code(code)
        page.apply_discount_code()
        error_is_present, error_text = page.is_discount_code_error_present()
        assert error_is_present, 'Wrong discount code error is missing'
        assert error_text == Bag.DISCOUNT_CODE_ERROR, 'Wrong discount code error text is incorrect'

    @allure.description('Can restore product in the mini bag')
    def test_restore_product(self, driver):
        page = MiniBag(driver, driver.current_url)

        page.delete_product()
        page.restore_product()
        assert page.is_product_present(), 'Product was not restored'

    @allure.description('Can open and close the delivery info sheet')
    def test_delivery_info_sheet(self, driver):
        page = MiniBag(driver, driver.current_url)

        open_sheet, closed_sheet = page.check_delivery_info_sheet()
        assert open_sheet, 'Delivery info sheet is not open when hovering over the info button'
        assert closed_sheet, 'Delivery info sheet is not closed when moving cursor outside info button'

    @allure.description('Can delete product from the mini bag')
    def test_delete_product(self, driver, check):
        page = MiniBag(driver, driver.current_url)

        page.delete_product()
        empty_bag_text_is_present, text = page.is_empty_bag_text_present()
        toast_is_present, toast_text = page.is_product_removed_toast_present()
        with check:
            assert page.is_product_present() is False, 'Product was not deleted from the mini bag'
        with check:
            assert empty_bag_text_is_present, 'Empty bag text is missing'
            assert text == Bag.EMPTY_BAG_TEXT, 'Empty bag text is incorrect'
        with check:
            assert toast_text, 'Removed product toast is missing'
            assert toast_text == Bag.REMOVED_PRODUCT_TOAST_TEXT, 'Removed product toast text is incorrect'
            assert page.is_product_removed_toast_disappeared(), 'Toast did not disappear after 5 seconds'

    @allure.description('Can close the mini bag')
    def test_close_mini_bag(self, driver):
        page = MiniBag(driver, driver.current_url)

        bag_is_closed = page.close_mini_bag()
        assert bag_is_closed, 'Mini bag was not closed'
