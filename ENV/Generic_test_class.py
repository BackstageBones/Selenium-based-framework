import pytest

from ENV.ninja_trials_page import NinjaTrialPage


class GenericTestClass:

    @pytest.fixture()
    def env(self):
        env = NinjaTrialPage('https://techstepacademy.com/trial-of-the-stones')
        return env

    @pytest.fixture()
    def setup_teardown(self, env):
        # setup
        env.verify_elements_presence()

        yield
        # teardown
        env.close_file()
