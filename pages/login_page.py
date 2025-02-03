import allure
from locators.login_locators import LoginLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    LOCATORS = LoginLocators()

    @allure.step('Enter email')
    def enter_email(self, email):
        self.find_element(self.LOCATORS.EMAIL).send_keys(email)

    def enter_password(self, password):
        with allure.step('Enter password'):
            self.find_element(self.LOCATORS.PASSWORD).send_keys(password)

    @allure.step('Click the Log In button')
    def click_login_button(self):
        self.find_element(self.LOCATORS.LOG_IN_BTN).click()

    @allure.step('Click the Show/Hide password button')
    def click_show_password_button(self):
        self.find_element(self.LOCATORS.SHOW_PASSWORD_BTN).click()

    @allure.step('Check if the password is shown or hidden')
    def is_password_masked(self):
        type_attribute = self.find_element(self.LOCATORS.PASSWORD).get_attribute('type')
        if type_attribute == 'password':
            return True
        elif type_attribute == 'text':
            return False

    @allure.step('Check if the Show Password tooltip is present')
    def is_show_password_tooltip_present(self):
        return self.is_element_present(self.LOCATORS.SHOW_PASSWORD_TOOLTIP)

    @allure.step('Check if the Hide Password tooltip is present')
    def is_hide_password_tooltip_present(self):
        return self.is_element_present(self.LOCATORS.HIDE_PASSWORD_TOOLTIP)

    @allure.step('Check if the username required error is present')
    def is_email_required_error_present(self):
        error = self.LOCATORS.EMAIL_REQUIRED_ERROR
        if self.is_element_present(error, 2):
            return True, self.find_element(error).text
        return False, None

    @allure.step('Check if the password required error is present')
    def is_password_required_error_present(self):
        error = self.LOCATORS.PASSWORD_REQUIRED_ERROR
        if self.is_element_present(error, 2):
            return True, self.find_element(error).text
        return False, None

    @allure.step('Check if the error for incorrect email format is present')
    def is_email_invalid_error_present(self):
        error = self.LOCATORS.EMAIL_INVALID_ERROR
        if self.is_element_present(error, 2):
            return True, self.find_element(error).text
        return False, None

    @allure.step('Check if the wrong credentials error is present')
    def is_wrong_credentials_error_present(self):
        error = self.LOCATORS.WRONG_CREDENTIALS
        if self.is_element_present(error, 2):
            return True, self.find_element(error).text
        return False, None
