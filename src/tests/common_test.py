from utils.setup import SetUp
from pages.login_page import LoginPage

class CommonTest:
    def __init__(self, selenium_grid_enabled):
        self.selenium_grid_enabled = selenium_grid_enabled
        self.setUp_instance = SetUp()

    def get_login_page(self, browser):
        driver = self.setUp_instance.get_driver(browser, self.selenium_grid_enabled)
        return LoginPage(driver)

    def navigate(self, browser):
        self.get_login_page(browser).navigate_to_sauce_lab()

    def successful_login(self, browser):
        login_page = self.get_login_page(browser)
        login_page.write_credentials("standard_user", "secret_sauce")
        login_page.click_login_button()
        valid_elements = login_page.get_valid_login_elements()
        assert valid_elements["cart_icon"].is_displayed()
        assert valid_elements["drop_down"].is_displayed()
