from selenium import webdriver
from selenium.webdriver import ChromeOptions, Chrome


class Environment(object):
    opts = ChromeOptions()
    opts.add_experimental_option("detach", True)

    def __init__(self, file_path, chrome_path):
        self.file_path = 'file://' + file_path
        self.driver = webdriver.Chrome(chrome_path, options=Environment.opts)

    def open_file(self):
        return self.driver.get(self.file_path)




if __name__ == "__main__":
    en = Environment(r"C:/Users/Adrian-PC/PycharmProjects/Pytest/index2.html", r"C:/Users/Adrian-PC/PycharmProjects/Pytest/chromedriver.exe")
    en.open_file()