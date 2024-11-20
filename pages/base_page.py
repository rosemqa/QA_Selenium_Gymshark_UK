import time

import allure
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open_page(self):
        with allure.step(f'Open {self.url} page'):
            self.driver.get(self.url)

    def is_open(self, timeout=10):
        with (allure.step(f'Page {self.url} is open')):
            WebDriverWait(self.driver, timeout) \
                .until(EC.url_to_be(self.url),
                       message='Expected url {self.url} is not open, actual url {self.driver.current_url}')

    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout=10)\
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

    def move_mouse_by_offset(self, x_offset, y_offset):
        action = ActionChains(self.driver)
        action \
            .move_by_offset(x_offset, y_offset) \
            .perform()
