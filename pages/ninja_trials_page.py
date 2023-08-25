from pages.basepage import BasePage
from pages.tech_step_home_page import TechStepHomePage


class NinjaTrialPage(BasePage):
    url = 'https://techstepacademy.com/trial-of-the-stones'

    def __init__(self):
        self.url = NinjaTrialPage.url
        super().__init__(self.url)
        self._verify_url()


    def solve_riddle_of_stones(self, text):
        self.riddle_of_stone_textbox.send_text(text)
        self.riddle_of_stone_button.click()
        return self.riddle_of_stone_anwser_control.get_text

    def solve_riddle_of_secrets(self, text):
        self.riddle_of_secrets_textbox.send_text(text)
        self.riddle_of_secrets_button.click()
        return self.riddle_of_secret_anwser_control.get_text

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

    def navigate_to_home_tab(self):
        self.set_next_page(trigger=self.Home_tab, next_page=TechStepHomePage('https://techstepacademy.com/'))
        return self


