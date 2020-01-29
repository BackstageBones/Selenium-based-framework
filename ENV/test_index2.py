import logging

import pytest

from ENV.website_main_page import WebsiteMainPage

test_path = r"C:/Users/a.miendlarzewski/PycharmProjects/Pytest-Assignment/ENV/index2.html"
chrome_path = r"C:/Users/a.miendlarzewski/PycharmProjects/Pytest-Assignment/ENV/chromedriver.exe"
class TestClass():

    @pytest.fixture(autouse=True, scope='class')
    def open_chrome(self):
        wb = WebsiteMainPage(test_path,
                             chrome_path)
        # Setup (called before test)
        logging.debug('Setup: open browser')
        wb.open_file()

        yield wb
        # Teardown (called after test)
        logging.debug('Teardown: close browser')
        wb.close_file()
        logging.debug('done')


    @pytest.mark.usefixtures('open_chrome')
    def test_webpage_element_check(self):
        assert wb.verify_page_elements_presence()
