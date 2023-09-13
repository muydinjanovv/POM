

class CheckoutPage:
    def __init__(self, page):
        self.page = page
        self._first_name = page.locator("[data-test='firstName']")
        self._last_name = page.locator("[data-test='lastName']")
        self._postal_code = page.locator("[data-test='postalCode']")
        self._continue_btn = page.locator("#continue")
        self._finish_btn = page.locator("#finish")
        self._confirmation_message = page.locator("h2.complete-header")

    def enter_first_name(self, first_name):
        """Enters the first name"""
        self._first_name.fill(first_name)
        return self

    def enter_last_name(self, last_name):
        """Enters the last name"""
        self._last_name.fill(last_name)
        return self

    def enter_postal_code(self, postal_code):
        """Enters the postal code"""
        self._postal_code.fill(postal_code)   
        return self        

    def enter_checkout_info(self, first_name, last_name, postal_code):
        """Enters the checkout info"""
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_postal_code(postal_code)
        return self

    def click_continue(self):
        """Clicks the continue button"""
        self._continue_btn.click()
        return self

    def click_finish(self):
        """Clicks the finish button"""
        self._finish_btn.click()  
        return self 

    def get_confirm_message(self):
        """Returns the confirmation message"""
        return self._confirmation_message