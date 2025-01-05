import allure
import pytest
from data.constants import Base, Account
from data.generator import not_valid_phone_number
from data.links import URL
from pages.account_page import AccountPage, AccountAddressBook


@allure.epic('Account')
@pytest.mark.usefixtures('login')
class TestAccount:
    @allure.feature('Account main page')
    class TestAccountMainPage:
        @allure.description('Can log out from account')
        def test_logout(self, driver, check):
            page = AccountPage(driver, URL.ACCOUNT_PAGE)

            page.log_out()
            with check:
                assert page.get_current_url() == URL.MAIN_PAGE, 'User is not redirected to main page after signing out'
            with check:
                assert page.is_sign_in_tooltip_present(), 'Sign In tooltip is missing after signing out'
                assert page.get_sign_in_tooltip_text() == Base.SIGN_IN_TOOLTIP_TEXT, 'Check text in the Sign In tooltip'
                assert page.is_sign_in_tooltip_disappeared(), 'Sign In tooltip did not disappear after 5 seconds'
            is_user_logged_in, account_icon_text = page.check_account_icon()
            with check:
                assert is_user_logged_in is False, 'Check the "logged-in" attribute of account icon'
                assert account_icon_text == Base.ACCOUNT_ICON_DEFAULT_TEXT, \
                    'Check the account name next to account icon'

    @allure.feature('Account address book')
    class TestAccountAddressBook:
        @pytest.fixture()
        def add_address(self, driver):
            """Add address before the test"""
            page = AccountAddressBook(driver, URL.ACCOUNT_ADDRESS_BOOK)
            page.open_page()
            page.click_add_address_button()
            page.fill_in_form_fields()
            page.save_address()

        @pytest.fixture()
        def clear_address_book(self, driver):
            """Delete all addresses after the test"""
            yield
            page = AccountAddressBook(driver, URL.ACCOUNT_ADDRESS_BOOK)
            page.open_page()
            if page.is_address_card_present():
                address_list = page.get_address_list()
                for _ in address_list:
                    page.delete_address()

        @allure.description('Can add a new address')
        def test_add_new_address(self, driver, clear_address_book):
            page = AccountAddressBook(driver, URL.ACCOUNT_ADDRESS_BOOK)
            page.open_page()

            page.click_add_address_button()
            form = page.fill_in_form_fields()
            page.save_address()
            added_address_details = page.get_address_book_item_text()
            assert form == added_address_details, 'Address details in the form and in the address card are different'

        @allure.description('Can delete the address')
        def test_delete_address(self, driver, check, add_address, clear_address_book):
            page = AccountAddressBook(driver, URL.ACCOUNT_ADDRESS_BOOK)
            page.open_page()

            page.delete_address()
            is_empty_address_book_title_present, title_text = page.is_empty_address_book_title_present()
            with check:
                assert is_empty_address_book_title_present, 'Empty address book title is missing'
                assert title_text == Account.EMPTY_ADDRESS_BOOK_TITLE_TEXT, 'Check the empty address book title text'
            with check:
                assert page.is_address_card_present() is False, 'Address card is present after deletion'

        @allure.description('Can edit the address')
        def test_edit_address(self, driver, add_address, clear_address_book):
            page = AccountAddressBook(driver, URL.ACCOUNT_ADDRESS_BOOK)
            page.open_page()

            page.edit_address()
            form = page.fill_in_form_fields()
            page.save_address()
            edited_address_details = page.get_address_book_item_text()
            assert form == edited_address_details, 'Address details in the form and in the address card are different'

        @allure.description('Can change the main address via radiobutton in the address cards')
        def test_change_main_address_in_address_cards(self, driver, add_address, clear_address_book):
            page = AccountAddressBook(driver, URL.ACCOUNT_ADDRESS_BOOK)
            page.open_page()

            first_address_details = page.get_address_book_item_text()

            # CHECK MAIN ADDRESS
            main_address = page.get_main_address_text()
            assert main_address == first_address_details, 'Main address does not match the address in the address card'

            # ADD SECOND ADDRESS
            page.click_add_address_button()
            second_address_details = page.fill_in_form_fields()
            page.save_address()

            # CHECK THAT THE SECOND ADDED ADDRESS IS NOT MAIN YET
            assert second_address_details != main_address, 'Main address changed after adding the second address'

            # CHANGE MAIN ADDRESS
            page.change_main_address()
            changed_main_address = page.get_main_address_text()

            # CHECK THAT MAIN ADDRESS CHANGED
            assert changed_main_address == second_address_details, 'Main address was not changed'

        @allure.description('Can change the main address using the checkbox in the form')
        def test_change_main_address_in_form(self, driver, add_address, clear_address_book):
            page = AccountAddressBook(driver, URL.ACCOUNT_ADDRESS_BOOK)
            page.open_page()

            first_address_details = page.get_address_book_item_text()

            # CHECK MAIN ADDRESS
            main_address = page.get_main_address_text()
            assert main_address == first_address_details, 'Main address does not match the address in the address card'

            # ADD SECOND ADDRESS WITH TICKING THE MAIN ADDRESS CHECKBOX IN THE FORM
            page.click_add_address_button()
            second_address_details = page.fill_in_form_fields()
            page.tick_main_address_checkbox()
            page.save_address()

            # CHECK THAT MAIN ADDRESS CHANGED
            changed_main_address = page.get_main_address_text()
            assert changed_main_address == second_address_details, 'Main address was not changed'

        @allure.description('Can see the errors when saving an address with empty required fields')
        @pytest.mark.parametrize('field', ['first_name', 'last_name', 'address1', 'city', 'post_code', 'phone'])
        @allure.tag('negative')
        def test_empty_field_errors(self, field, driver):
            page = AccountAddressBook(driver, URL.ACCOUNT_ADDRESS_BOOK)
            page.open_page()

            error = page.check_empty_field_errors(field)
            assert error == Account.REQUIRED_FIELD_ERROR_TEXT, f'Check error for empty {field} field'

        @allure.description('Can see the error when entering a not valid phone format')
        @pytest.mark.parametrize('input_value', not_valid_phone_number())
        @allure.tag('negative')
        def test_validate_phone_field(self, input_value, driver):
            page = AccountAddressBook(driver, URL.ACCOUNT_ADDRESS_BOOK)
            page.open_page()

            page.click_add_address_button()
            error = page.enter_not_valid_phone_format(input_value)
            assert error == Account.PHONE_ERROR_TEXT, 'Check the phone field error'
