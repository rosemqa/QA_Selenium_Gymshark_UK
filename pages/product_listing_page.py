import random
import time
import allure
from locators.plp_locators import PLPLocators
from pages.base_page import BasePage


class ProductListingPage(BasePage):
    LOCATORS = PLPLocators

    def get_product_size(self):
        card = self.find_elements(self.LOCATORS.PRODUCT_CARD)[0]
        self.move_to_element(card)
        time.sleep(1)
        size = card.find_elements(*self.LOCATORS.PRODUCT_SIZE)[3]
        print(size.text)
        size.click()
        return size.text

    def get_product_title_text(self):
        print(self.find_element(self.LOCATORS.PRODUCT_TITLE).text)
        return self.find_element(self.LOCATORS.PRODUCT_TITLE).text

    def get_product_color_text(self):
        print(self.find_element(self.LOCATORS.PRODUCT_COLOR).text)
        return self.find_element(self.LOCATORS.PRODUCT_COLOR).text

    def get_product_price_value(self):
        return float(self.find_element(self.LOCATORS.PRODUCT_PRICE).text.split('£')[1])

    def get_total_product_count_value(self):
        return int(self.find_element(self.LOCATORS.TOTAL_PRODUCT_COUNT).text.split()[0])

    @allure.step('Get price list sorted in asc/desc order')
    def get_price_list(self):
        prices = self.find_elements(self.LOCATORS.PRODUCT_PRICE)
        price_list = [float(price.text.split('£')[1]) for price in prices]
        return sorted(price_list), sorted(price_list, reverse=True)

    @allure.step('Click the Load More button and get the products quantity before and after')
    def load_more(self):
        products_quantity_before = len(self.find_elements(self.LOCATORS.PRODUCT_CARD))
        button = self.LOCATORS.LOAD_MORE_BTN
        self.move_to_element(button)
        self.find_element(button).click()
        time.sleep(2)
        products_quantity_after = len(self.find_elements(self.LOCATORS.PRODUCT_CARD))
        return products_quantity_before < products_quantity_after

    @allure.step('Click the View More button and get the number of displayed products')
    def view_all_products(self):
        quantity_of_all_products = int(self.find_element(self.LOCATORS.PAGINATION_TEXT).text.split()[5])
        button = self.LOCATORS.VIEW_ALL_BTN
        self.move_to_element(button)
        self.find_element(button).click()
        time.sleep(2)
        products_quantity = len(self.find_elements(self.LOCATORS.PRODUCT_CARD))
        return quantity_of_all_products == products_quantity

    @allure.step('Sort by price asc and get price list')
    def sort_by_price_asc(self):
        self.find_element(self.LOCATORS.SORT_BY_PRICE_ASC).click()
        time.sleep(2)
        prices = self.find_elements(self.LOCATORS.PRODUCT_PRICE)
        price_list = [float(price.text.split('£')[1]) for price in prices]
        return price_list == sorted(price_list)

    @allure.step('Sort by price desc and get price list')
    def sort_by_price_desc(self):
        sort_by_price_desc = self.LOCATORS.SORT_BY_PRICE_DESC
        self.move_to_element(sort_by_price_desc)
        self.find_element(sort_by_price_desc).click()
        time.sleep(1)
        prices = self.find_elements(self.LOCATORS.PRODUCT_PRICE)
        price_list = [float(price.text.split('£')[1]) for price in prices]
        return price_list == sorted(price_list, reverse=True)

    @allure.step('Click the Newest under Sort By')
    def sort_by_newest(self):
        self.move_to_element(self.LOCATORS.SORT_BY_NEWEST)
        self.find_element(self.LOCATORS.SORT_BY_NEWEST).click()
        time.sleep(1)

    @allure.step('Check if new products are listed first')
    def check_sorted_by_newest(self):
        new_products = []
        product_cards = self.find_elements(self.LOCATORS.PRODUCT_CARD)
        for card in product_cards:
            if "NEW" in card.text:
                new_products.append(card)
        return len(new_products), product_cards[:len(new_products)] == new_products

    @allure.step('Select random price range filter and get min and max prices')
    def select_price_filter(self):
        price_category = self.LOCATORS.PRICE_FILTER_DROPDOWN
        price_range = self.LOCATORS.PRICE_FILTER_ITEM
        random_price_range = random.randint(1, 2)

        self.move_to_element(price_category)
        self.find_element(price_category).click()
        self.find_elements(price_range)[random_price_range].click()
        min_price = float(self.find_elements(price_range)[random_price_range].text.split(' -')[0].lstrip('£'))
        max_price = float(self.find_elements(price_range)[random_price_range].text.split('- ')[1].lstrip('£'))
        time.sleep(2)
        return min_price, max_price

    @allure.step('Click Clear All')
    def clear_all_filters(self):
        self.find_element(self.LOCATORS.CLEAR_ALL_FILTERS).click()
        time.sleep(2)

    @allure.step('Click Add To Wishlist icon')
    def add_to_wishlist(self):
        self.move_to_element(self.LOCATORS.ADD_TO_WISHLIST)
        self.find_element(self.LOCATORS.ADD_TO_WISHLIST).click()
