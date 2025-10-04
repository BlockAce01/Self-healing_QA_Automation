from selenium.webdriver.common.by import By
from .BasePage import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_message = (By.CSS_SELECTOR, "h3[data-test='error']")

    def enter_username(self, username):
        self._send_keys(self.username_input, username)

    def enter_password(self, password):
        self._send_keys(self.password_input, password)

    def click_login(self):
        self._click(self.login_button)

    def get_error_message_text(self):
        return self._get_text(self.error_message)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
