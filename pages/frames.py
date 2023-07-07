from pages.base_page import BasePage
from pages.nested_frames import NestedFramesPage


class FramesPage(BasePage):
    def __init__(self, driver, config):
        self.driver = driver
        self.config = config
        super().__init__(driver, config)

    def nested_frames_click(self):
        self.click('a[href="/nested_frames"]')
        return NestedFramesPage(self.driver, self.config)
