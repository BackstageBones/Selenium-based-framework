from .environment import Environment
from .ninja_trials_page import NinjaTrialPage
import pytest


class GenericTestClass(Environment):

    def __init__(self):
        super().__init__()

    @pytest.fixture()
    def setup_teardown(self):
        # setup
        env = NinjaTrialPage('https://techstepacademy.com/trial-of-the-stones')

        yield
        #teardown
        env.close_file()
