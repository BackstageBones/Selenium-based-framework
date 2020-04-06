import pytest

from tests.Generic_test_class import GenericTestClass


class TestClass(GenericTestClass):

    @pytest.mark.usefixtures('setup_teardown')
    def test_solve_riddle_of_stones(self, website):
        global anwser
        anwser = website.solve_riddle_of_stones('rock')
        assert anwser == 'bamboo'

    @pytest.mark.usefixtures('setup_teardown')
    def test_solve_riddle_of_secrets(self, website):
        secrets_anwser = website.solve_riddle_of_secrets(anwser)
        assert secrets_anwser == 'Success!'

    @pytest.mark.usefixtures('setup_teardown')
    def test_solve_the_two_merchants_riddle(self, website):
        anwser_check = website.solve_the_riddle_of_two_merchants('Bernard','Jessica')
        assert anwser_check == 'Success!'

    @pytest.mark.usefixtures('setup_teardown')
    def test_solve_the_trial_of_stones(self, website):
        anwser = website.solve_riddle_of_stones('rock')
        assert anwser == 'bamboo'
        secrets_anwser = website.solve_riddle_of_secrets(anwser)
        assert secrets_anwser == 'Success!'
        anwser_check = website.solve_the_riddle_of_two_merchants()
        assert anwser_check == 'Success!'
        finall_anwser = website.check_all_the_anwsers()
        assert finall_anwser == 'Trial Complete'
