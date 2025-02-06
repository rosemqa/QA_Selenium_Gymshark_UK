import allure
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    LOCATORS = MainPageLocators

    @allure.step('Click the Show Next button above the carousel')
    def click_carousel_next_button(self):
        self.move_to_element(self.LOCATORS.NEXT_BTN)
        self.find_element(self.LOCATORS.NEXT_BTN).click()

    @allure.step('Click the Show Previous button above the carousel')
    def click_carousel_prev_button(self):
        self.find_element(self.LOCATORS.PREV_BTN).click()

    @allure.step('Check if the slides move forward and backward')
    def check_carousel(self):
        slides = self.find_elements(self.LOCATORS.CAROUSEL_SLIDES)
        self.click_carousel_next_button()
        next_slide = slides[1].get_attribute('data-is-active')
        self.click_carousel_prev_button()
        initial_slide = slides[0].get_attribute('data-is-active')
        return next_slide == 'true', initial_slide == 'true'
