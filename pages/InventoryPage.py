from selenium.webdriver.common.by import By

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.header_title = (By.CLASS_NAME, "title")
        self.backpack_add_to_cart_button = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.cart_link = (By.CLASS_NAME, "shopping_cart_link")

    def get_header_title_text(self):
        return self.driver.find_element(*self.header_title).text

    def add_backpack_to_cart(self):
        self.driver.find_element(*self.backpack_add_to_cart_button).click()

    def go_to_cart(self):
        self.driver.find_element(*self.cart_link).click()
