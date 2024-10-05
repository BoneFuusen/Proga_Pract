from playwright.sync_api import expect, Page

from pages.LoginPage import LoginPage
from pages.ProductsPage import ProductsPage


def test_login(page: Page) -> None:
    login_page = LoginPage(page)
    products_page = ProductsPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    expect(products_page.title_exists()).to_be_visible()
