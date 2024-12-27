from selenium.webdriver.common.by import By


class AccountLocators:
    LOG_OUT_LINK = (By.CSS_SELECTOR, '[data-locator-id="account-logoutButton-select"]')
    NO_ORDERS_TITLE = (By.CSS_SELECTOR, '[class*="orders-page_empty-view_"] h4')
    VIEW_ADDRESS_BOOK_LINK = (By.CSS_SELECTOR, '[data-locator-id="address-viewAllAddresses-select"]')


class AddressBookLocators:
    ADD_ADDRESS_BTN = (By.CSS_SELECTOR, '[data-locator-id="address-newAddress-select"]')
    EMPTY_ADDRESS_BOOK_TITLE = (By.CSS_SELECTOR, '[data-locator-id="address-emptyViewTitle-read"]')

    # FORM
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, '#firstName')
    LAST_NAME_INPUT = (By.CSS_SELECTOR, '#lastName')
    ADDRESS_1_INPUT = (By.CSS_SELECTOR, '#address1')
    ADDRESS_2_INPUT = (By.CSS_SELECTOR, '#address2')
    CITY_INPUT = (By.CSS_SELECTOR, '#city')
    COUNTRY_DROPDOWN = (By.CSS_SELECTOR, '#country')
    STATE_DROPDOWN = (By.CSS_SELECTOR, '#country-provinces')
    POST_CODE_INPUT = (By.CSS_SELECTOR, '#zip')
    PHONE_INPUT = (By.CSS_SELECTOR, '#phone')
    DEFAULT_ADDRESS_CHECKBOX = (By.CSS_SELECTOR, '[data-locator-id="address-defaultAddress-select"]')
    SAVE_ADDRESS_BTN = (By.CSS_SELECTOR, '[data-locator-id="address-saveAddress-select"]')
    CANCEL_ADDRESS_BTN = (By.CSS_SELECTOR, '[data-locator-id="address-cancelAddress-select"]')
    # ADDRESS BOOK ITEM
    ADDRESS_CARD = (By.CSS_SELECTOR, '[data-locator-id*="address-addressItem-"]')
    ADDRESS_DETAILS_ITEM = (By.CSS_SELECTOR, '[data-locator-id*="address-addressItem-"] p span')
    EDIT_ADDRESS_BTN = (By.CSS_SELECTOR, '[data-locator-id*="address-edit-"]')
    DELETE_ADDRESS_BTN = (By.CSS_SELECTOR, '[data-locator-id*="address-delete-"]')
    NAKE_ADDRESS_MAIN_RADIO_BTN = (By.CSS_SELECTOR, '[class*="address-card_actions_"] label')
    # MAIN ADDRESS SECTION
    MAIN_ADDRESS_OUTPUT = (By.CSS_SELECTOR, '[data-locator-id="address-mainAddress-read"]')
    MAIN_ADDRESS_DETAILS_ITEM = (By.CSS_SELECTOR, '[data-locator-id="address-mainAddress-read"] span')

