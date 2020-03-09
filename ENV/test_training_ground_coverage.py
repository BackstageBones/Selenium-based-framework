import pytest
from .Generic_test_class import env

class Test_Trainig_ground(env):



    pytest.mark.usefixtures('setup_teardown')
    def test_solve_riddle_of_stones(self, setup_teardown):
        anwser = env.solve_riddle_of_stones()
        assert anwser == 'bamboo'
        return anwser

    pytest.mark.usefixtures('setup_teardown')

