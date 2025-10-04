from selenium.webdriver.common.by import By

class CheckoutStepTwoPage:
    def __init__(self, driver):
        self.driver = driver
        self.finish_button = (By.ID, "finish")

    def click_finish(self):
        self.driver.find_element(*self.finish_button).click()
