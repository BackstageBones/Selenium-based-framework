from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.remote.webdriver import WebElement
from selenium.common.exceptions import TimeoutException


class SeleniumActions:
    DEFAULT_TIMEOUT = 20

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator) -> WebElement:
        return self.driver.find_element(*locator)

    def find_elements(self, locator) -> list:
        return self.driver.find_elements(*locator)

    def wait_for_elements_visible(self, locator) -> list:
        return WebDriverWait(self.driver, timeout=SeleniumActions.DEFAULT_TIMEOUT).until(
            ec.visibility_of_any_elements_located(locator)
        )

    def click_element(self, locator) -> None:
        element = WebDriverWait(self.driver, timeout=SeleniumActions.DEFAULT_TIMEOUT).until(
            ec.element_to_be_clickable(locator)
        )
        element.click()
