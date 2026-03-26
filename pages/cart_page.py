import re
from selenium.webdriver.common.by import By
from pages.base_page import base_page


class cart_page(base_page):
    CART_ICON = (By.ID, "nav-cart")
    CART_PRICE = (By.CSS_SELECTOR, ".sc-product-price, .a-price .a-offscreen")

    def no_thanks_to_offers(self):
        try:
            no_thanks_buttons = self.driver.find_elements(By.ID, "attach-warranty-close-icon")
            if len(no_thanks_buttons) > 0:
                self.driver.execute_script("arguments[0].click();", no_thanks_buttons[0])  # Use JavaScript to click the button
                
                #no_thanks_buttons[0].click()
        except Exception as e:
            print(f"No 'No Thanks' button found or could not click: {e}")

    def go_to_cart(self):
        self.click(self.CART_ICON)

    def get_cart_price(self):
        price_elements = self.driver.find_elements(*self.CART_PRICE)
        price_text = price_elements[0].get_attribute("innerHTML") or price_elements[0].text
        return float(price_text.replace('$', ''))  
