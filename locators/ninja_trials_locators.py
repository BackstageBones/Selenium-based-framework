from dataclasses import dataclass

from selenium.webdriver.common.by import By


@dataclass()
class NinjaTrialsLocators:
    riddle_of_stone_textbox: By = (By.ID, "r1Input")
    riddle_of_stone_button: By = (By.ID, "r1Btn")
    riddle_of_stone_answer_control: By = (By.ID, "passwordBanner")
    riddle_of_secrets_textbox: By = (By.ID, "r2Input")
    riddle_of_secrets_button: By = (By.ID, "r2Butn")
    riddle_of_secret_answer_control: By = (By.ID, "successBanner1")
    the_two_merchants_jessica_control: By = (By.XPATH, "//p[text() = '3000']")
    the_two_merchants_bernard_control: By = (By.XPATH, "//p[text() = '2000']")
    the_name_of_the_richiest_merchant_textbox: By = (By.ID, "r3Input")
    the_two_merchants_answer_button: By = (By.ID, "r3Butn")
    check_all_answers_button: By = (By.ID, 'checkButn')
    the_two_merchants_answer_control: By = (By.ID, 'successBanner2')
    check_all_answers_output_control: By = (By.ID, 'trialCompleteBanner')
    Home_tab = (By.ID, "lower-logo")
