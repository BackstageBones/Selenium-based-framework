from pages.basepage import BasePage
import logging

class WebsiteMainPage(BasePage):

    def __init__(self):
        self.header = self.is_element_present("header")

        super().__init__()


        self.form_resource_id = 'test-form'
        self.first_name_resource_id = "firstname-input"
        self.last_name_resource_id = "lastname-input"
        self.submit_button_resource_id = "submit-button"

    def verify_page_elements_presence(self) -> bool:
        logging.debug('trying to check for all visible elements')
        if self.is_element_present(self.form_resource_id):
            if self.is_element_present(self.first_name_resource_id):
                if self.is_element_present(self.last_name_resource_id):
                    if self.is_element_present(self.submit_button_resource_id):
                        return True
        return False

    def insert_first_name(self, text):
        logging.debug('trying to insert text in the specified field')
        self.input_text(self.first_name_resource_id, text)

    def insert_last_name(self, text):
        logging.debug('trying to insert text in the specified field')
        self.input_text(self.last_name_resource_id, text)

    def click_submit_button(self):
        logging.debug('trying to click visible submit button')
        self.click_element(self.submit_button_resource_id)
