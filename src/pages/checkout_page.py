from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from pages.dashboard_page import DashboardPage
from utils.base_page import BasePage
from locators import checkout_locators, dashboard_locators

class CheckoutPage(BasePage):
    def __init__(self, driver: RemoteWebDriver):
        super().__init__(driver)

    def proceed_with_checkout(self):
        self.click_element((By.XPATH, dashboard_locators.cartIcon), 10)
        self.click_element((By.XPATH, checkout_locators.checkoutButton), 10)
        self.write_text((By.XPATH, checkout_locators.txtFirstName), "Orlando", 10)
        self.write_text((By.XPATH, checkout_locators.txtLastName), "Orlando", 10)
        self.write_text((By.XPATH, checkout_locators.txtZipCode), "Orlando", 10)
        self.click_element((By.XPATH, checkout_locators.continueButton), 10)

    def get_subtotal(self):
        return self.get_element_text((By.XPATH, checkout_locators.subtotal), 10)

    def get_item_sum(self):
        subtotal: float = 0

        for selected_item_price in DashboardPage.get_selected_item_prices():
            subtotal += selected_item_price

        return "Item total: $" + str(subtotal)
    
    def click_finish_button(self):
        DashboardPage.get_selected_item_prices().clear()
        self.click_element((By.XPATH, checkout_locators.finishButton), 10)

    def get_checkout_elements(self):
        present_elements: dict[str, bool] = {
            "order_title": self.element_is_displayed((By.XPATH, checkout_locators.orderTitle), 10),
            "order_message": self.element_is_displayed((By.XPATH, checkout_locators.orderMessage), 10),
            "home_button": self.element_is_displayed((By.XPATH, checkout_locators.backToHomeButton), 10)
        }

        return present_elements
