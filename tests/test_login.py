import time

import pytest
from utils.constans.enums import ScreenSize
from pages.main_page import MainPage


@pytest.mark.parametrize("driver", [ScreenSize.DESKTOP], indirect=True)
def test_check_address_by_name(driver, config):
    login_page = MainPage(driver, config)
    login_page.visit_page()
    login_page.frames_click()
    time.sleep(100)



