import time
import allure
import pytest
from datetime import datetime
from selenium import webdriver
from data.data import AutData
from data.links import URL
from pages.account_page import AccountAddressBook
from pages.login_page import LoginPage
from pages.product_listing_page import ProductListingPage
from pages.product_page import ProductPage
from pages.wishlist_page import WishlistPage


def pytest_addoption(parser):
    parser.addoption(
        '--browser_name',
        action='store',
        default='chrome',
        help='Choose browser: chrome, firefox or edge'
    )


@pytest.fixture(scope='class')
def driver(request):
    browser_name = request.config.getoption('--browser_name')

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--disable-notifications')
    chrome_options.add_argument('--disable-infobars')
    chrome_options.page_load_strategy = 'eager'
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    # chrome_options.add_argument('--headless=new')

    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument("--disable-notifications")
    firefox_options.add_argument('--disable-infobars')
    firefox_options.page_load_strategy = 'eager'
    firefox_options.add_argument("--disable-dev-shm-usage")
    firefox_options.add_argument('--headless')

    if browser_name == 'chrome':
        driver = webdriver.Chrome(options=chrome_options)
        print('\nStart Chrome browser')
        # driver.maximize_window()
        driver.set_window_size(1920, 1080)
    elif browser_name == 'firefox':
        driver = webdriver.Firefox(options=firefox_options)
        print('\nStart Firefox browser')
        # driver.maximize_window()
        driver.set_window_size(1920, 1080)
    elif browser_name == 'docker_chrome':
        driver = webdriver.Remote('http://localhost:4444/wd/hub', options=chrome_options)
        # driver = webdriver.Remote('http://selenium_chrome:4444/wd/hub', options=chrome_options)
        print('Start Chrome browser in Docker')
        driver.set_window_size(1920, 1080)
    elif browser_name == 'docker_firefox':
        driver = webdriver.Remote('http://localhost:4440/wd/hub', options=firefox_options)
        # driver = webdriver.Remote('http://selenium_firefox:4440/wd/hub', options=firefox_options)
        print('Start Firefox browser in Docker')
        driver.set_window_size(1920, 1080)
    else:
        raise pytest.UsageError('--browser_name should be chrome, firefox or edge')
    yield driver
    attachment = driver.get_screenshot_as_png()
    allure.attach(attachment, name=f"Screenshot {datetime.today()}", attachment_type=allure.attachment_type.PNG)
    driver.quit()
    print('\nQuit browser')


@pytest.fixture(scope="session")
def get_auth_cookies():
    driver = webdriver.Chrome()
    page = LoginPage(driver, URL.LOGIN_PAGE)
    page.open_page()

    page.enter_email(AutData.LOGIN_EMAIL)
    page.enter_password(AutData.PASSWORD)
    page.click_login_button()

    cookies = driver.get_cookies()
    return cookies


@pytest.fixture
def add_cookies(driver, get_auth_cookies):
    driver.get("https://uk.gymshark.com")
    for cookie in get_auth_cookies:
        driver.add_cookie(cookie)


@pytest.fixture(scope='class')
def add_product_to_bag(driver):
    page = ProductPage(driver, URL.PDP)
    page.open_page()

    page.select_random_size()
    page.add_to_bag()
    page.open_mini_bag()


@pytest.fixture(scope='class')
def login(driver):
    page = LoginPage(driver, URL.LOGIN_PAGE)
    page.open_page()

    page.enter_email(AutData.LOGIN_EMAIL)
    page.enter_password(AutData.PASSWORD)
    page.click_login_button()


@pytest.fixture()
def add_to_wishlist(driver):
    """Add product to Favourites from PLP"""
    plp = ProductListingPage(driver, URL.PLP)
    plp.open_page()
    plp.add_to_wishlist()


@pytest.fixture()
def clear_wishlist(driver):
    """Delete all products on the Wishlist page after the test"""
    yield
    wishlist_page = WishlistPage(driver, URL.WISHLIST)
    wishlist_page.open_page()
    if wishlist_page.is_product_present():
        wishlist_page.remove_all_products()


@pytest.fixture(scope='function')
def clear_cookies(driver):
    yield
    driver.delete_all_cookies()
