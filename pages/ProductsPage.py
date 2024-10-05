from playwright.sync_api import Page


class ProductsPage:
    def __init__(self, page: Page):
        self.title = page.locator("[data-test=\"title\"]")
        self.backpack_add_button = page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]")
        self.cart_go_button = page.locator("[data-test=\"shopping-cart-link\"]")

    def title_exists(self):
        return self.title

    def add_backpack_to_cart(self):
        self.backpack_add_button.click()

    def go_to_cart(self):
        self.cart_go_button.click()
