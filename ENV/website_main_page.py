from .environment import Environment

class WebsiteMainPage(Environment):

    def __init__(self, file_path, chrome_path):
        super().__init__(file_path, chrome_path)

        self.form_resource_id = 'test-form'
        self.first_name_resource_id = "firstname-input"
        self.last_name_resource_id = "lastname-input"
        self.submit_button_resource_id = "submit-button"

    def verify_page_elements_presence(self) -> bool:
        if self.is_element_present(self.form_resource_id):
            if self.is_element_present(self.first_name_resource_id):
                if self.is_element_present(self.last_name_resource_id):
                    if self.is_element_present(self.submit_button_resource_id):
                        return True
        return False

    def insert_first_name(self, text):
        self.input_text(self.first_name_resource_id, text)

    def insert_last_name(self, text):
        self.input_text(self.last_name_resource_id, text)

    def click_submit_button(self):
        self.click_element(self.submit_button_resource_id)