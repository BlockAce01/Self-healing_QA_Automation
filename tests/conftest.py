import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager

def get_driver(browser_name):
    if browser_name == "firefox":
        return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser_name == "chrome":
        return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    else:
        raise ValueError(f"Browser '{browser_name}' is not supported. Use 'firefox' or 'chrome'.")

@pytest.fixture(params=["firefox", "chrome"])
def driver(request):
    browser_name = request.param
    driver_instance = get_driver(browser_name)
    driver_instance.maximize_window()

    yield driver_instance

    driver_instance.quit()
