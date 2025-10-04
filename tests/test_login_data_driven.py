import pandas as pd
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import sys
import os
import time

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from pages.LoginPage import LoginPage

test_data = pd.read_csv("test_data/login_credentials.csv", index_col=False)
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
login_page = LoginPage(driver)

for index, row in test_data.iterrows():
    username = row['username']
    password = row['password']
    expected_outcome = row['expected_outcome']

    print(f"--- Testing with user: {username} ---")
    driver.get("https://www.saucedemo.com/")
    login_page.login(username, password)

    # If the user is the glitch user, the page takes ~5 seconds to load
    if username == 'performance_glitch_user':
        print("Performance glitch user detected. Waiting for 6 seconds...")
        time.sleep(6)
    # Assertion
    if expected_outcome == 'success':
        expected_url = "https://www.saucedemo.com/inventory.html"
        actual_url = driver.current_url
        try:
            assert actual_url == expected_url
            print("Status: PASSED - Login successful and on inventory page.")
        except AssertionError:
            print(f"Status: FAILED - Expected '{expected_url}' vs. Got '{actual_url}'.")
    else:
        try:
            error_text = login_page.get_error_message_text()
            print(f"Found error message: '{error_text}'")
            print("Status: PASSED - Error message was displayed as expected.")
        except Exception as e:
            print(f"Status: FAILED - Expected an error message but none was found. {e}")
    print("-" * 40)

# Clean
driver.quit()
print("All login tests finished.")
