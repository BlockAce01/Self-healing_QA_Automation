from selenium.webdriver.common.by import By
from .BasePage import BasePage

class InventoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.header_title = (By.CLASS_NAME, "title")
        self.backpack_add_to_cart_button = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.cart_link = (By.CLASS_NAME, "shopping_cart_link")

    def get_header_title_text(self):
        return self._get_text(self.header_title)

    def add_backpack_to_cart(self):
        self._click(self.backpack_add_to_cart_button)

    def go_to_cart(self):
        self._click(self.cart_link)
