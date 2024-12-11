from selenium.webdriver.common.by import By


class PLPLocators:
    PRODUCT_CARD = (By.CSS_SELECTOR, '[data-locator-id*="plp-productCard-"]')
    PRODUCT_TITLE = (By.CSS_SELECTOR, '[data-locator-id*="plp-productTitle"]')
    PRODUCT_COLOR = (By.CSS_SELECTOR, '[data-locator-id*="plp-productColour"]')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '[class*="product-card_product-price"]')
    PRODUCT_SIZE = (By.CSS_SELECTOR, '[data-locator-id*="plp-size"]')
    CLEAR_ALL_FILTERS = (By.CSS_SELECTOR, '[data-locator-id="filtersPanel-clearAll-select"]')
    SORT_BY_PRICE_ASC = (By.CSS_SELECTOR, '[data-locator-id="filtersPanel-filterOptionLabel-SORTLTH-select"]')
    SORT_BY_PRICE_DESC = (By.CSS_SELECTOR, '[data-locator-id="filtersPanel-filterOptionLabel-SORTHTL-select"]')
    PRODUCT_TAG_NEW = (By.CSS_SELECTOR, '[data-locator-id="plp-productTag-new-read"]')
    LOAD_MORE_BTN = (By.CSS_SELECTOR, 'a[class*="button_button"]')
    