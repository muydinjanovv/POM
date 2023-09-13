from playwright.sync_api import expect
from automationpom.src.pages.LoginPage import LoginPage


def test_place_order(set_up_tear_down) -> None:
    """
    Verify that a user can place an order successfully
    """
    page = set_up_tear_down
    credentials = {'username':'standard_user', 'password':'secret_sauce'}
    login_p = LoginPage(page)
    products_p = login_p.do_login(credentials)
    product_name = "Sauce Labs Fleece Jacket"
    checkout_p = products_p.click_add_to_cart_or_remove(product_name)\
        .click_cart_icon()\
        .click_checkout_button()\
        .enter_checkout_info("John", "Doe", "12345")\
        .click_continue()\
        .click_finish()
    
    expect(checkout_p.get_confirm_message()).to_have_text("Thank you for your order!")
    page.screenshot(path="order_confirmation.png")