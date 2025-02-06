import allure
from data.links import URL
from pages.main_page import MainPage


@allure.epic('Main page')
class TestMainPage:
    @allure.description('Can move the carousel using the Show Next and Show Previous buttons')
    def test_carousel(self, driver):
        page = MainPage(driver, URL.MAIN_PAGE)
        page.open_page()

        next_slide, initial_slide = page.check_carousel()
        assert next_slide, 'Show Next button does not move the carousel'
        assert initial_slide, 'Show Previous button does not move the carousel'
