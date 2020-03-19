from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class Environment(object):
    opts = ChromeOptions()
    opts.add_experimental_option("detach", True)
    opts.add_argument("--start-maximized")

    def __init__(self):
        self.driver = webdriver.Chrome(options=Environment.opts)
        self.wait = WebDriverWait

    def close_file(self):
        return self.driver.close()

    def is_element_present(self, resource_id) -> bool:
        return self.wait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, resource_id)))

    def get_text(self, text) -> str:
        element = self.driver.find_element_by_link_text(text)
        return element.text

    def get_text_by_xpath(self, xpath) -> str:
        element = self.driver.find_element_by_xpath(xpath)
        return element.text

    def get_text_by_id(self, id) -> str:
        element = self.driver.find_element_by_id(id)
        return element.text

    def click_element(self, resource_id) -> bool:
        if self.is_element_present(resource_id):
            element = self.driver.find_element_by_id(resource_id)
            element.click()
            return True
        else:
            return False

    def input_text(self, resource_id, string) -> bool:
        box = self.driver.find_element_by_id(resource_id)
        box.send_keys(string)
        box.send_keys(Keys.ENTER)
        return box.text == string


class Button(Environment):

    def __init__(self, resource_id):
        self.resource_id = None
        super().__init__()
        self.wait(self.driver, timeout=10).until(EC.element_to_be_clickable((By.ID, self.resource_id)))

    def click(self):
        return self.driver.find_element_by_id(self.resource_id).click()
