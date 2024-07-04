from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from utils.base_page import BasePage
from utils.constant_data import URL
from locators import login_locators, dashboard_locators

class LoginPage(BasePage):
    def __init__(self, driver: RemoteWebDriver):
        super().__init__(driver)

    def navigate_to_sauce_lab(self):
        self.navigate_to(URL)

    def click_login_button(self):
        self.click_element((By.XPATH, login_locators.loginButton), 10)

    def write_credentials(self, email: str, password: str):
        self.write_text((By.XPATH, login_locators.userTextbox), email, 10)
        self.write_text((By.XPATH, login_locators.passwordTextbox), password, 10)

    def get_valid_login_elements(self):
        present_elements = {
            "cart_icon": self.get_element_by((By.XPATH, dashboard_locators.cartIcon), 10),
            "drop_down": self.get_element_by((By.XPATH, dashboard_locators.sortDropDown), 10)
        }
        return present_elements

    def get_invalid_login_elements(self):
        present_elements = {
            "login_button": self.element_is_displayed((By.XPATH, login_locators.loginButton), 10),
            "error_message": self.element_is_displayed((By.XPATH, login_locators.errorMessage), 10)
        }
        return present_elements

    def get_error_message_text(self):
        return self.get_element_text((By.XPATH, login_locators.errorMessage), 10)
