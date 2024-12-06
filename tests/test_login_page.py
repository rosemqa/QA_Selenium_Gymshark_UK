import time
import allure
import pytest
from data.constants import Login
from data.data import AutData
from data.links import LOGIN_PAGE, ACCOUNT_PAGE
from pages.login_page import LoginPage


@allure.epic('Login Page')
class TestLoginPage:
    @allure.feature('Login to account')
    class TestLoginToAccount:
        @allure.description('Can login with valid credentials')
        def test_happy_path_login(self, driver):
            page = LoginPage(driver, LOGIN_PAGE)
            page.open_page()

            page.enter_email(AutData.LOGIN_EMAIL)
            page.enter_password(AutData.PASSWORD)
            page.click_login_button()
            assert ACCOUNT_PAGE in page.get_current_url()

    @allure.feature('Login page cases')
    class TestLoginPageCases:
        @allure.description('Can not login with empty email field')
        @allure.tag('negative')
        def test_login_with_empty_email(self, driver):
            page = LoginPage(driver, LOGIN_PAGE)
            page.open_page()

            page.enter_password(AutData.PASSWORD)
            page.click_login_button()
            error_is_present, error_text = page.is_email_required_error_present()
            assert error_is_present, 'Email required error is missing'
            assert error_text == Login.EMAIL_REQUIRED_ERROR_TEXT, 'Email required error text is incorrect'

        @allure.description('Can not login with empty password field')
        @allure.tag('negative')
        def test_login_with_empty_password(self, driver):
            page = LoginPage(driver, LOGIN_PAGE)
            page.open_page()

            page.enter_email(AutData.LOGIN_EMAIL)
            page.click_login_button()
            error_is_present, error_text = page.is_password_required_error_present()
            assert error_is_present, 'Password required error is missing'
            assert error_text == Login.PASSWORD_REQUIRED_ERROR_TEXT, 'Password required error text is incorrect'

        @allure.description('Can not login with with incorrect email format')
        @pytest.mark.parametrize('email', ['test mail.com', 'test@mailcom'])
        @allure.tag('negative')
        def test_login_with_incorrect_email_format(self, driver, email):
            page = LoginPage(driver, LOGIN_PAGE)
            page.open_page()

            page.enter_email(email)
            page.enter_password(AutData.PASSWORD)
            page.click_login_button()
            error_is_present, error_text = page.is_email_invalid_error_present()
            assert error_is_present, 'Email invalid error is missing'
            assert error_text == Login.EMAIL_INVALID_ERROR_TEXT, 'Email invalid error text is incorrect'
            time.sleep(3)

        @allure.description('Cannot login with wrong email/password')
        @pytest.mark.parametrize('email, password', [
            ('unregistered_email@mail.com', AutData.PASSWORD),
            (AutData.LOGIN_EMAIL, 'wrong_password')])
        @allure.tag('negative')
        def test_login_with_wrong_credentials(self, driver, email, password):
            page = LoginPage(driver, LOGIN_PAGE)
            page.open_page()

            page.enter_email(email)
            page.enter_password(password)
            page.click_login_button()
            error_is_present, error_text = page.is_wrong_credentials_error_present()
            assert error_is_present, 'Wrong credentials error is missing'
            assert error_text == Login.WRONG_CREDENTIALS_ERROR_TEXT, 'Wrong credentials error text is incorrect'

        @allure.description('Can show/hide password')
        def test_show_password(self, driver):
            page = LoginPage(driver, LOGIN_PAGE)
            page.open_page()

            password = AutData.PASSWORD
            page.enter_password(password)
            page.click_show_password_button()
            assert page.is_password_masked() is False, 'Password was not shown'
            assert page.is_hide_password_tooltip_present(), 'Hide password tooltip is missing'

            page.click_show_password_button()
            assert page.is_password_masked(), 'Password was not hidden'
            assert page.is_show_password_tooltip_present(), 'Show password tooltip is missing'
