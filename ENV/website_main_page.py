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