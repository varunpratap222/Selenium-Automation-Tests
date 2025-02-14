import pytest
from selenium import webdriver
from pages.checkout_page import CheckoutPage
from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from utils.config import BASE_URL, VALID_USERNAME, VALID_PASSWORD

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(BASE_URL)
    yield driver
    driver.quit()

@pytest.fixture
def logged_in_driver(driver):
    from pages.login_page import LoginPage
    login_page = LoginPage(driver)
    login_page.login(VALID_USERNAME, VALID_PASSWORD)
    return driver

def test_checkout_process(logged_in_driver):
    driver = logged_in_driver
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)
    
    # Add an item to the cart
    inventory_page.add_item_to_cart("Sauce Labs Backpack")
    inventory_page.go_to_cart()
    
    # Initiate checkout
    cart_page.proceed_to_checkout()
    
    # Fill out checkout information (assuming these methods exist)
    checkout_page.enter_first_name("John")
    checkout_page.enter_last_name("Doe")
    checkout_page.enter_postal_code("12345")
    checkout_page.continue_checkout()
    
    # Finalize the order
    checkout_page.finish_checkout()
    
    # Verify that we see an order confirmation message or page
    assert "Thank you for your order" in checkout_page.get_confirmation_message()
