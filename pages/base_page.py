from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class base_page:
    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url):
        self.driver.get(url)

    def wait_for_element_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_element_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def click(self, locator):
        element = self.wait_for_element_clickable(locator)
        element.click()

    def type(self, locator, value):
        element = self.wait_for_element_visible(locator)
        element.clear()
        element.send_keys(value)

    def get_text(self, locator):
        element = self.wait_for_element_visible(locator)
        return element.text.strip()