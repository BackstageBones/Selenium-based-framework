import pytest

from pages.ninja_trials_page import NinjaTrialPage


class GenericTestClass:

    @pytest.fixture()
    def setup_teardown(self):
        # setup
        website = NinjaTrialPage('https://techstepacademy.com/trial-of-the-stones')
        website.open_page()
        yield
        # teardown
        website.close_file()
