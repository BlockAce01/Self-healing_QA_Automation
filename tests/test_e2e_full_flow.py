import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from pages.LoginPage import LoginPage
from pages.InventoryPage import InventoryPage
from pages.CartPage import CartPage
from pages.CheckoutStepOnePage import CheckoutStepOnePage
from pages.CheckoutStepTwoPage import CheckoutStepTwoPage
from pages.CheckoutCompletePage import CheckoutCompletePage

def test_full_e2e_flow(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_one_page = CheckoutStepOnePage(driver)
    checkout_two_page = CheckoutStepTwoPage(driver)
    checkout_complete_page = CheckoutCompletePage(driver)

    #Step 1
    driver.get("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")
    assert "products" in inventory_page.get_header_title_text().lower()

    #Step 2
    inventory_page.add_backpack_to_cart()
    inventory_page.go_to_cart()

    #Step 3
    cart_page.click_checkout()

    #Step 4
    checkout_one_page.fill_out_form("Test", "User", "12345")

    #Step 5
    checkout_two_page.click_finish()

    #Step 6
    confirmation_text = checkout_complete_page.get_complete_header_text()
    assert "thank you for your order" in confirmation_text.lower()
