from utils.base_page import BasePage
from utils.constant_data import URL
from utils.setup import SetUp
from pages.login_page import LoginPage
from selenium.webdriver.remote.webdriver import WebDriver

class CommonTest (BasePage):
    def __init__(self, selenium_grid_enabled: bool, browser: str):
        self.setUp_instance = SetUp()
        self.driver: WebDriver = self.setUp_instance.get_driver(browser, selenium_grid_enabled)
        super().__init__(self.driver)  # Initialize BasePage with the driver
        self.login_page = LoginPage(self.driver)

    def navigate(self):
        self.navigate_to(URL)

    def successful_login(self):
        self.login_page.write_credentials("standard_user", "secret_sauce")
        self.login_page.click_login_button()
        valid_elements = self.login_page.get_valid_login_elements()
        assert valid_elements["cart_icon"].is_displayed()
        assert valid_elements["drop_down"].is_displayed()

    def quit(self):
        self.setUp_instance.quit_driver()
