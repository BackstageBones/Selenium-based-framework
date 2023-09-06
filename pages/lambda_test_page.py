from pages.basepage import BasePage
from locators.lambda_test_locators import LambdaTestLocators


class LambdaTestPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def mark_all_checkboxes(self) -> None:
        for checkbox in self.actions.wait_for_elements_visible(LambdaTestLocators.checkboxes):
            self.actions.click_element(checkbox)
