from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import os

class SetUp:
    driver = None
    driver_instance_exists = False
    driver_instance = None

    def get_driver(self, browser_name, is_selenium_grid_enabled: bool):
        if self.driver_instance_exists:
            self.driver = self.driver_instance
        else:
            if is_selenium_grid_enabled:
                self.driver = self.create_remote_driver(browser_name)
            else:
                self.driver = self.create_local_driver(browser_name)

        self.driver_instance_exists = True
        self.driver_instance = self.driver

        print("Browser: ", browser_name)
        return self.driver
    
    def create_remote_driver(cls, browser: str):
        capabilities = None
        ip = os.getenv("GRID_HUB_HOST")
        grid_hub_host = f"http://{ip}:4444/wd/hub"

        if browser.lower() == "chrome":
            ChromeDriverManager().install()
            chrome_options = ChromeOptions()
            # chrome_options.add_argument("--remote-allow-origins=*")
            # chrome_options.add_argument("--headless=new")
            capabilities = chrome_options.to_capabilities()
        elif browser.lower() == "firefox":
            GeckoDriverManager().install()
            firefox_options = FirefoxOptions()
            # firefox_options.add_argument("--headless")
            capabilities = firefox_options.to_capabilities()

        if capabilities:
            return RemoteWebDriver(command_executor=grid_hub_host, desired_capabilities=capabilities)
        else:
            raise RuntimeError("Capabilities not set for the browser")

    def create_local_driver(self, browser_name):
        if browser_name.lower() == "chrome":
            ChromeDriverManager().install()
            chrome_options = ChromeOptions()
            # chrome_options.add_argument("--remote-allow-origins=*")
            chrome_options.add_argument("--headless")
            self.driver = webdriver.Chrome(service=ChromeService(), options=chrome_options)
        elif browser_name.lower() == "firefox":
            GeckoDriverManager().install()
            firefox_options = FirefoxOptions()
            firefox_options.add_argument("--headless")
            self.driver = webdriver.Firefox(service=FirefoxService(), options=firefox_options)

        self.driver.maximize_window()
        #self.wait = WebDriverWait(self.driver, 10)

        return self.driver

    def quit_driver(self):
        if self.driver_instance_exists:
            current_driver = self.driver_instance
            current_driver.quit()

        self.driver_instance_exists = False
        self.driver_instance = None
