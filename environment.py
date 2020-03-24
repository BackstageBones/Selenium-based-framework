from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Environment(object):
    opts = ChromeOptions()
    opts.add_experimental_option("detach", True)
    opts.add_argument("--start-maximized")

    def __init__(self):
        self.driver = webdriver.Chrome(options=Environment.opts)
        self.wait = WebDriverWait
        self.by = By

    def close_file(self):
        return self.driver.close()


class Button(Environment):

    def __init__(self, by, locator):
        super().__init__()
        self.by = by
        self.source = (self.by, locator)
        self._web_element = None
        self._initialize()

    def _initialize(self) -> object:
        self._web_element = self.wait(self.driver, 10).until(EC.element_to_be_clickable((self.source)))
        return self._web_element

    def click(self) -> None:
        return self._web_element.click()


class WebControl(Environment):

    def __init__(self, by, locator):
        super().__init__()
        self.by = by
        self.source = (self.by, locator)
        self._web_element = None
        self._initialize()

    def _initialize(self) -> object:
        self._web_element = self.wait(self.driver, 10).until(EC.visibility_of_element_located((self.source)))
        return self._web_element

    @property
    def get_text(self) -> str:
        return self._web_element.text


class InputControl(Environment):

    def __init__(self, by, locator):
        super().__init__()
        self.by = by
        self.source = (self.by, locator)
        self._web_element = None
        self._initialize()

    def _initialize(self) -> object:
        self._web_element = self.wait(self.driver, 10).until(EC.visibility_of_element_located((self.source)))
        return self._web_element

    def send_text(self, string) -> None:
        self._web_element.clear()
        self._web_element.send_keys(string)
