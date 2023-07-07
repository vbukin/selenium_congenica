import time

from pages.base_page import BasePage
from pages.nested_frames import NestedFramesPage


class DynamicLoading(BasePage):
    def __init__(self, driver, config):
        self.driver = driver
        self.config = config
        self.path = 'dynamic_loading'
        super().__init__(driver, config)

    def visit(self, index):
        self.visit_page(f'{self.path}/{index}')

    def start_button_click(self):
        self.click('#start > button')

    def wait_until_loading(self):
        for i in range(100):
            time.sleep(0.1)

            element = self.find_element("#loading")
            style_attribute = element.get_attribute("style")
            if "display: none" not in style_attribute:
                return True

        return False

    def get_finish_text(self):
        return self.find_element('#finish').text


