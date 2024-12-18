from selenium.webdriver.common.by import By


class WishListLocators:
    PRODUCT_CARD = (By.CSS_SELECTOR, '[data-locator-id*="plp-productCard-"]')
    PRODUCT_CARD_WISHLIST_ICON = (By.CSS_SELECTOR, 'button[aria-label="remove from wishlist"]')
    PRODUCT_TITLE = (By.CSS_SELECTOR, '[data-locator-id*="plp-productTitle-"]')
    PRODUCT_COLOR = (By.CSS_SELECTOR, '[data-locator-id*="plp-productColour-"]')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '[class*="product-card_product-price"]')
    PRODUCT_COUNT = (By.CSS_SELECTOR, '[data-locator-id="plp-productCount-read"]')

    SIZE_DROPDOWN = (By.CSS_SELECTOR, '[data-locator-id*="plp-sizeDropdown-"]')
    SIZE_DROPDOWN_ITEM = (By.CSS_SELECTOR, '[data-locator-id*="plp-sizeDropdownOption-"]')
    ADD_TO_BAG_BTN = (By.CSS_SELECTOR, '[data-locator-id*="plp-addToBag-"]')

    REMOVE_ALL_ITEMS_BTN = (By.CSS_SELECTOR, '[data-locator-id="wishlist-removeAllItems-select"] .icon-delete')
    MORE_MENU = (By.CSS_SELECTOR, '[aria-label="more-icon"]')
    MORE_MENU_ADD_TO_BAG = (By.CSS_SELECTOR, '[data-locator-id="wishlist-actionMenu-addToBag-select"]')
    MORE_MENU_REMOVE = (By.CSS_SELECTOR, '[data-locator-id="wishlist-actionMenu-remove-select"]')
    REMOVE_ALL_YES_BTN = (By.CSS_SELECTOR, '[data-locator-id="wishlistRemove-confirm-select"]')
    REMOVE_ALL_NO_BTN = (By.CSS_SELECTOR, '[data-locator-id="wishlistRemove-cancel-select"]')
    WISHLIST_TOAST = (By.CSS_SELECTOR, '[data-locator-id="snackbox-component"]')
    WISHLIST_TOAST_TEXT = (By.CSS_SELECTOR, '[data-locator-id="snackbox-component"]>p')
    WISHLIST_TOAST_ACTION_BTN = (By.CSS_SELECTOR, '[data-locator-id*="snackbox-action-"]')
    # REMOVE_TOAST_UNDO_BTN = (By.CSS_SELECTOR, '[data-locator-id="snackbox-action-button-select"]')
    # REMOVE_TOAST_VIEW_LINK = (By.CSS_SELECTOR, '[data-locator-id="snackbox-action-link-select"]')
    EMPTY_WISHLIST_CONTENT = (By.CSS_SELECTOR, '[data-testid="wishlist__empty-view"]')
    EMPTY_WISHLIST_TITLE = (By.CSS_SELECTOR, '[data-testid="wishlist__empty-view"] h4:nth-child(2)')
