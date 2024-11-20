from selenium.webdriver.common.by import By


class PDPLocators:
    PRODUCT_PRICE = (By.CSS_SELECTOR, '[data-locator-id="pdp-totalValue-read"]>div')
    PRODUCT_COLOR = (By.CSS_SELECTOR, '.variants_colour__A3adN')

    PDP_ADD_TO_WISHLIST_BTN = (By.CSS_SELECTOR, '[data-locator-id="pdp-addToWishlist-add"]')
    SHARE_BTN = (By.CSS_SELECTOR, '[data-locator-id="pdp-share-select"]')
    LINK_COPIED_TOAST = (By.CSS_SELECTOR, '[data-locator-id="pdp-linkCopied-read"]')

    ADD_TO_BAG = (By.CSS_SELECTOR, '[data-locator-id="pdp-addToBag-submit"]')

    SIZE_SELECTOR_ITEM = (By.CSS_SELECTOR, '.add-to-cart_section__GygMh label')
    SIZE_GUIDE_BTN = (By.CSS_SELECTOR, '[data-locator-id="pdp-sizeGuideButton-select"]')
    COLOR_SELECTOR_ITEM = (By.CSS_SELECTOR, '.variants_variants__C9MOx a')
    CLOSE_SIZE_GUIDE_BTN = (By.CSS_SELECTOR, '[data-locator-id="infoSheet-close-size_guide-select"]')
    SELECT_SIZE_ERROR = (By.CSS_SELECTOR, '[data-locator-id="pdp-validation-read"]')

    REVIEWS_RATING_BTN = (By.CSS_SELECTOR, '[data-locator-id="pdp-reviews-rating-select"]')
    REVIEWS_TITLE = (By.CSS_SELECTOR, '[data-locator-id="pdp-reviews-title-read"]')
    SEE_MORE_REVIEWS_BTN = (By.CSS_SELECTOR, '[data-locator-id="pdp-reviews-seeMore-select"]')
    CLOSE_REVIEWS_BTN = (By.CSS_SELECTOR, '[data-locator-id="infoSheet-close-reviews-select"]')

    CLOSE_LOGIN_PROMPT_BTN = (By.CSS_SELECTOR, '[data-locator-id="loginPrompt-close-select"]')

    GALLERY_CAROUSEL = (By.CSS_SELECTOR, '.image-gallery_gallery__3npnc')
    PRODUCT_IMAGE = (By.CSS_SELECTOR, '[data-locator-id="pdp-page"] button img')
    IMAGE_SLIDER = (By.CSS_SELECTOR, '.image-index-slider_progress-pill___13Cg')
    IMAGE_SLIDER_UP = (By.CSS_SELECTOR, '[aria-label="Scroll up"]')
    IMAGE_SLIDER_DOWN = (By.CSS_SELECTOR, '[aria-label="Scroll down"]')
