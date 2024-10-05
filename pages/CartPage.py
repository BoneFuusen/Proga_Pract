from playwright.sync_api import Page


class CartPage:
    def __init__(self, page: Page):
        self.backpack_remove_button = page.locator("[data-test=\"remove-sauce-labs-backpack\"]")

    def remove_backpack_from_cart(self):
        self.backpack_remove_button.click()
