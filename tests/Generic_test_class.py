import pytest

from pages.ninja_trials_page import NinjaTrialPage


class GenericTestClass:


    @pytest.fixture()
    def website(self):
        website = NinjaTrialPage('https://techstepacademy.com/trial-of-the-stones')
        return website

    @pytest.fixture()
    def setup_teardown(self, website):
        # setup
        yield
        # teardown
        website.close_file()
