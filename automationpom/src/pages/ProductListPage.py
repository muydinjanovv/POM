class ProductListPage:

    def __init__(self, page):
        self.page = page
        self._products_header = page.locator("span.title")
        self._burger_menu = page.locator("button#react-burger-menu-btn")
        self._logout_btn = page.locator("#logout_sidebar_link")

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