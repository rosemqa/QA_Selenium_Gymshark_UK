from selenium.webdriver.common.by import By


class MainPageLocators:
    PREV_BTN = (By.CSS_SELECTOR, '[aria-label="Show previous"]')
    NEXT_BTN = (By.CSS_SELECTOR, '[aria-label="Show next"]')
    CAROUSEL_SLIDES = (By.CSS_SELECTOR, '[data-testid="As Seen On-carousel-list"] li')
