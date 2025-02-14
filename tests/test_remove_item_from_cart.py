import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.config import BASE_URL, VALID_USERNAME, VALID_PASSWORD

# Fixture to initialize the WebDriver and open the base URL.
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(BASE_URL)
    yield driver
    driver.quit()

# Fixture to perform login.
@pytest.fixture
def logged_in_driver(driver):
    login_page = LoginPage(driver)
    login_page.login(VALID_USERNAME, VALID_PASSWORD)
    return driver

def test_remove_item_from_cart(logged_in_driver):
    driver = logged_in_driver
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    
    # For this test, add three items to the cart:
    # Two items are added via inventory page.
    inventory_page.add_item_to_cart("Sauce Labs Backpack")
    inventory_page.add_item_to_cart("Sauce Labs Bike Light")
    # Add one item from the item details page (Task 3 scenario).
    inventory_page.click_product("Sauce Labs Onesie")
    from pages.inventory_item_page import InventoryItemPage
    item_page = InventoryItemPage(driver)
    item_page.add_to_cart()
    
    # Verify the cart count is 3.
    assert inventory_page.get_cart_item_count() == 3
    
    # Navigate to the cart page.
    inventory_page.go_to_cart()
    
    # Remove an item that costs between $8 and $10.
    # (Assuming your CartPage.remove_item_by_price_range() is implemented accordingly.)
    cart_page.remove_item_by_price_range(8, 10)
    
    # Verify that the cart count is updated to 2.
    assert cart_page.get_cart_item_count() == 2
