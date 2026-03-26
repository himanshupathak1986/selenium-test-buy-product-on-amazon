import re
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from pages.base_page import base_page


class search_results_page(base_page):
    SEARCH_RESULTS = (By.CSS_SELECTOR, 'div[data-component-type="s-search-result"]')
    PRODUCT_TITLE_LINK = (By.CSS_SELECTOR, "h2 a")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".a-price .a-offscreen")
    # .a-box-group .a-price-whole
    ADD_TO_CART_BUTTON_ID = "add-to-cart-button"
    ADD_TO_CART_BUTTON = (By.ID, ADD_TO_CART_BUTTON_ID)

    def get_search_results(self):
        self.wait_for_element_visible(self.SEARCH_RESULTS)
        return self.driver.find_elements(*self.SEARCH_RESULTS)

    def select_third_result_and_get_price(self):
        results = self.get_search_results()

        if len(results) < 3:
            raise AssertionError(f"Expected at least 3 search results, but found {len(results)}")

        print(f"Total search results found: {len(results)}")    
        if len(results) >= 3:
            print("printing third item details for debugging:")
            # print(f"Third item is {results[2].text}")  # Debugging line to check the third item
        else:
            raise AssertionError("Less than 3 search results found, cannot select the third item.")
        third_result = results[2] # Select the third result (index 2)
        title_link = third_result.find_element(By.CSS_SELECTOR,"h2")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", title_link)
        self.driver.execute_script("arguments[0].click();", title_link)  # Adjust scroll position to account for sticky headers
        return self.get_product_price()

    def get_product_price(self):
        price_elements = self.driver.find_elements(*self.PRODUCT_PRICE)
        price_text = price_elements[0].get_attribute("innerHTML") or price_elements[0].text
        return float(price_text.replace('$', ''))  

    def add_to_cart(self):
        add_cart_button = self.driver.find_element(*self.ADD_TO_CART_BUTTON)
        print("Clicking 'Add to Cart' button...")  # Debugging line to confirm button is found
        add_cart_button.click()
        time.sleep(4) 
        #breakpoint()# Wait for potential offers to appear after adding to cart
