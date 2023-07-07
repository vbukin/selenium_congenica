from pages.base_page import BasePage


class NestedFramesPage(BasePage):
    def __init__(self, driver, config):
        self.driver = driver
        super().__init__(driver, config)

    def get_left_frame_text(self):
        self.switch_to_frame('[name="frame-top"]')
        self.switch_to_frame('[name="frame-left"]')
        text = self.find_element('body').text
        self.switch_to_default_content()
        return text

    def get_middle_frame_text(self):
        self.switch_to_frame('[name="frame-top"]')
        self.switch_to_frame('[name="frame-middle"]')
        text = self.find_element('body').text
        self.switch_to_default_content()
        return text

    def get_right_frame_text(self):
        self.switch_to_frame('[name="frame-top"]')
        self.switch_to_frame('[name="frame-right"]')
        text = self.find_element('body').text
        self.switch_to_default_content()
        return text

    def get_bottom_frame_text(self):
        self.switch_to_frame('[name="frame-bottom"]')
        text = self.find_element('body').text
        self.switch_to_default_content()
        return text
