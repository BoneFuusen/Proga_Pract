from playwright.sync_api import expect, Page

from pages.LoginPage import LoginPage


def test_login_empty(page: Page) -> None:
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("", "")
    expect(login_page.error).to_have_text("Epic sadface: Username is required")
