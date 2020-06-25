from basepage import BasePage, BaseElement
from pages.tech_step_home_page import TechStepHomePage


class NinjaTrialPage(BasePage):
    url = 'https://techstepacademy.com/trial-of-the-stones'

    def __init__(self, url):
        self.url = url
        super().__init__(url)
        self._verify_url()

        self.riddle_of_stone_textbox = BaseElement(self.driver, self.by.ID, "r1Input")
        self.riddle_of_stone_button = BaseElement(self.driver, self.by.ID, "r1Btn")
        self.riddle_of_stone_anwser_control = BaseElement(self.driver, self.by.ID, "passwordBanner", visible=False)
        self.riddle_of_secrets_textbox = BaseElement(self.driver, self.by.ID, "r2Input")
        self.riddle_of_secrets_button = BaseElement(self.driver, self.by.ID, "r2Butn")
        self.riddle_of_secret_anwser_control = BaseElement(self.driver, self.by.ID, "successBanner1", visible=False)
        self.the_two_merchants_jessica_control = BaseElement(self.driver, self.by.XPATH, "//p[text() = '3000']")
        self.the_two_merchants_bernard_control = BaseElement(self.driver, self.by.XPATH, "//p[text() = '2000']")
        self.the_name_of_the_richiest_merchant_textbox = BaseElement(self.driver, self.by.ID, "r3Input")
        self.the_two_merchants_anwser_button = BaseElement(self.driver, self.by.ID, "r3Butn")
        self.check_all_anwsers_button = BaseElement(self.driver, self.by.ID, 'checkButn')
        self.the_two_merchants_anwser_control = BaseElement(self.driver, self.by.ID, 'successBanner2', visible=False)
        self.check_all_anwsers_output_control = BaseElement(self.driver, self.by.ID, 'trialCompleteBanner',
                                                            visible=False)
        self.Home_tab = BaseElement(self.driver, self.by.ID, "lower-logo")

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
        self.Home_tab.click()
        self.set_next_page(next_page=TechStepHomePage('https://techstepacademy.com/'))


