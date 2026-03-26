from time import time
import pages.search_results_page
import pages.cart_page
from pages.home_page import homepage


def test_select_third_tv_and_verify_cart_price(driver):
    home_page_instance = homepage(driver)
    search_results_page_instance = pages.search_results_page.search_results_page(driver)
    cart_page_instance = pages.cart_page.cart_page(driver)

    home_page_instance.load()
    home_page_instance.search_product("TV")

    stored_price = search_results_page_instance.select_third_result_and_get_price()
    print(f"TEST STEP:: Stored product price: {stored_price}")
    #breakpoint()
    
    print(f"TEST STEP:: Add the item to cart")
    search_results_page_instance.add_to_cart()

    breakpoint()
    print(f"TEST STEP:: Click on X to not add any offers if they appear after adding to cart")
    cart_page_instance.no_thanks_to_offers_by_clicking_x()  # Handle any offers that may appear after adding to cart
    
    print(f"TEST STEP:: Go to Cart")
    cart_page_instance.go_to_cart()

    breakpoint()
    driver.refresh()  # Refresh the cart page to ensure the latest price is displayed
    print(f"TEST STEP:: Get the price of cart items")
    cart_price = cart_page_instance.get_cart_price()
    print(f"TEST STEP:: Cart price: {cart_price}")

    
    #breakpoint()
    print(f"TEST STEP:: verify that cart price::{cart_price} equals to product price::{stored_price}")
    assert stored_price == cart_price, (
        f"Price mismatch. Product price: {stored_price}, Cart price: {cart_price}"
    )