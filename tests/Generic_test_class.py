import pytest

from pages.ninja_trials_page import NinjaTrialPage


class GenericTestClass:


    @pytest.fixture()
    def website(self):
        website = NinjaTrialPage()
        return website

    @pytest.fixture()
    def setup_teardown(self, website):
        # setup
        yield
        # teardown
        website.close_file()
