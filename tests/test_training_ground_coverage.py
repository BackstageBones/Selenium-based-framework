import pytest
from assertpy import assert_that

from pages.ninja_trials_page import NinjaTrialPage


@pytest.mark.usefixtures("driver_init", "open_ninja_trials_page")
class TestsTrainingGround:

    @pytest.mark.parametrize(
        "answer, expected_value",
        [
            pytest.param("rock", "bamboo"),
            pytest.param("stone", "", marks=pytest.mark.xfail)

        ]
    )
    def test_solve_riddle_of_stones(self, answer, expected_value):
        ninja_page = NinjaTrialPage(self.driver)
        ninja_page.solve_riddle_of_stones(answer)
        result = ninja_page.get_riddle_of_stones_answer()
        assert_that(result).is_equal_to(expected_value)
        pytest.shared = result

    @pytest.mark.parametrize("correct_answer, expected_condition",
                             [
                                 pytest.param("rock", "Success!")
                             ])
    def test_solve_riddle_of_secrets(self, correct_answer, expected_condition):
        ninja_page = NinjaTrialPage(self.driver)
        ninja_page.solve_riddle_of_stones(correct_answer)
        result = ninja_page.get_riddle_of_stones_answer()
        ninja_page.solve_riddle_of_secrets(result)
        assert_that(ninja_page.get_riddle_of_secrets_answer()).is_equal_to(expected_condition)

    # def test_solve_the_two_merchants_riddle(self, website):
    #     anwser_check = website.solve_the_riddle_of_two_merchants('Bernard', 'Jessica')
    #     assert anwser_check == 'Success!'
    #
    # def test_solve_the_trial_of_stones(self, website):
    #     anwser = website.solve_riddle_of_stones('rock')
    #     assert anwser == 'bamboo'
    #     secrets_anwser = website.solve_riddle_of_secrets(anwser)
    #     assert secrets_anwser == 'Success!'
    #     anwser_check = website.solve_the_riddle_of_two_merchants('Bernard', 'Jessica')
    #     assert anwser_check == 'Success!'
    #     finall_anwser = website.check_all_the_anwsers()
    #     assert finall_anwser == 'Trial Complete'
    #
    # def test_browser_navigation(self, website):
    #     website.navigate_to_home_tab()
