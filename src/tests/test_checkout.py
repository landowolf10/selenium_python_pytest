import pytest
from assertpy import assert_that
from pages.checkout_page import CheckoutPage
from pages.dashboard_page import DashboardPage
from tests.common_test import CommonTest


@pytest.mark.usefixtures("selenium_grid_enabled", "browser")
class TestCheckout:
    @pytest.fixture(autouse=True)
    def setup(self, selenium_grid_enabled, browser):
        # Initialize CommonTest with browser and grid settings
        self.common_test = CommonTest(selenium_grid_enabled, browser)
        self.dashboard_page = DashboardPage(self.common_test.driver)
        self.checkout_page = CheckoutPage(self.common_test.driver)
        self.common_test.navigate()
        self.common_test.successful_login()
        yield
        # Quit driver after tests
        self.common_test.setUp_instance.quit_driver()

    def perform_checkout_steps(self):
        self.dashboard_page.sort_dropdown()
        self.dashboard_page.add_product()
        self.dashboard_page.add_product()
        self.checkout_page.proceed_with_checkout()
        print("Subtotal: ", self.checkout_page.get_subtotal())
        assert_that(self.checkout_page.get_item_sum()).is_equal_to(self.checkout_page.get_subtotal())
        self.checkout_page.click_finish_button()

    def test_checkout(self):
        """Test that completes the checkout process."""
        self.perform_checkout_steps()

    def test_finish_checkout(self):
        self.perform_checkout_steps()

        assert self.checkout_page.get_checkout_elements().get("order_title") is not None
        assert self.checkout_page.get_checkout_elements().get("order_message") is not None
        assert self.checkout_page.get_checkout_elements().get("home_button") is not None
