from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):
    opts = ChromeOptions()
    opts.add_experimental_option("detach", True)
    opts.add_argument("--start-maximized")

    def __init__(self, url):
        self.url = url
        self.by = By
        self.driver = webdriver.Chrome(options=BasePage.opts)
        self._open_webpage()

    def close_file(self):
        return self.driver.close()

    def _open_webpage(self):
        return self.driver.get(self.url)

    def _verify_header(self):
        return self.driver.title


class BaseElement:

    def __init__(self, driver, by, locator, visible=True):
        self.driver = driver
        self.by = by
        self.source = (self.by, locator)
        self._web_element = None
        self.visible = visible
        if self.visible:
            self._initialize()

    def _initialize(self) -> object:
        self._web_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.source))
        return self._web_element

    def click(self) -> None:
        self._web_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.source))
        return self._web_element.click()

    @property
    def get_text(self) -> str:
        if not self.visible:
            self._initialize()
        return self._web_element.text

    def send_text(self, string) -> None:
        if not self.visible:
            self._initialize()
        self._web_element.clear()
        self._web_element.send_keys(string)
