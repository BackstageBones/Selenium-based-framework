from ENV.environment import Environment


class NinjaTrialPage(Environment):

    def __init__(self, web_address):
        self.web_address = web_address
        super().__init__()
        self.driver.get(web_address)

        self.riddle_of_stone_text_input_id = "r1Input"
        self.button_anwser_riddle_of_stone_id = "r1Btn"
        self.riddle_of_stone_anwser_id = "passwordBanner"
        self.riddle_of_secrets_text_input_id = "r2Input"
        self.button_riddle_of_secrets_id = "r2Butn"
        self.riddle_of_secret_anwser_id = "successBanner1"
        self.the_two_merchants_jessica_xpath = "//p[text() = '3000']"
        self.the_two_merchants_bernard_xpath = "//p[text() = '2000']"
        self.the_name_of_the_richiest_merchant_id = "r3Input"
        self.the_two_merchants_anwser_button_id = "r3Butn"
        self.the_two_merchants_anwser_id = 'successBanner2'
        self.check_anwsers_id = 'checkButn'
        self.check_anwsers_output_id = 'trialCompleteBanner'

    def verify_elements_presence(self) -> bool:
        if self.is_element_present(self.riddle_of_stone_text_input_id):
            if self.is_element_present(self.button_anwser_riddle_of_stone_id):
                if self.is_element_present(self.riddle_of_secrets_text_input_id):
                    if self.is_element_present(self.button_riddle_of_secrets_id):
                        return True
        return False

    def solve_riddle_of_stones(self, text):
        self.input_text(self.riddle_of_stone_text_input_id, text)
        self.click_element(self.button_anwser_riddle_of_stone_id)
        return self.get_text_by_id(self.riddle_of_stone_anwser_id)

    def solve_riddle_of_secrets(self, text):
        self.input_text(self.riddle_of_secrets_text_input_id, text)
        self.click_element(self.button_riddle_of_secrets_id)
        return self.get_text_by_id(self.riddle_of_secret_anwser_id)

    def solve_the_riddle_of_two_merchants(self):
        jessica = self.get_text_by_xpath(self.the_two_merchants_jessica_xpath)
        bernard = self.get_text_by_xpath(self.the_two_merchants_bernard_xpath)
        if int(bernard) > int(jessica):
            self.input_text(self.the_name_of_the_richiest_merchant_id, 'Bernard')
        else:
            self.input_text(self.the_name_of_the_richiest_merchant_id, 'Jessica')
        self.click_element(self.the_two_merchants_anwser_button_id)
        return self.get_text_by_id(self.the_two_merchants_anwser_id)

    def check_all_the_anwsers(self):
        self.click_element(self.check_anwsers_id)
        return self.get_text_by_id(self.check_anwsers_output_id)
