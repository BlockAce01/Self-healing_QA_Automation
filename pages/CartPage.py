from selenium.webdriver.common.by import By
from .BasePage import BasePage

class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.checkout_button = (By.ID, "checkout")

    def click_checkout(self):
        self._click(self.checkout_button)
