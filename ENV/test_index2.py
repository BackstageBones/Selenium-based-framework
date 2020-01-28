import pytest
import logging
from .environment import env

class TestClass():

    @pytest.fixture
    def open_chrome(self, env):
        # Setup (called before test)
        logging.debug('Setup: open browser')
        env.open_file()
        # Teardown (called after test)
        def fin():
            logging.debug('Teardown: close browser')
            env.close_file()
            logging.debug('done')
