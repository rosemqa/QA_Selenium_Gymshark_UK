import time

import allure
from locators.base_locators import BaseLocators
from pages.base_page import BasePage


class SearchModal(BasePage):
    LOCATORS = BaseLocators

    @allure.step('Get the recent search item text')
    def get_recent_search_item_text(self):
        return self.find_element(self.LOCATORS.RECENT_SEARCH_ITEM).text.lower()

    @allure.step('Get the recent search item link')
    def get_recent_search_item_link(self):
        return self.find_element(self.LOCATORS.RECENT_SEARCH_ITEM).get_attribute('href')

    @allure.step('Get the recently viewed link')
    def get_recently_viewed_link(self):
        return self.find_element(self.LOCATORS.RECENTLY_VIEWED_ITEM).get_attribute('href')

    @allure.step('Get the no results error text')
    def get_no_results_error_text(self):
        return self.find_element(self.LOCATORS.NO_RESULTS_ERROR).text

    @allure.step('Click the search icon and get the placeholder text in the search field')
    def click_header_search(self):
        self.find_element(self.LOCATORS.SEARCH_ICON).click()
        placeholder_text = self.find_element(self.LOCATORS.SEARCH_INPUT).get_attribute('placeholder')
        return placeholder_text

    @allure.step('Click the Close icon in the Search modal')
    def close_search_modal(self):
        self.find_element(self.LOCATORS.CLOSE_SEARCH_BTN).click()

    @allure.step('Enter the search query into the search field')
    def enter_search_query(self, search_query):
        self.find_element(self.LOCATORS.SEARCH_INPUT).send_keys(search_query)

    @allure.step('Click the Close icon in the search field')
    def clear_search_field(self):
        self.find_element(self.LOCATORS.CLEAR_SEARCH_INPUT_BTN).click()
        search_input_value = self.find_element(self.LOCATORS.SEARCH_INPUT).get_attribute('value')
        return search_input_value == ""

    @allure.step('Click View All link')
    def click_view_all_link(self):
        view_all_name = self.find_element(self.LOCATORS.VIEW_ALL_NAME).text
        self.find_element(self.LOCATORS.VIEW_ALL_LINK).click()
        time.sleep(1)
        return view_all_name.lower()

    @allure.step('Click the Clear button in the recent searches and check if recent searches is disappeared')
    def clear_recent_searches(self):
        self.find_element(self.LOCATORS.CLEAR_RECENT_SEARCHES_BTN).click()
        return self.is_disappeared(self.LOCATORS.CLEAR_RECENT_SEARCHES_BTN)

    @allure.step('Click the Clear button in the recently viewed and check if recently viewed is disappeared')
    def clear_recently_viewed(self):
        self.find_element(self.LOCATORS.CLEAR_RECENTLY_VIEWED_BTN).click()
        return self.is_disappeared(self.LOCATORS.CLEAR_RECENTLY_VIEWED_BTN)

    @allure.step('Check if the search modal is closed')
    def is_search_modal_closed(self):
        return self.is_disappeared(self.LOCATORS.SEARCH_MODAL)
