import random
import time
import allure
from selenium.webdriver import Keys, ActionChains
from locators.bag_locators import BagLocators
from pages.base_page import BasePage


class MiniBag(BasePage):
    LOCATORS = BagLocators

    def get_product_title_text(self):
        return self.find_element(self.LOCATORS.PRODUCT_TITLE).text

    def get_product_color_value(self):
        return self.find_element(self.LOCATORS.PRODUCT_COLOR_AND_SIZE).text.split(' |')[0]

    def get_product_size_value(self):
        return self.find_element(self.LOCATORS.PRODUCT_COLOR_AND_SIZE).text.split('| ')[1]

    def get_product_price_value(self):
        return float(self.find_element(self.LOCATORS.PRODUCT_PRICE).text.split('£')[1])

    def get_subtotal_value(self):
        return int(self.find_element(self.LOCATORS.SUBTOTAL_VALUE).text.lstrip('£'))

    def get_empty_bag_text(self):
        return self.find_element(self.LOCATORS.EMPTY_BAG_TEXT).text

    def click_checkout_button(self):
        self.find_element(self.LOCATORS.CHECKOUT_BTN).click()

    @allure.step('Enter the discount code')
    def enter_discount_code(self, code):
        self.find_element(self.LOCATORS.ENTER_CODE_FIELD).send_keys(code)

    @allure.step('Click the Apply button')
    def apply_discount_code(self):
        self.find_element(self.LOCATORS.APPLY_CODE_BUTTON).click()

    def add_to_wishlist(self):
        self.find_element(self.LOCATORS.ADD_TO_WISHLIST).click()

    @allure.step('Select a random product quantity')
    def select_quantity(self):
        self.find_element(self.LOCATORS.QUANTITY_SELECTOR).click()
        random_quantity = random.randint(1, 9)
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ARROW_DOWN * random_quantity)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        time.sleep(4)
        displayed_quantity = int(self.find_element(self.LOCATORS.QUANTITY_SELECTOR).text.split(': ')[1])
        return random_quantity + 1, displayed_quantity

    @allure.step('Click the  Delete button')
    def delete_product(self):
        self.find_element(self.LOCATORS.DELETE_BTN).click()

    @allure.step('Click the Undo button')
    def restore_product(self):
        time.sleep(3)
        self.find_element(self.LOCATORS.UNDO_DELETION_BTN).click()

    def check_delivery_info_sheet(self):
        time.sleep(1)
        with allure.step('Hover over the delivery info icon'):
            self.move_to_element(self.LOCATORS.DELIVERY_INFO_BUTTON)
        with allure.step('Check if the delivery info sheet is open'):
            open_sheet = self.is_element_present(self.LOCATORS.DELIVERY_INFO_SHEET)
        with allure.step('Move cursor outside the delivery info icon'):
            self.move_mouse_by_offset(15, 15)
        with allure.step('Check if the delivery info sheet disappeared'):
            closed_sheet = self.is_disappeared(self.LOCATORS.DELIVERY_INFO_SHEET, 2)
        return open_sheet, closed_sheet

    @allure.step('Click the Close button in the mini bag')
    def close_mini_bag(self):
        self.find_element(self.LOCATORS.CLOSE_BAG_BTN).click()
        return self.is_disappeared(self.LOCATORS.MINI_BAG_SHEET)

    @allure.step('Check if the discount code error is present')
    def is_discount_code_error_present(self):
        error = self.LOCATORS.CODE_ERROR
        if self.is_element_present(error):
            return True, self.find_element(error).text
        return False, None

    @allure.step('Check if the Empty Bag text is present')
    def is_empty_bag_text_present(self):
        text = self.LOCATORS.EMPTY_BAG_TEXT
        if self.is_element_present(text):
            return True, self.find_element(text).text
        return False, None

    @allure.step('Check if a product is in the mini bag')
    def is_product_present(self):
        return self.is_element_present(self.LOCATORS.PRODUCT_ITEM, 2)

    def is_product_removed_toast_present(self):
        toast = self.LOCATORS.PRODUCT_REMOVED_TOAST
        if self.is_element_present(toast):
            return True, self.find_element(toast).text
        return False, None

    @allure.step('Check if the product_removed_toast disappears after 5 seconds')
    def is_product_removed_toast_disappeared(self):
        return self.is_disappeared(self.LOCATORS.PRODUCT_REMOVED_TOAST, 5)
