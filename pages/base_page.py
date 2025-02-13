import time
import allure
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.base_locators import BaseLocators


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open_page(self):
        with allure.step(f'Open {self.url} page'):
            self.driver.get(self.url)
            time.sleep(2)
            if self.is_element_present(BaseLocators.GEOLOCATION_CONFIRMATION_CLOSE_BTN, 1):
                self.close_geolocation_confirmation()
            if self.is_element_present(BaseLocators.CLOSE_COOKIES_BTN, 1):
                self.close_cookies_banner()
                WebDriverWait(self.driver, 2) \
                    .until(EC.invisibility_of_element_located(BaseLocators.CLOSE_COOKIES_BTN))

    def is_open(self, timeout=5):
        with (allure.step(f'Page {self.url} is open')):
            WebDriverWait(self.driver, timeout) \
                .until(EC.url_to_be(self.url),
                       message=f'Expected url {self.url} is not open, actual url {self.driver.current_url}')

    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout)\
            .until(EC.element_to_be_clickable(locator), message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout) \
            .until(EC.presence_of_all_elements_located(locator), message=f"Can't find element by locator {locator}")

    def is_element_present(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            return False
        return True

    def is_disappeared(self, locator, timeout=1):
        try:
            WebDriverWait(self.driver, timeout).until_not(EC.visibility_of_element_located(locator))
        except TimeoutException:
            return False
        return True

    def get_current_url(self, timeout=1):
        time.sleep(timeout)
        return self.driver.current_url

    def move_to_element(self, locator):
        """Move cursor to element"""
        action = ActionChains(self.driver)
        element = self.find_element(locator)
        action.move_to_element(element).perform()

    def scroll_to_element(self, locator):
        """Scroll to element"""
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Select item in drop-down list by visible text')
    def select_item_in_dropdown_by_text(self, locator, text):
        """Select item in drop-down list by visible text"""
        Select(self.find_element(locator)).select_by_visible_text(text)
        return text

    @allure.step('Select item in drop-down list by index, get the selected element text')
    def select_item_in_dropdown_by_index(self, locator, index):
        """Select item in drop-down list by index"""
        select = Select(self.find_element(locator))
        select.select_by_index(index)
        element_text = select.first_selected_option.text
        return element_text

    def move_mouse_by_offset(self, x_offset, y_offset):
        action = ActionChains(self.driver)
        action \
            .move_by_offset(x_offset, y_offset) \
            .perform()

    def close_geolocation_confirmation(self):
        self.find_element(BaseLocators.GEOLOCATION_CONFIRMATION_CLOSE_BTN).click()

    @allure.step('Close the Cookies banner')
    def close_cookies_banner(self):
        self.find_element(BaseLocators.CLOSE_COOKIES_BTN).click()

    @allure.step('Get the "logged-in" attribute of account icon')
    def check_account_icon(self):
        account = self.find_element(BaseLocators.ACCOUNT_NAME)
        account_attribute = account.get_attribute('data-user-logged-in')
        if account_attribute == "true":
            return True, account.text
        elif account_attribute == 'false':
            return False, account.text

    # ACTIONS
    @allure.step('Get text in the Sign In tooltip')
    def get_sign_in_tooltip_text(self):
        return self.find_element(BaseLocators.SIGN_IN_TOOLTIP).text

    @allure.step('Click the Bag icon in the header')
    def open_mini_bag(self):
        self.find_element(BaseLocators.BAG_ICON).click()

    @allure.step('Check if the bag count icon present')
    def is_bag_count_icon_present(self):
        bag_count_icon = BaseLocators.BAG_COUNT
        if self.is_element_present(bag_count_icon):
            count_value = int(self.find_element(bag_count_icon).text)
            return True, count_value
        return False, None

    @allure.step('Check if the wishlist toast present')
    def is_wishlist_toast_present(self):
        return self.is_element_present(BaseLocators.WISHLIST_TOAST)

    @allure.step('Check if the wishlist toast disappears after 5 seconds')
    def is_wishlist_toast_disappeared(self):
        return self.is_disappeared(BaseLocators.WISHLIST_TOAST, 6)

    @allure.step('Check if the Sign In tooltip present')
    def is_sign_in_tooltip_present(self):
        return self.is_element_present(BaseLocators.SIGN_IN_TOOLTIP)

    @allure.step('Check if the Sign In tooltip disappears after 5 seconds')
    def is_sign_in_tooltip_disappeared(self):
        return self.is_disappeared(BaseLocators.SIGN_IN_TOOLTIP, 6)
