from locators.ninja_trials_locators import NinjaTrialsLocators
from pages.basepage import BasePage


class NinjaTrialPage(BasePage):
    url = 'https://techstepacademy.com/trial-of-the-stones'

    def __init__(self, driver):
        super().__init__(driver)

    def solve_riddle_of_stones(self, text: str) -> str:
        """
        Sends text to the first riddle and retrieves answer
        :param text: text to send in to the textfield
        :return: string with riddle answer
        """
        self.actions.send_text(NinjaTrialsLocators.riddle_of_stone_textbox, text)
        self.actions.click_element(NinjaTrialsLocators.riddle_of_stone_button)

    def get_riddle_of_stones_answer(self) -> str:
        return self.actions.wait_for_element_visible(NinjaTrialsLocators.riddle_of_stone_answer_control).text.strip()

    def solve_riddle_of_secrets(self, text: str) -> str:
        """
        Sends text to the second riddle and retrieves answer
        :param text: text to send as answer
        :return: string with riddle answer
        """
        self.actions.send_text(NinjaTrialsLocators.riddle_of_secrets_textbox, text)
        self.actions.click_element(NinjaTrialsLocators.riddle_of_secrets_button)

    def get_riddle_of_secrets_answer(self) -> str:
        return self.actions.wait_for_element_visible(NinjaTrialsLocators.riddle_of_secret_answer_control).text.strip()

    def solve_the_riddle_of_two_merchants(self, first_merchant, second_merchant):
        jessica = self.the_two_merchants_jessica_control.get_text
        bernard = self.the_two_merchants_bernard_control.get_text
        if int(bernard) > int(jessica):
            self.the_name_of_the_richiest_merchant_textbox.send_text(first_merchant)
        else:
            self.the_name_of_the_richiest_merchant_textbox.send_text(second_merchant)
        self.the_two_merchants_anwser_button.click()
        return self.the_two_merchants_anwser_control.get_text

    def check_all_the_anwsers(self):
        self.check_all_anwsers_button.click()
        return self.check_all_anwsers_output_control.get_text
