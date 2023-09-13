from automationpom.src.pages.CheckoutPage import CheckoutPage


class CartPage:
    def __init__(self, page):
        self.page = page
        self._checkout_btn = page.locator("#checkout")

    def click_checkout_button(self):
        """Clicks the checkout button"""
        self._checkout_btn.click()
        return CheckoutPage(self.page)