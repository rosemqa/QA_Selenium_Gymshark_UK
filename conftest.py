import pytest
from selenium import webdriver


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    print('\nStart Chrome browser')
    # driver.maximize_window()
    driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()
    print('\nQuit browser')
