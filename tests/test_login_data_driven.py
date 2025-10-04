import pytest
import pandas as pd
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from pages.LoginPage import LoginPage
from pages.InventoryPage import InventoryPage

test_data_df = pd.read_csv("test_data/login_credentials.csv", index_col=False)
test_data = [tuple(x) for x in test_data_df.to_numpy()]

@pytest.mark.parametrize("username, password, expected_outcome, description", test_data)
def test_login(driver, username, password, expected_outcome, description):
    """
    This single function will be run multiple times by pytest,
    once for each row in our test_data.
    """
    print(f"Testing login for: {description}")
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    driver.get("https://www.saucedemo.com/")
    login_page.login(username, password)

    if expected_outcome == 'success':
        expected_url = "https://www.saucedemo.com/inventory.html"
        actual_url = inventory_page._get_current_url()
        assert actual_url == expected_url, f"Expected URL {expected_url} but got {actual_url}"
    else:
        error_text = login_page.get_error_message_text()
        assert error_text is not None, "Expected an error message but none was found."
