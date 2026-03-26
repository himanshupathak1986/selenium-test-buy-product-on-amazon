import re
from selenium.webdriver.common.by import By
from pages.base_page import base_page


class cart_page(base_page):
    CART_ICON_ID = "nav-cart"
    CART_ICON = (By.ID, CART_ICON_ID)
    CART_PRICE = (By.CSS_SELECTOR, ".a-price .a-offscreen")
    CART_PRICE_ID = (By.ID, "sc-subtotal-amount-buybox")
    CART_PRICE_CLASS = (By.CLASS_NAME, "a-price sw-subtotal-amount")

    def no_thanks_to_offers_by_clicking_x(self):
        try:
            no_thanks_buttons = self.driver.find_elements(By.ID, "attach-warranty-close-icon")
            if len(no_thanks_buttons) > 0:
                self.driver.execute_script("arguments[0].click();", no_thanks_buttons[0])  # Use JavaScript to click the button
                
                #no_thanks_buttons[0].click()
        except Exception as e:
            print(f"No 'No Thanks' button found or could not click: {e}")

    def go_to_cart(self):
        #breakpoint()
        self.wait_for_element_clickable(self.CART_ICON)
        cart_button = self.driver.find_element(By.ID, self.CART_ICON_ID)
        self.driver.execute_script("arguments[0].click();", cart_button)  
        #breakpoint()
        #self.click(self.CART_ICON)

    def get_cart_price(self):
        cart_price_elements = self.driver.find_elements(*self.CART_PRICE)
        cart_price = cart_price_elements[0].get_attribute("innerHTML") or cart_price_elements[0].text
        cleaned_price = re.sub(r'[^\d.]', '', cart_price) # remove everything except numbers and the decimal point.
        return float(cleaned_price)  
