import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# --- Step 1: Initialize the WebDriver ---
print("Setting up Chrome options for incognito mode...")
chrome_options = Options()
chrome_options.add_argument("--incognito")
print("Initializing the Chrome browser...")
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
print("Browser initialized.")

# --- Step 2: Navigate to the Webpage ---
print("Navigating to the login page...")
driver.get("https://the-internet.herokuapp.com/login")
print("Successfully navigated to the page.")


# --- Step 3: Find Elements and Interact ---
print("Finding the username field...")
username_field = driver.find_element(By.ID, "username")
print("Typing in the username...")
username_field.send_keys("tomsmith")

print("Finding the password field...")
password_field = driver.find_element(By.ID, "password")
print("Typing in the password...")
password_field.send_keys("SuperSecretPassword!")

print("Finding the login button...")
login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
print("Clicking the login button...")
login_button.click()


# --- Step 4: Assertion ---
print("Verifying the login was successful...")
time.sleep(2) 

success_banner = driver.find_element(By.ID, "flash")
banner_text = success_banner.text

print(f"Found banner text: '{banner_text}'")
assert "You logged into a secure area!" in banner_text
print("Assertion successful! The correct text was found.")

# --- Clean Up ---
print("Waiting for 3 seconds before closing...")
time.sleep(3)

driver.quit()
print("Browser closed. Test finished successfully.")