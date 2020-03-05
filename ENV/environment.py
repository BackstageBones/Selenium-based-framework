from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.keys import Keys


class Environment(object):
    opts = ChromeOptions()
    opts.add_experimental_option("detach", True)


    def __init__(self):
        self.driver = webdriver.Chrome(options=Environment.opts)


    def close_file(self):
        return self.driver.close()

    def is_element_present(self, resource_id) -> bool:
        element = self.driver.find_element_by_id(resource_id)
        return element.is_displayed()

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

    def input_text(self, resource_id, string) -> None:
        box = self.driver.find_element_by_id(resource_id)
        box.send_keys(string)
        box.send_keys(Keys.ENTER)




