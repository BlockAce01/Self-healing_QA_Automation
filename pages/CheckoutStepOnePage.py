from selenium.webdriver.common.by import By
from .BasePage import BasePage

class CheckoutStepOnePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.zip_code_input = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")

    def fill_out_form(self, first_name, last_name, zip_code):
        self._send_keys(self.first_name_input, first_name)
        self._send_keys(self.last_name_input, last_name)
        self._send_keys(self.zip_code_input, zip_code)
        self._click(self.continue_button)
