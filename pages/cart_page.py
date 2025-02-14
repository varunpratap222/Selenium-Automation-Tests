from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    REMOVE_BUTTON = (By.CLASS_NAME, "cart_button")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def get_cart_items(self):
        items = self.driver.find_elements(*self.CART_ITEMS)
        return [item.find_element(By.CLASS_NAME, "inventory_item_name").text for item in items]

    def remove_item_by_price_range(self, min_price, max_price):
        items = self.driver.find_elements(*self.CART_ITEMS)
        for item in items:
            price_element = item.find_element(By.CLASS_NAME, "inventory_item_price")
            price = float(price_element.text.replace("$", ""))
            if min_price <= price <= max_price:
                remove_button = item.find_element(By.CLASS_NAME, "cart_button")
                remove_button.click()
                break

    def get_cart_item_count(self):
        try:
            badge = self.find_element((By.CLASS_NAME, "shopping_cart_badge"), timeout=3)
            return int(badge.text)
        except Exception:
            return 0

    def proceed_to_checkout(self):
        self.click_element(self.CHECKOUT_BUTTON)
