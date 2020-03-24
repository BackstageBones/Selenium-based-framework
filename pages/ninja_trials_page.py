from environment import Environment, Button, WebControl, InputControl


class NinjaTrialPage(Environment):

    def __init__(self, url):
        self.url = url
        super().__init__()
        self.driver.get(self.url)

        self.riddle_of_stone_textbox = InputControl(self.by.ID, "r1Input")
        self.riddle_of_stone_button = Button(self.by.ID, "r1Btn")
        self.riddle_of_stone_anwser_control = WebControl(self.by.ID, "passwordBanner")
        self.riddle_of_secrets_textbox = InputControl(self.by.ID, "r2Input")
        self.riddle_of_secrets_button = Button(self.by.ID, "r2Butn")
        self.riddle_of_secret_anwser_control = WebControl(self.by.ID, "successBanner1")
        self.the_two_merchants_jessica_control = WebControl(self.by.xpath, "//p[text() = '3000']")
        self.the_two_merchants_bernard_control = WebControl(self.by.xpath, "//p[text() = '2000']")
        self.the_name_of_the_richiest_merchant_textbox = InputControl(self.by.ID, "r3Input")
        self.the_two_merchants_anwser_button = Button(self.by.ID, "r3Butn")
        self.the_two_merchants_anwser_control = WebControl(self.by.ID, 'successBanner2')
        self.check_all_anwsers_button = Button(self.by.ID, 'checkButn')
        self.check_all_anwsers_output_control = WebControl(self.by.ID, 'trialCompleteBanner')

    def solve_riddle_of_stones(self, text):
        self.riddle_of_stone_textbox.send_text(text)
        self.riddle_of_stone_button.click()
        return self.riddle_of_stone_anwser_control.get_text

    def solve_riddle_of_secrets(self, text):
        self.riddle_of_secrets_textbox.send_text(text)
        self.riddle_of_secrets_button.click()
        return self.riddle_of_secret_anwser_control.get_text

    def solve_the_riddle_of_two_merchants(self):
        jessica = self.the_two_merchants_jessica_control.get_text
        bernard = self.the_two_merchants_bernard_control.get_text
        if int(bernard) > int(jessica):
            self.the_name_of_the_richiest_merchant_textbox.send_text('Bernard')
        else:
            self.the_name_of_the_richiest_merchant_textbox.send_text('Jessica')
        self.the_two_merchants_anwser_button.click()
        return self.the_two_merchants_anwser_control.get_text

    def check_all_the_anwsers(self):
        self.check_all_anwsers_button.click()
        return self.check_all_anwsers_output_control.get_text


# env = NinjaTrialPage('https://techstepacademy.com/trial-of-the-stones')
print(InputControl.__mro__)

