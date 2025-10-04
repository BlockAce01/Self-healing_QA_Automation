from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    
    def __init__(self, driver):
        self.driver = driver

    def _find_element(self, locator, timeout=10):
        
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            raise TimeoutException(f"Element with locator {locator} not found within {timeout} seconds.")

    def _click(self, locator):
        
        element = self._find_element(locator)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)).click()

    def _send_keys(self, locator, text):
        
        self._find_element(locator).send_keys(text)

    def _get_text(self, locator):
        
        return self._find_element(locator).text

    def _get_current_url(self):
        
        return self.driver.current_url