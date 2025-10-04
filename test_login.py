import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# --- Step 1: Initialize the WebDriver ---
print("Initializing the Chrome browser...")
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
print("Browser initialized.")

# --- Step 2: Navigate to the Webpage ---
print("Navigating to the login page...")
driver.get("http://the-internet.herokuapp.com/login")
print("Successfully navigated to the page.")

# --- Step 3: Wait and Then Clean Up ---
print("Waiting for 5 seconds before closing...")
time.sleep(5)

driver.quit()
print("Browser closed. Test finished.")