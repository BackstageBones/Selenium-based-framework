import pytest

from ENV.Generic_test_class import GenericTestClass



class TestClass(GenericTestClass):

    @pytest.mark.usefixtures('env', 'setup_teardown')
    def test_solve_riddle_of_stones(self, env):
        global anwser
        anwser = env.solve_riddle_of_stones('rock')
        assert anwser == 'bamboo'

    @pytest.mark.usefixtures('env', 'setup_teardown')
    def test_solve_riddle_of_secrets(self, env):
        anwser_check = env.solve_riddle_of_secrets(anwser)
        assert anwser_check == 'Success!'
