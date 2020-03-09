import pytest

from ENV.ninja_trials_page import NinjaTrialPage


class GenericTestClass(NinjaTrialPage):

    @pytest.fixture(scope='session')
    def setup_teardown(self):
        # setup
        env = NinjaTrialPage('https://techstepacademy.com/trial-of-the-stones')
        env.verify_elements_presence()

        yield
        # teardown
        env.close_file()
