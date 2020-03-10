from ENV.environment import Environment


class NinjaTrialPage(Environment):

    def __init__(self, web_address):
        super().__init__()
        self.web_address = web_address
        self.driver.get(web_address)

        self.riddle_of_stone_text_input_id = "r1Input"
        self.button_anwser_riddle_of_stone_id = "r1Btn"
        self.riddle_of_stone_anwser_id = "passwordBanner"
        self.riddle_of_secrets_text_input_id = "r2Input"
        self.button_riddle_of_secrets_id = "r2Butn"
        self.riddle_of_secret_anwser_id = "successBanner1"
        self.the_two_merchants_jessica_xpath = "//p[text() = '3000']"
        self.the_two_merchants_bernard_xpath =  "//p[text() = '2000']"

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

    #def solve_the_two_merchants_riddle(self):


