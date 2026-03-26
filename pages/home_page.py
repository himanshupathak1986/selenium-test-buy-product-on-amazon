from selenium.webdriver.common.by import By
from pages.base_page import base_page


class homepage(base_page):
    SEARCH_BOX = (By.ID, "twotabsearchtextbox")
    SEARCH_BUTTON = (By.ID, "nav-search-submit-button")

    def load(self):
        self.open("https://www.amazon.com")

    def search_product(self, product_name):
        self.type(self.SEARCH_BOX, product_name)
        self.click(self.SEARCH_BUTTON)