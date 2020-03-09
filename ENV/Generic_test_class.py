from .environment import Environment
from .ninja_trials_page import NinjaTrialPage
import pytest


class GenericTestClass(Environment):

    def __init__(self):
        super().__init__()

    @pytest.fixture(scope='session')
    def setup_teardown(self):
        # setup
        env.verify_elements_presence()

        yield
        #teardown
        env.close_file()

if __name__ == '__main__':
    env = NinjaTrialPage('https://techstepacademy.com/trial-of-the-stones')
