from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class LogoutPage(BasePage):
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")

    def open_menu(self):
        # Wait for the menu button to be clickable and click it.
        menu_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.MENU_BUTTON)
        )
        try:
            menu_button.click()
        except Exception:
            self.driver.execute_script("arguments[0].scrollIntoView();", menu_button)
            self.driver.execute_script("arguments[0].click();", menu_button)

    def logout(self):
        # Wait until the logout link is clickable
        logout_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.LOGOUT_LINK)
        )
        try:
            logout_link.click()
        except Exception:
            self.driver.execute_script("arguments[0].scrollIntoView();", logout_link)
            self.driver.execute_script("arguments[0].click();", logout_link)
