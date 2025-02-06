from selenium.webdriver.common.by import By


class PLPLocators:
    PRODUCT_CARD = (By.CSS_SELECTOR, '[class*="product-card_image-wrap"]')
    PRODUCT_TITLE = (By.CSS_SELECTOR, '[data-locator-id*="plp-productTitle"]')
    PRODUCT_COLOR = (By.CSS_SELECTOR, '[data-locator-id*="plp-productColour"]')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '[class*="product-card_product-price"]')
    PRODUCT_SIZE = (By.CSS_SELECTOR, '[data-locator-id*="plp-size"]')
    PRODUCT_TAG_NEW = (By.CSS_SELECTOR, '[data-locator-id="plp-productTag-new-read"]')
    ADD_TO_WISHLIST = (By.CSS_SELECTOR, '[data-locator-id*="plp-productCardWishlist"]')

    TOTAL_PRODUCT_COUNT = (By.CSS_SELECTOR, '[data-locator-id="plp-productCount-read"]')

    CLEAR_ALL_FILTERS = (By.CSS_SELECTOR, '[data-locator-id="filtersPanel-clearAll-select"]')
    SORT_BY_PRICE_ASC = (By.CSS_SELECTOR, '[data-locator-id="filtersPanel-filterOptionLabel-SORTLTH-select"]')
    SORT_BY_PRICE_DESC = (By.CSS_SELECTOR, '[data-locator-id="filtersPanel-filterOptionLabel-SORTHTL-select"]')
    SORT_BY_NEWEST = (By.CSS_SELECTOR, '[data-locator-id="filtersPanel-filterOptionLabel-NEWEST-select"]')
    PRICE_FILTER_DROPDOWN = (By.CSS_SELECTOR, '[data-locator-id="filtersPanel-filterCategory-PRICE-select"]')
    PRICE_FILTER_ITEM = (By.CSS_SELECTOR, '[for*="price-"]')

    LOAD_MORE_BTN = (By.CSS_SELECTOR, 'a[class*="button_button"]')
    VIEW_ALL_BTN = (By.CSS_SELECTOR, '[class*="pagination_view-all"]')
    PAGINATION_TEXT = (By.CSS_SELECTOR, '[class*="pagination_pagination-text"]')
