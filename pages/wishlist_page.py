import allure
import random
from locators.wishlist_locators import WishListLocators
from pages.base_page import BasePage


class WishlistPage(BasePage):
    LOCATORS = WishListLocators

    def get_product_count(self):
        return int(self.find_element(self.LOCATORS.PRODUCT_COUNT).text.split()[0])

    @allure.step('Get wishlist toast text')
    def get_toast_text(self):
        return self.find_element(self.LOCATORS.WISHLIST_TOAST_TEXT).text

    @allure.step('Click the Wishlist icon in the product card')
    def click_wishlist_icon_in_product_card(self):
        self.find_element(self.LOCATORS.PRODUCT_CARD_WISHLIST_ICON).click()
        return self.is_wishlist_empty()

    def remove_product_in_more_menu(self):
        with allure.step('Click the More menu'):
            self.find_element(self.LOCATORS.MORE_MENU).click()
        with allure.step('Click the Remove From Wishlist button'):
            self.find_element(self.LOCATORS.MORE_MENU_REMOVE).click()
        return self.is_wishlist_empty()

    def remove_all_products(self):
        with allure.step('Click the Remove All Items button'):
            self.move_to_element(self.LOCATORS.REMOVE_ALL_ITEMS_BTN)
            self.find_element(self.LOCATORS.REMOVE_ALL_ITEMS_BTN).click()
        with allure.step('Click Yes button in modal'):
            self.find_element(self.LOCATORS.REMOVE_ALL_YES_BTN).click()
        return self.is_wishlist_empty()

    @allure.step('Open the Size dropdown, select a random size, get selected size')
    def select_random_size(self):
        random_item = random.randint(0, 4)
        size_dropdown = self.LOCATORS.SIZE_DROPDOWN
        size_list_item = self.LOCATORS.SIZE_DROPDOWN_ITEM

        self.find_element(size_dropdown).click()
        random_size_value = self.find_elements(size_list_item)[random_item].text
        self.find_elements(size_list_item)[random_item].click()
        selected_size_value = self.find_element(size_dropdown).text
        return random_size_value, selected_size_value

    @allure.step('Click the add to bag button')
    def click_add_to_bag_button(self):
        self.find_element(self.LOCATORS.ADD_TO_BAG_BTN).click()

    def add_to_bag_from_more_menu(self):
        with allure.step('Click the More menu'):
            self.find_element(self.LOCATORS.MORE_MENU).click()
        with allure.step('Click the Add To Bag button'):
            self.find_element(self.LOCATORS.MORE_MENU_ADD_TO_BAG).click()
        return self.is_bag_count_icon_present()

    @allure.step('Click the Undo button in the toast')
    def undo_deletion(self):
        if self.is_wishlist_toast_present():
            toast_text = self.get_toast_text()
            self.find_element(self.LOCATORS.WISHLIST_TOAST_ACTION_BTN).click()
            return True, toast_text
        return False, None

    @allure.step('Check if the wishlist is empty')
    def is_wishlist_empty(self):
        if self.is_element_present(self.LOCATORS.EMPTY_WISHLIST_CONTENT):
            empty_wishlist_title_text = self.find_element(self.LOCATORS.EMPTY_WISHLIST_TITLE).text
            return True, empty_wishlist_title_text
        return False, None

    @allure.step('Check if a product is present in the wishlist')
    def is_product_present(self):
        return self.is_element_present(self.LOCATORS.PRODUCT_CARD, 2)
