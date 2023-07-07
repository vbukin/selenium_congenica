import time

from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    def __init__(self, driver, config):
        self.driver = driver
        super().__init__(driver, config)

    def frames_click(self):
        self.click('a[href="/frames"]')

