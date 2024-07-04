import pytest
from assertpy import assert_that
from utils.setup import SetUp  # Assuming setup.py contains the SetUp class
from tests.common_test import CommonTest


@pytest.mark.usefixtures("selenium_grid_enabled", "browser")
class TestLogin:
    @pytest.fixture(autouse=True)
    def setup_class(self, selenium_grid_enabled, browser):
        self.selenium_grid_enabled = selenium_grid_enabled
        self.browser = browser
        self.common_test = CommonTest(self.selenium_grid_enabled)
        self.login_page = self.common_test.get_login_page(self.browser)
        self.common_test.navigate(self.browser)
        yield
        self.common_test.setUp_instance.quit_driver()

    def test_successful_login(self):
        self.common_test.successful_login(self.browser)

    def test_invalid_login(self):
        self.login_page.write_credentials("standard_use", "secret_sauce")
        self.login_page.click_login_button()
        invalid_elements = self.login_page.get_invalid_login_elements()
        assert_that(invalid_elements["login_button"]).is_true()
        assert_that(invalid_elements["error_message"]).is_true()
        assert_that(self.login_page.get_error_message_text()).is_equal_to(
            "Epic sadface: Username and password do not match any user in this service"
        )
