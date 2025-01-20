import pytest
from assertpy import assert_that
from tests.common_test import CommonTest


@pytest.mark.usefixtures("selenium_grid_enabled", "browser")
class TestLogin:
    @pytest.fixture(autouse=True)
    def setup(self, selenium_grid_enabled, browser):
        # Initialize CommonTest with browser and grid settings
        self.common_test = CommonTest(selenium_grid_enabled, browser)
        self.common_test.navigate()
        yield
        # Quit driver after tests
        self.common_test.setUp_instance.quit_driver()

    def test_successful_login(self):
        self.common_test.successful_login()

    def test_invalid_login(self):
        login_page = self.common_test.login_page

        login_page.write_credentials("standard_use", "secret_sauce")
        login_page.click_login_button()
        invalid_elements = login_page.get_invalid_login_elements()
        assert_that(invalid_elements["login_button"]).is_true()
        assert_that(invalid_elements["error_message"]).is_true()
        assert_that(login_page.get_error_message_text()).is_equal_to(
            "Epic sadface: Username and password do not match any user in this service"
        )
