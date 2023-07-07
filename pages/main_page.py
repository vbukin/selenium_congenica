from pages.base_page import BasePage
from pages.frames import FramesPage


class MainPage(BasePage):
    def __init__(self, driver, config):
        self.driver = driver
        self.config = config
        super().__init__(driver, config)

    def frames_click(self):
        self.click('a[href="/frames"]')
        return FramesPage(self.driver, self.config)

