from automationpom.src.pages.ProductListPage import ProductListPage


class LoginPage:

    def __init__(self, page):
        self.page = page
        self._username = page.get_by_placeholder("Username")
        self._password = page.get_by_placeholder("Password")
        self._login_btn = page.get_by_text("Login")
        self._error_msg = page.locator("h3[data-test='error']")

    def enter_username(self, username):
        self._username.clear()
        self._username.fill(username)    

    def enter_password(self, password):
        self._password.clear()
        self._password.fill(password)     

    def click_login(self):
        self._login_btn.click()    

    def do_login(self, credentials):
        self.enter_username(credentials["username"])
        self.enter_password(credentials["password"])
        self.click_login()
        return ProductListPage(self.page)
    
    @property
    def err_msg_loc(self):
        return self._error_msg
    
    @property
    def login_button(self):
        return self._login_btn