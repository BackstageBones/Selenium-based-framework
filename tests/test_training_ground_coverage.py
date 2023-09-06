import pytest
from assertpy import assert_that

from pages.ninja_trials_page import NinjaTrialPage
from test_lambdatest import BasicChromeTest


@pytest.mark.usefixtures("open_ninja_trials_page")
class TrainingGroundTests(BasicChromeTest):
    pytest.mark.parametrize(
        "answer",
        [
            pytest.param("rock", marks=pytest.mark.basic),
            pytest.param("stone", marks=pytest.mark.xfail),

        ]
    )

    def test_solve_riddle_of_stones(self, answer):
        ninja_page = NinjaTrialPage(self.driver)
        ninja_page.solve_riddle_of_stones(answer)
        answer = ninja_page.get_riddle_of_stones_answer()
        assert_that(answer).is_equal_to("bamboo")
        return answer

    def test_solve_riddle_of_secrets(self):
        ninja_page = NinjaTrialPage(self.driver)
        ninja_page.solve_riddle_of_secrets(self.test_solve_riddle_of_stones('rock'))
        assert_that(ninja_page.get_riddle_of_secrets_answer()).is_equal_to("Success!")

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
