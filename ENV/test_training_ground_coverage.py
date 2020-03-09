import pytest

from ENV.Generic_test_class import GenericTestClass


class TestClass(GenericTestClass):

    pytest.mark.usefixtures('setup_teardown')
    def test_solve_riddle_of_stones(self, setup_teardown):
        global anwser
        anwser = self.solve_riddle_of_stones('rock')
        assert anwser == 'bamboo'

    pytest.mark.usefixtures('setup_teardown')
    def test_solve_riddle_of_secrets(self):
        anwser_check = self.solve_riddle_of_secrets(anwser)
        assert anwser_check == 'Success!'
