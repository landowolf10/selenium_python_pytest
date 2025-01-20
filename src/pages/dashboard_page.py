from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver, WebElement
from utils.base_page import BasePage
from locators import dashboard_locators

class DashboardPage(BasePage):
    selected_item_prices: list[float] = []

    def __init__(self, driver: RemoteWebDriver):
        super().__init__(driver)

    def sort_dropdown(self):
        """Select 'Price (high to low)' from the sort dropdown."""
        self.select_from_drop_down_by_text((By.XPATH, dashboard_locators.sortDropDown), "Price (high to low)", 10)

    def add_product(self):
        """Add a product to the cart if its price is less than 20."""
        web_elements: list[WebElement] = self.get_all_elements_by(By.XPATH, dashboard_locators.addToCartButton)
        prices: list[float] = self.get_prices()

        for i in range(len(prices)):
            if prices[i] < 20:
                self.click_element(web_elements[i])
                self.selected_item_prices.append(prices[i])
                # Remove the selected item from the lists
                del prices[i]
                del web_elements[i]
                break

    def get_prices(self):
        """Fetch prices of all products as a list of floats."""
        price_elements: list[WebElement] = self.get_all_elements_by(By.XPATH, dashboard_locators.productPrice)
        prices: list[float] = []

        for element in price_elements:
            # Remove the currency symbol and convert the price to float
            price = float(element.text[1:])
            prices.append(price)

        return prices

    @staticmethod
    def get_selected_item_prices():
        """Return the selected item prices."""
        print(f"Selected Item Prices: {DashboardPage.selected_item_prices}")
        return DashboardPage.selected_item_prices
