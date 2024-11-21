import allure
import time
import random
from locators.pdp import PDPLocators
from pages.base_page import BasePage
import pyperclip


class ProductPage(BasePage):
    LOCATORS = PDPLocators()

    def get_product_color_text(self):
        return self.find_element(self.LOCATORS.PRODUCT_COLOR).text

    def get_product_price_value(self):
        return self.find_element(self.LOCATORS.PRODUCT_PRICE).text.lstrip('£')

    def get_product_image_src(self):
        return self.find_element(self.LOCATORS.PRODUCT_IMAGE).get_attribute('src')

    def get_size_error_text(self):
        return self.find_element(self.LOCATORS.SELECT_SIZE_ERROR).text

    def get_clipboard_data(self):
        time.sleep(1)
        clip_data = self.driver.execute_script("""
                return navigator.clipboard.readText().then(text => {
                    return text;
                }).catch(err => {
                    console.error('Ошибка чтения буфера обмена: ', err);
                    return '';
                });
            """)
        print(clip_data)
        return clip_data

    @allure.step('Click Share button and get clipboard content')
    def click_share_button(self):
        self.find_element(self.LOCATORS.SHARE_BTN).click()
        clipboard_content = pyperclip.paste()
        return clipboard_content

    @allure.step('Select a random color')
    def select_random_color(self):
        self.find_elements(self.LOCATORS.COLOR_SELECTOR_ITEM)[random.randint(1, 2)].click()
        time.sleep(1)
        return self.get_product_color_text(), self.get_product_image_src()

    @allure.step('Select a random size')
    def select_random_size(self):
        size = self.find_elements(self.LOCATORS.SIZE_SELECTOR_ITEM)[random.randint(0, 5)]
        size.click()
        return size.text

    @allure.step('Click the size guide button')
    def open_size_guide(self):
        self.find_element(self.LOCATORS.SIZE_GUIDE_BTN).click()

    @allure.step('Click the close button in the size guide sheet')
    def close_size_guide(self):
        self.find_element(self.LOCATORS.CLOSE_SIZE_GUIDE_BTN).click()

    @allure.step('Click the close button in the login prompt modal')
    def close_login_prompt(self):
        self.find_element(self.LOCATORS.CLOSE_LOGIN_PROMPT_BTN).click()

    @allure.step('Click Add To Bag button')
    def add_to_bag(self):
        self.find_element(self.LOCATORS.ADD_TO_BAG).click()

    @allure.step('Click the product rating button')
    def click_rating_button(self):
        self.find_element(self.LOCATORS.REVIEWS_RATING_BTN).click()

    @allure.step('Click the See More Reviews button')
    def click_more_reviews_button(self):
        more_reviews_button = self.LOCATORS.SEE_MORE_REVIEWS_BTN
        time.sleep(1)
        self.move_to_element(more_reviews_button)
        self.find_element(more_reviews_button).click()

    @allure.step('Click the close button in the review sheet')
    def close_review_sheet(self):
        self.find_element(self.LOCATORS.CLOSE_REVIEWS_BTN).click()

    @allure.step('Click Add To Wishlist button (under the product title)')
    def click_add_to_wishlist_button(self):
        self.find_element(self.LOCATORS.PDP_ADD_TO_WISHLIST_BTN).click()

    def check_image_slider(self):
        self.scroll_down_image_carousel()
        value_before = self.find_element(self.LOCATORS.IMAGE_SLIDER).get_attribute('style').split()[1].rstrip('px;')
        with allure.step('Click the image slider down button'):
            self.find_element(self.LOCATORS.IMAGE_SLIDER_DOWN).click()
        time.sleep(1)
        value_after_down = self.find_element(self.LOCATORS.IMAGE_SLIDER).get_attribute('style').split()[1].rstrip('px;')
        with allure.step('Click the image slider up button'):
            self.find_element(self.LOCATORS.IMAGE_SLIDER_UP).click()
        time.sleep(1)
        value_after_up = self.find_element(self.LOCATORS.IMAGE_SLIDER).get_attribute('style').split()[1].rstrip('px;')
        return float(value_before), float(value_after_down), float(value_after_up)

    @allure.step('Scroll down the image carousel')
    def scroll_down_image_carousel(self):
        carousel = self.find_element(self.LOCATORS.GALLERY_CAROUSEL)
        scroll_amount = 350
        self.driver.execute_script("arguments[0].scrollTop += arguments[1];", carousel, scroll_amount)

    @allure.step('Check if the size guide sheet open')
    def is_size_guide_open(self):
        time.sleep(1)
        return self.is_element_present(self.LOCATORS.CLOSE_SIZE_GUIDE_BTN, 1)

    @allure.step('Check if the reviews sheet open')
    def is_reviews_sheet_open(self):
        time.sleep(1)
        return self.is_element_present(self.LOCATORS.CLOSE_REVIEWS_BTN, timeout=1)

    @allure.step('Check if the reviews title in the viewport')
    def is_reviews_title_in_viewport(self):
        title = self.find_element(self.LOCATORS.REVIEWS_TITLE)
        time.sleep(1)
        is_in_viewport = self.driver.execute_script("""
            var elem = arguments[0];
            var rect = elem.getBoundingClientRect();
            return (
                rect.top >= 0 &&
                rect.left >= 0 &&
                rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
                rect.right <= (window.innerWidth || document.documentElement.clientWidth)
            );
        """, title)
        return is_in_viewport

    @allure.step('Check if the size error present')
    def is_size_error_present(self):
        return self.is_element_present(self.LOCATORS.SELECT_SIZE_ERROR, 1)

    @allure.step('Check if the login prompt modal open')
    def is_login_prompt_open(self):
        time.sleep(1)
        return self.is_element_present(self.LOCATORS.CLOSE_LOGIN_PROMPT_BTN, 1)

    @allure.step('Check if the toast appears when clicking the Share button')
    def link_copied_toast_appears(self):
        return self.is_element_present(self.LOCATORS.LINK_COPIED_TOAST)

    @allure.step('Check if the link copied toast disappears after 3 seconds')
    def link_copied_toast_disappears(self):
        return self.is_disappeared(self.LOCATORS.LINK_COPIED_TOAST, 4)
