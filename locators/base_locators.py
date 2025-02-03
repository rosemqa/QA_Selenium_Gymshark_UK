from selenium.webdriver.common.by import By


class BaseLocators:
    HEADER_LOGO = (By.CSS_SELECTOR, '[data-locator-id="header-logo-select"]')
    ACCOUNT_NAME = (By.CSS_SELECTOR, '[data-locator-id="secondaryLinks-account-select"]')
    SEARCH_ICON = (By.CSS_SELECTOR, '[data-locator-id="header-searchContainer-read"]')
    WISHLIST_ICON = (By.CSS_SELECTOR, '.header_action-bar-item-wrap__m_Rhz [title="Wishlist"]')
    ACCOUNT_ICON = (By.CSS_SELECTOR, '[aria-label="View your account"]')
    BAG_ICON = (By.CSS_SELECTOR, '[data-locator-id="header-miniBag-select"]')
    BAG_COUNT = (By.CSS_SELECTOR, '#cart-count')
    CLOSE_COOKIES_BTN = (By.CSS_SELECTOR, '.banner-close-button')
    GEOLOCATION_CONFIRMATION_CLOSE_BTN = (By.CSS_SELECTOR, '[data-locator-id="storeSelector-close-select"]')
    WISHLIST_TOAST = (By.CSS_SELECTOR, '[data-locator-id="snackbox-component"]')
    SIGN_IN_TOOLTIP = (By.CSS_SELECTOR, '[class*="tooltip_value"]')
    # SEARCH MODAL
    SEARCH_INPUT = (By.CSS_SELECTOR, '[data-locator-id="search-search-enter"]')
    SEARCH_MODAL = (By.CSS_SELECTOR, '[data-locator-id="searchModal-component"]')
    CLOSE_SEARCH_BTN = (By.CSS_SELECTOR, '[data-locator-id="searchModal-search-close"]:nth-child(3)')
    CLEAR_RECENT_SEARCHES_BTN = (By.CSS_SELECTOR, '[data-locator-id="searchModal-clearRecentSearches-select"]')
    RECENT_SEARCH_ITEM = (By.CSS_SELECTOR, '[data-testid="recent-search-link"]')
    CLEAR_SEARCH_INPUT_BTN = (By.CSS_SELECTOR, '[aria-label="Clear your search"]')
    CLEAR_RECENTLY_VIEWED_BTN = (By.CSS_SELECTOR, '[data-locator-id="searchModal-clearRecentlyViewed-select"]')
    RECENTLY_VIEWED_ITEM = (By.CSS_SELECTOR, '[data-locator-id*="searchModal-recentlyViewed-"]')
    VIEW_ALL_LINK = (By.CSS_SELECTOR, '[data-locator-id="searchModal-viewAll-select"]')
    VIEW_ALL_NAME = (By.CSS_SELECTOR, '[data-locator-id="searchModal-viewAll-select"] span')
    NO_RESULTS_ERROR = (By.CSS_SELECTOR, '[data-testid="no-results-error-message"]')
