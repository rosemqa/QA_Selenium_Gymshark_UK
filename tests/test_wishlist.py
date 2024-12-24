import allure
from data.constants import Wishlist
from data.links import URL
from pages.wishlist_page import WishlistPage


@allure.epic('Wishlist')
class TestWishlist:
    @allure.description('Can delete product using the wishlist icon in the product card')
    def test_remove_product_via_wishlist_icon(self, driver, login, add_to_wishlist, clear_wishlist):
        page = WishlistPage(driver, URL.WISHLIST)
        page.open_page()

        is_wishlist_empty, empty_wishlist_title = page.click_wishlist_icon_in_product_card()
        assert is_wishlist_empty, 'Wishlist is not empty'
        assert empty_wishlist_title == Wishlist.EMPTY_WISHLIST_TITLE, 'Empty wishlist title text is incorrect'

    @allure.description('Can delete product using the More menu')
    def test_remove_product_via_menu(self, driver, add_to_wishlist, clear_wishlist):
        page = WishlistPage(driver, URL.WISHLIST)
        page.open_page()

        is_wishlist_empty, empty_wishlist_title = page.remove_product_in_more_menu()
        assert is_wishlist_empty, 'Wishlist is not empty'
        assert empty_wishlist_title == Wishlist.EMPTY_WISHLIST_TITLE, 'Empty wishlist title text is incorrect'

    @allure.description('Can clear the wishlist using the Remove All button')
    def test_remove_all_products(self, driver, login, add_to_wishlist, clear_wishlist):
        page = WishlistPage(driver, URL.WISHLIST)
        page.open_page()

        is_wishlist_empty, empty_wishlist_title = page.remove_all_products()
        assert is_wishlist_empty, 'Wishlist is not empty'
        assert empty_wishlist_title == Wishlist.EMPTY_WISHLIST_TITLE, 'Empty wishlist title text is incorrect'

    @allure.description('Can select size in the size dropdown')
    def test_select_size(self, driver, login, add_to_wishlist, clear_wishlist):
        page = WishlistPage(driver, URL.WISHLIST)
        page.open_page()

        random_size, selected_size = page.select_random_size()
        assert random_size == selected_size, 'The random size in the drop down list does not match the selected one'

    @allure.description('Can add a product from wishlist to the bag using the Bag button')
    def test_add_to_bag_via_bag_button(self, driver, login, add_to_wishlist, clear_wishlist):
        page = WishlistPage(driver, URL.WISHLIST)
        page.open_page()

        page.select_random_size()
        page.click_add_to_bag_button()
        is_count_icon_present, count_value = page.is_bag_count_icon_present()
        assert is_count_icon_present, 'Bag count icon is missing, the product was probably not added to the bag'

    @allure.description('Can add a product from wishlist to the bag using the More menu')
    def test_add_to_bag_via_menu(self, driver, login, add_to_wishlist, clear_wishlist):
        page = WishlistPage(driver, URL.WISHLIST)
        page.open_page()

        page.select_random_size()
        is_count_icon_present, count_value = page.add_to_bag_from_more_menu()
        assert is_count_icon_present, 'Bag count icon is missing, the product was probably not added to the bag'

    @allure.description('Can restore product after deletion')
    def test_undo_deletion(self, driver, login, check):
        page = WishlistPage(driver, URL.WISHLIST)
        page.open_page()

        page.click_wishlist_icon_in_product_card()
        is_toast_present, toast_text = page.undo_deletion()
        is_product_present = page.is_product_present()
        toast_text_after = page.get_toast_text()
        is_toast_disappeared = page.is_wishlist_toast_disappeared()
        with check:
            assert is_product_present, 'Product was not restored to the wishlist'
        with check:
            assert is_toast_present, 'Wishlist toast is missing'
        with check:
            assert toast_text == Wishlist.ITEM_REMOVED_TOAST_TEXT, 'Check the toast text when deleting a product'
        with check:
            assert toast_text_after == Wishlist.ITEM_ADDED_TOAST_TEXT, 'Check the toast text after restoring a product'
        assert is_toast_disappeared, 'The toast was not disappeared after 5 seconds'
