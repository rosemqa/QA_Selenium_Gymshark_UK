from data.data import AutData


class Login:
    EMAIL_REQUIRED_ERROR_TEXT = 'Username is required'
    PASSWORD_REQUIRED_ERROR_TEXT = 'Password is required'
    EMAIL_INVALID_ERROR_TEXT = 'Email is not valid.'
    WRONG_CREDENTIALS_ERROR_TEXT = 'Wrong email or password'


class Bag:
    DISCOUNT_CODE_ERROR = '*The discount code is invalid.'
    EMPTY_BAG_TEXT = 'YOUR BAG IS EMPTY'
    REMOVED_PRODUCT_TOAST_TEXT = 'You removed an item from your bag.'


class Wishlist:
    EMPTY_WISHLIST_TITLE = 'YOUR WISHLIST IS EMPTY'
    ITEM_REMOVED_TOAST_TEXT = 'Item removed from your wishlist'
    ITEM_ADDED_TOAST_TEXT = 'Item added to your wishlist'


class Base:
    SIGN_IN_TOOLTIP_TEXT = 'Sign in to get exclusive rewards & benefits\nNew Customer? Create account'
    ACCOUNT_ICON_DEFAULT_TEXT = 'Account'
    ACCOUNT_ICON_LOGGED_IN_USER_TEXT = f'Hi, {AutData.USER_FIRST_NAME}'


class Account:
    EMPTY_ADDRESS_BOOK_TITLE_TEXT = 'ADDRESS BOOK IS EMPTY'
    REQUIRED_FIELD_ERROR_TEXT = '*This field is required'
    PHONE_ERROR_TEXT = '*Minimum 10 digits and maximum 22 digits, numbers only'


class Search:
    SEARCH_FIELD_PLACEHOLDER = 'What are you looking for today?'
    NO_RESULTS_ERROR = lambda search_query: \
        f'NO RESULTS FOUND\nWe are sorry but we can’t find any results for “{search_query}”'
