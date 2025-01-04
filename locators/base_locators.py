from selenium.webdriver.common.by import By


class BaseLocators:
    HEADER_LOGO = (By.CSS_SELECTOR, '[data-locator-id="header-logo-select"]')
    ACCOUNT_NAME = (By.CSS_SELECTOR, '[data-locator-id="secondaryLinks-account-select"]')
    SEARCH_ICON = (By.CSS_SELECTOR, '[data-locator-id="search-searchTrigger-select"]')
    WISHLIST_ICON = (By.CSS_SELECTOR, '.header_action-bar-item-wrap__m_Rhz [title="Wishlist"]')
    ACCOUNT_ICON = (By.CSS_SELECTOR, '[aria-label="View your account"]')
    BAG_ICON = (By.CSS_SELECTOR, '[data-locator-id="header-miniBag-select"]')
    BAG_COUNT = (By.CSS_SELECTOR, '#cart-count')
    CLOSE_COOKIES_BTN = (By.CSS_SELECTOR, '.banner-close-button')
    GEOLOCATION_CONFIRMATION_CLOSE_BTN = (By.CSS_SELECTOR, '[data-locator-id="storeSelector-close-select"]')
    WISHLIST_TOAST = (By.CSS_SELECTOR, '[data-locator-id="snackbox-component"]')
    SIGN_IN_TOOLTIP = (By.CSS_SELECTOR, '[class*="tooltip_value"]')
