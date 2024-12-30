import random
import time
import allure
from data.generator import generated_address
from locators.account_locators import AccountLocators, AddressBookLocators
from pages.base_page import BasePage


class AccountPage(BasePage):
    LOCATORS = AccountLocators

    @allure.step('Click the Log out link')
    def log_out(self):
        self.find_element(self.LOCATORS.LOG_OUT_LINK).click()

    def view_address_book(self):
        self.find_element(self.LOCATORS.VIEW_ADDRESS_BOOK_LINK).click()


class AccountAddressBook(BasePage):
    LOCATORS = AddressBookLocators

    @allure.step('Get address details in the Main Address section')
    def get_main_address_text(self):
        address = self.find_elements(self.LOCATORS.MAIN_ADDRESS_DETAILS_ITEM)
        return [i.text for i in address]

    @allure.step('Get address details of the first address card')
    def get_address_book_item_text(self):
        address_details = self.find_elements(self.LOCATORS.ADDRESS_DETAILS_ITEM)[:6]
        return [i.text for i in address_details]

    @allure.step('Get address details of the second address card')
    def get_second_address_text(self):
        address_details = self.find_elements(self.LOCATORS.ADDRESS_DETAILS_ITEM)[6:12]
        return [i.text for i in address_details]

    @allure.step('Get the title text of the empty address book')
    def get_empty_address_book_title_text(self):
        return self.find_element(self.LOCATORS.EMPTY_ADDRESS_BOOK_TITLE).text

    def get_address_list(self):
        return self.find_elements(self.LOCATORS.ADDRESS_CARD)

    @allure.step('Click the Add An Address button')
    def click_add_address_button(self):
        self.find_element(self.LOCATORS.ADD_ADDRESS_BTN).click()
        time.sleep(1)

    @allure.step('Fill in the form fields')
    def fill_in_form_fields(self):
        address = generated_address()
        firstname = address.firstname
        lastname = address.lastname
        address1 = address.address1.replace('\n', '')
        address2 = address.address2.replace('\n', '')
        city = address.city
        postal_code = address.postal_code
        with allure.step('Enter firstname'):
            self.find_element(self.LOCATORS.FIRST_NAME_INPUT).send_keys(firstname)
        with allure.step('Enter lastname'):
            self.find_element(self.LOCATORS.LAST_NAME_INPUT).send_keys(lastname)
        with allure.step('Enter address 1'):
            self.find_element(self.LOCATORS.ADDRESS_1_INPUT).send_keys(address1)
        with allure.step('Enter address 2'):
            self.find_element(self.LOCATORS.ADDRESS_2_INPUT).send_keys(address2)
        with allure.step('Enter city'):
            self.find_element(self.LOCATORS.CITY_INPUT).send_keys(city)
        with allure.step('Select country in the dropdown'):
            country = self.select_item_in_dropdown_by_text(self.LOCATORS.COUNTRY_DROPDOWN, 'United Kingdom')
        with allure.step('Select random province in the dropdown'):
            random_index = random.randint(1, 5)
            self.select_item_in_dropdown_by_index(self.LOCATORS.STATE_DROPDOWN, random_index)
        with allure.step('Enter post code'):
            self.find_element(self.LOCATORS.POST_CODE_INPUT).send_keys(postal_code)
        with allure.step('Enter phone number'):
            self.find_element(self.LOCATORS.PHONE_INPUT).send_keys(address.phone)
        return [f'{firstname} {lastname}', address1, address2, city, postal_code, country]

    @allure.step('Tick the "Make this my main address" checkbox in the address form')
    def tick_main_address_checkbox(self):
        self.move_to_element(self.LOCATORS.DEFAULT_ADDRESS_CHECKBOX)
        self.find_element(self.LOCATORS.DEFAULT_ADDRESS_CHECKBOX).click()

    @allure.step('Click the Save address button')
    def save_address(self):
        self.move_to_element(self.LOCATORS.SAVE_ADDRESS_BTN)
        self.find_element(self.LOCATORS.SAVE_ADDRESS_BTN).click()
        time.sleep(2)

    @allure.step('Click the Delete address button')
    def delete_address(self):
        self.find_element(self.LOCATORS.DELETE_ADDRESS_BTN).click()
        time.sleep(1)

    @allure.step('Click the Edit address button')
    def edit_address(self):
        self.find_element(self.LOCATORS.EDIT_ADDRESS_BTN).click()
        self.clear_form()

    @allure.step('Clear form fields')
    def clear_form(self):
        self.find_element(self.LOCATORS.FIRST_NAME_INPUT).clear()
        self.find_element(self.LOCATORS.LAST_NAME_INPUT).clear()
        self.find_element(self.LOCATORS.ADDRESS_1_INPUT).clear()
        self.find_element(self.LOCATORS.ADDRESS_2_INPUT).clear()
        self.find_element(self.LOCATORS.CITY_INPUT).clear()
        self.find_element(self.LOCATORS.POST_CODE_INPUT).clear()
        self.find_element(self.LOCATORS.PHONE_INPUT).clear()

    @allure.step('Click "Make this my main" radiobutton in the address card')
    def change_main_address(self):
        self.find_element(self.LOCATORS.NAKE_ADDRESS_MAIN_RADIO_BTN).click()
        time.sleep(2)

    def check_field_errors(self):
        self.click_add_address_button()
        self.save_address()
        first_name_error = self.find_element(self.LOCATORS.FIRST_NAME_ERROR).text
        last_name_error = self.find_element(self.LOCATORS.LAST_NAME_ERROR).text
        address1_error = self.find_element(self.LOCATORS.ADDRESS_1_ERROR).text
        city_error = self.find_element(self.LOCATORS.CITY_ERROR).text
        post_code_error = self.find_element(self.LOCATORS.POST_CODE_ERROR).text
        return first_name_error, last_name_error, address1_error, city_error, post_code_error

    @allure.step('Check if an address card is present')
    def is_address_card_present(self):
        return self.is_element_present(self.LOCATORS.ADDRESS_CARD, 1)

    @allure.step('Check if the empty address book title is present')
    def is_empty_address_book_title_present(self):
        title = self.LOCATORS.EMPTY_ADDRESS_BOOK_TITLE
        if self.is_element_present(title):
            return True, self.get_empty_address_book_title_text()
        return False, None
    