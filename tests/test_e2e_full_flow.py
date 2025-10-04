from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import sys
import os
import time

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from pages.LoginPage import LoginPage
from pages.InventoryPage import InventoryPage
from pages.CartPage import CartPage
from pages.CheckoutStepOnePage import CheckoutStepOnePage
from pages.CheckoutStepTwoPage import CheckoutStepTwoPage
from pages.CheckoutCompletePage import CheckoutCompletePage

print("Starting the End-to-End E-commerce Flow Test on Firefox...")
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

login_page = LoginPage(driver)
inventory_page = InventoryPage(driver)
cart_page = CartPage(driver)
checkout_one_page = CheckoutStepOnePage(driver)
checkout_two_page = CheckoutStepTwoPage(driver)
checkout_complete_page = CheckoutCompletePage(driver)

try:
    # Step 1
    print("Step 1: Logging in with standard_user...")
    driver.get("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")

    assert "Products" in inventory_page.get_header_title_text()
    print("SUCCESS: Logged in and on the Inventory Page.")
    time.sleep(2)  

    # Step 2
    print("Step 2: Adding Sauce Labs Backpack to cart...")
    inventory_page.add_backpack_to_cart()
    inventory_page.go_to_cart()
    print("SUCCESS: Navigated to the cart.")
    time.sleep(2)  

    # Step 3
    print("Step 3: Clicking checkout...")
    cart_page.click_checkout()
    print("SUCCESS: On the checkout information page.")
    time.sleep(2)  

    # Step 4
    print("Step 4: Filling out user information...")
    checkout_one_page.fill_out_form("Test", "User", "12345")
    print("SUCCESS: Information filled and continued to overview.")
    time.sleep(2)  

    # Step 5
    print("Step 5: Clicking the finish button...")
    checkout_two_page.click_finish()
    print("SUCCESS: Order finished.")
    time.sleep(2)  

    # Step 6
    print("Step 6: Verifying the order completion message...")
    confirmation_text = checkout_complete_page.get_complete_header_text()
    assert "Thank you for your order!" in confirmation_text
    print("SUCCESS: Order confirmation message is correct.")
    time.sleep(2)  

    print("\n--- TEST PASSED: E2E flow completed successfully! ---")

except AssertionError as e:
    print(f"\n--- TEST FAILED: Assertion failed at step verification. {e} ---")
except Exception as e:
    print(f"\n--- TEST FAILED: An unexpected error occurred. {e} ---")
finally:
    # Clean
    print("Closing the browser.")
    driver.quit()
