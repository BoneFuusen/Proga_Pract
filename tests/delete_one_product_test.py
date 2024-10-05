from playwright.sync_api import expect, Page

from pages.LoginPage import LoginPage
from pages.ProductsPage import ProductsPage
from pages.CartPage import CartPage


def test_delete_one_prod(page: Page) -> None:
    login_page = LoginPage(page)
    products_page = ProductsPage(page)
    cart_page = CartPage(page)

    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    products_page.add_backpack_to_cart()
    products_page.go_to_cart()

    expect(cart_page.backpack_remove_button).to_be_visible()
    cart_page.remove_backpack_from_cart()
    expect(cart_page.backpack_remove_button).to_be_hidden()
