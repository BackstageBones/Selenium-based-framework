from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.keys import Keys


class Environment(object):
    opts = ChromeOptions()
    opts.add_experimental_option("detach", True)

    def __init__(self, file_path, chrome_path):
        self.file_path = 'file://' + file_path
        self.driver = webdriver.Chrome(chrome_path, options=Environment.opts)

    def open_file(self):
        return self.driver.get(self.file_path)

    def close_file(self):
        return self.driver.close()

    def is_element_present(self, resource_id) -> bool:
        element = self.driver.find_element_by_id(resource_id)
        return element.is_displayed()

    def verify_text(self, text) -> str:
        element = self.driver.find_element_by_link_text(text)
        return element.text

    def click_element(self, resource_id) -> bool:
        if self.is_element_present(resource_id):
            element = self.driver.find_element_by_id(resource_id)
            element.click()
            return True
        else:
            return False

    def input_text(self, string, resource_id) -> None:
        box = self.driver.find_element_by_id(resource_id)
        box.send_keys(string)
        box.send_keys(Keys.ENTER)


if __name__ == "__main__":
    en = Environment(r"C:/Users/Adrian-PC/PycharmProjects/Pytest/index2.html",
                     r"C:/Users/Adrian-PC/PycharmProjects/Pytest/chromedriver.exe")
    en.open_file()
