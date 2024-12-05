from selenium.webdriver.common.by import By


class BagLocators:
    MINI_BAG_SHEET = (By.CSS_SELECTOR, '[data-locator-id="miniBag-component"]')
    CLOSE_BAG_BTN = (By.CSS_SELECTOR, '[data-locator-id="miniBag-closeButton-select"]')
    ENTER_CODE_FIELD = (By.CSS_SELECTOR, '#code')
    APPLY_CODE_BUTTON = (By.CSS_SELECTOR, '[data-locator-id="miniBag"] button')
    CODE_ERROR = (By.CSS_SELECTOR, '#code-error')
    CHECKOUT_BTN = (By.CSS_SELECTOR, '[data-locator-id="miniBag-checkout-select"]')
    DELETE_BTN = (By.CSS_SELECTOR, '[aria-label="remove from bag"]')
    ADD_TO_WISHLIST = (By.CSS_SELECTOR, '[data-locator-id="miniBag-component"] button[aria-label="add to wishlist"]')
    QUANTITY_SELECTOR = (By.CSS_SELECTOR, '[class*="qty-selector_dropdown"]')
    SUBTOTAL_VALUE = (By.CSS_SELECTOR, '[data-locator-id="miniBag-subTotalValue-read"]')
    TOTAL_VALUE = (By.CSS_SELECTOR, '[data-locator-id="miniBag-totalValue-read"]')
    PRODUCT_TITLE = (By.CSS_SELECTOR, '[role="group"] h2')
    PRODUCT_COLOR_AND_SIZE = (By.CSS_SELECTOR, '.product-card_selected-option__steV8')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.price_price___2MY1')
    DELIVERY_INFO_BUTTON = (By.CSS_SELECTOR, '[data-locator-id="bag-infoButton-deliveryOptions-select"]')
    DELIVERY_INFO_SHEET = (By.CSS_SELECTOR, '[data-locator-id="infoSheet-container-deliveryOptions-read"]')
    EMPTY_BAG_TEXT = (By.CSS_SELECTOR, '[data-locator-id="miniBag-miniBagEmpty-read"] h2')
    PRODUCT_REMOVED_TOAST = (By.CSS_SELECTOR, '[class*="snackbox_text"]')
    UNDO_DELETION_BTN = (By.CSS_SELECTOR, '[aria-label="Add Product"]')
    PRODUCT_ITEM = (By.CSS_SELECTOR, '[data-locator-id*="miniBag-miniBagItem"]')
