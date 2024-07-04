import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome,firfox",
        help="Comma-separated list of browsers to run tests with (e.g., chrome,firefox)"
    )
    parser.addoption(
        "--selenium_grid_enabled",
        action="store",
        default="False",
        help="Enable or disable Selenium Grid (e.g., True or False)"
    )

@pytest.fixture(scope="session")
def selenium_grid_enabled(request):
    return request.config.getoption("--selenium_grid_enabled").lower() == 'true'

@pytest.fixture(scope="class", params=["chrome", "firefox"])
def browser(request):
    return request.param
