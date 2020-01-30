import logging

import pytest

from ENV.website_main_page import WebsiteMainPage

test_path = r"C:/Users/a.miendlarzewski/PycharmProjects/Pytest-Assignment/ENV/index2.html"
chrome_path = r"C:/Users/a.miendlarzewski/PycharmProjects/Pytest-Assignment/ENV/chromedriver.exe"


class TestClass():

    @pytest.fixture(scope='session')
    def wb(self):
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

    @pytest.mark.usefixtures('wb')
    def test_webpage_element_check(self, wb):
        logging.info('Check for fields occurence - Input boxes are displayed.')
        assert wb.verify_page_elements_presence()

    @pytest.mark.usefixtures('wb')
    def test_enter_only_incompatible_name(self, wb):
        wrong_name = '#@whatever*dude'
        logging.info('Insert incorrect non-alphanumeric signs - incorrect signs entered in the name box.')
        wb.insert_first_name(wrong_name)
        logging.info('Click submit button - Submit button clicked.')
        wb.click_submit_button()
        logging.info('Wait for error message to occure - Error message displayed.')
        # to do: assert that error occures
        # wait for error monit (example only field entered, wrong first field)

    @pytest.mark.usefixtures('wb')
    def test_enter_correct_first_name_last_name(self, wb):
        name = 'Michael'
        last_name = 'Jordan'
        logging.info('Insert correct name - regular name typed in the name box.')
        wb.insert_first_name(name)
        logging.info('Insert correct last name - regular last name typed in the name box.')
        wb.insert_last_name(last_name)
        logging.info('Click submit button - Submit button clicked.')
        wb.click_submit_button()
        logging.info('check for finish screen display - Submit screen is displayed.')

    @pytest.mark.usefixtures('wb')
    def test_enter_incompatible_surname(self, wb):
        wrong_surname = '#@whatever*dude'
        logging.info('Insert incorrect non-alphanumeric signs - incorrect signs entered in the name box.')
        wb.insert_last_name(wrong_surname)
        logging.info('Click submit button - Submit button clicked.')
        wb.click_submit_button()
        logging.info('Wait for error message to occure - Error message displayed.')
        # to do: assert that error occures
        # wait for error monit (example only one field entered, wrong second field)

    @pytest.mark.usefixtures('wb')
    def test_enter_last_name_only(self, wb):
        name = 'Jordan'
        logging.info('Insert correct surname - regular surname typed in the name box.')
        wb.insert_first_name(name)
        logging.info('Click submit button - Submit button clicked.')
        wb.click_submit_button()
        # to do: assert that no error occures

    @pytest.mark.usefixtures('wb')
    def test_enter_incompatible_first_name_correct_last_name(self, wb):
        wrong_name = '#@whatever*dude'
        last_name = 'Jordan'
        logging.info('Insert incorrect non-alphanumeric signs - incorrect signs entered in the name box.')
        wb.insert_first_name(wrong_name)
        logging.info('Insert correct surname - regular surname typed in the name box.')
        wb.insert_last_name(last_name)
        logging.info('Click submit button - Submit button clicked.')
        wb.click_submit_button()
        # to do: assert that error occures
        # wait for error monit

    @pytest.mark.usefixtures('wb')
    def test_enter_correct_first_name_incorrect_last_name(self, wb):
        wrong_last_name = '#@whatever*dude'
        name = 'Jordan'
        logging.info('Insert correct name - regular name typed in the name box.')
        wb.insert_first_name(name)
        logging.info('Insert non-alphanumeric signs - incorrect signs entered in the name box.')
        wb.insert_last_name(wrong_last_name)
        logging.info('Click submit button - Submit button clicked.')
        wb.click_submit_button()
        # to do: assert that error occures
        # wait for error monit
