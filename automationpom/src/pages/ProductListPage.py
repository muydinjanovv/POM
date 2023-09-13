class ProductListPage:

    def __init__(self, page):
        self.page = page
        self._products_header = page.locator("span.title")
        self._burger_menu = page.locator("button#react-burger-menu-btn")
        self._logout_btn = page.locator("#logout_sidebar_link")
        self._addOto_cart = page.locator(
            "//div[text()='Sauce Labs Bike Light']/ancestor::div[@class='inventory_item']//button[text()='Add to cart']")

    @property
    def product_header(self):
        """Returns the product header locator"""
        return self._products_header\


    def click_burger_menu(self):
        """Clicks the burger menu"""
        self._burger_menu.click()

    def click_logout(self):
        """Clicks the logout button"""
        self._logout_btn.click()

    def do_logout(self):
        self.click_burger_menu()
        self.click_logout()


    def get_add_remove_cart_locator(self, product):
        """Returns the locator for the add/remove cart button for a given product"""
        return self.page.locator(f"//div[text()='{product}']/ancestor::div[@class='inventory_item_label']/following-sibling::div//button")
    
    def click_add_to_cart_or_remove(self, product):
        """Clicks the add to cart button for a given product"""
        self.get_add_remove_cart_locator(product).click()
