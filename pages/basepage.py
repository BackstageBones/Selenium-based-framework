from pages.selenium_actions import SeleniumActions


class BasePage(object):

    def __init__(self, driver):
        self.actions = SeleniumActions(driver)

    def _open_webpage(self, url):
        return self.actions.driver.get(url)

    @property
    def _get_page_title(self):
        return self.actions.driver.title

    def set_next_page(self, next_page: object) -> object:
        self.__class__ = next_page.__class__
        self.__dict__ = next_page.__dict__
        return next_page
