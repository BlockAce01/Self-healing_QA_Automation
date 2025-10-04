import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture
def driver():
    driver_instance = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver_instance.maximize_window()

    yield driver_instance

    driver_instance.quit()
