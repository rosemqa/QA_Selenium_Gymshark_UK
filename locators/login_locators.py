from selenium.webdriver.common.by import By


class LoginLocators:
    EMAIL = (By.CSS_SELECTOR, '#username')
    PASSWORD = (By.CSS_SELECTOR, '#password')
    LOG_IN_BTN = (By.CSS_SELECTOR, '[type="submit"][name="action"]')
    SHOW_PASSWORD_BTN = (By.CSS_SELECTOR, '[role="switch"]')
    SHOW_PASSWORD_TOOLTIP = (By.CSS_SELECTOR, 'span.show-password-tooltip')
    HIDE_PASSWORD_TOOLTIP = (By.CSS_SELECTOR, 'span.hide-password-tooltip')
    FORGOT_PASSWORD_LINK = (By.CSS_SELECTOR, '[method="POST"] p a')
    SIGN_UP_LINK = (By.CSS_SELECTOR, '.ulp-alternate-action a')
    EMAIL_REQUIRED_ERROR = (By.CSS_SELECTOR, '#error-cs-email-required')
    EMAIL_INVALID_ERROR = (By.CSS_SELECTOR, '#error-cs-email-invalid')
    PASSWORD_REQUIRED_ERROR = (By.CSS_SELECTOR, '#error-cs-password-required')
    WRONG_CREDENTIALS = (By.CSS_SELECTOR, '#error-element-password')
