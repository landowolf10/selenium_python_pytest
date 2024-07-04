from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utils.setup import SetUp
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver

class BasePage:
    web_driver = None
    action = None

    def __init__(self, driver: RemoteWebDriver):
        self.driver = driver
        self.action = ActionChains(driver)

    def navigate_to(self, url: str):
        self.driver.get(url)

    def get_element_by(self, element_locator: By, max_wait_sec: int):
        wait = WebDriverWait(self.driver, max_wait_sec)
        return wait.until(EC.visibility_of_element_located(element_locator))

    def get_all_elements_by(self, element_locator: By):
        return self.driver.find_elements(element_locator)

    def go_to_link_text(self, link_text: str):
        self.driver.find_element(By.LINK_TEXT, link_text).click()

    def click_element(self, element_locator: By, max_wait_sec: int):
        self.get_element_by(element_locator, max_wait_sec).click()

    def click_element_from_list(self, element):
        element.click()

    def write_text(self, element_locator: By, text: str, max_wait_sec: int):
        element = self.get_element_by(element_locator, max_wait_sec)
        element.clear()
        element.send_keys(text)

    def get_element_text(self, element_locator: By, max_wait_sec: int):
        return self.get_element_by(element_locator, max_wait_sec).text

    def select_from_drop_down_by_value(self, element_locator: By, value_to_select: str, max_wait_sec: int):
        dropdown = Select(self.get_element_by(element_locator, max_wait_sec))
        dropdown.select_by_value(value_to_select)

    def select_from_drop_down_by_index(self, element_locator: By, index: int, max_wait_sec: int):
        dropdown = Select(self.get_element_by(element_locator, max_wait_sec))
        dropdown.select_by_index(index)

    def select_from_drop_down_by_text(self, element_locator: By, text: str, max_wait_sec: int):
        dropdown = Select(self.get_element_by(element_locator, max_wait_sec))
        dropdown.select_by_visible_text(text)

    def hover_over_element(self, element_locator: By, max_wait_sec: int):
        element = self.get_element_by(element_locator, max_wait_sec)
        self.action.move_to_element(element).perform()

    def double_click(self, element_locator: By, max_wait_sec: int):
        element = self.get_element_by(element_locator, max_wait_sec)
        self.action.double_click(element).perform()

    def right_click(self, element_locator: By, max_wait_sec: int):
        element = self.get_element_by(element_locator, max_wait_sec)
        self.action.context_click(element).perform()

    def get_value_from_table(self, element_locator: By, row: int, column: int, max_wait_sec: int):
        cell_xpath = f"{element_locator}/table/tbody/tr[{row}]/td[{column}]"
        print("Cell locator: ", cell_xpath)
        return self.get_element_by((By.XPATH, cell_xpath), max_wait_sec).text

    def set_value_on_table(self, element_locator: By, row: int, column: int, value: str, max_wait_sec: int):
        cell_xpath = f"{element_locator}/table/tbody/tr[{row}]/td[{column}]"
        self.get_element_by((By.XPATH, cell_xpath), max_wait_sec).send_keys(value)

    def switch_to_iframe(self, iframe_index: int):
        self.driver.switch_to.frame(iframe_index)

    def switch_to_parent_frame(self):
        self.driver.switch_to.parent_frame()

    def dismiss_alert(self):
        Alert(self.driver).dismiss()

    def wait_until_element_located(self, locator_type: By, max_wait_sec: int):
        wait = WebDriverWait(self.driver, max_wait_sec)
        wait.until(EC.visibility_of_element_located(locator_type))

    def element_is_displayed(self, locator_type: By, max_wait_sec: int):
        return self.get_element_by(locator_type, max_wait_sec).is_displayed()

    def element_is_selected(self, locator_type: By, max_wait_sec: int):
        return self.get_element_by(locator_type, max_wait_sec).is_selected()

    def element_is_enabled(self, locator_type: By, max_wait_sec: int):
        return self.get_element_by(locator_type, max_wait_sec).is_enabled()