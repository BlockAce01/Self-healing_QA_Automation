from selenium.webdriver.common.by import By
from .BasePage import BasePage

class CheckoutStepTwoPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.finish_button = (By.ID, "finish")

    def click_finish(self):
        self._click(self.finish_button)
