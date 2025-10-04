from selenium.webdriver.common.by import By
from .BasePage import BasePage

class CheckoutCompletePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.complete_header = (By.CLASS_NAME, "complete-header")

    def get_complete_header_text(self):
        return self._get_text(self.complete_header)
