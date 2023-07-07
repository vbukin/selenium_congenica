import time

import pytest

from pages.dynamic_loading import DynamicLoading
from pages.main_page import MainPage
from pages.challenging_dom import ChallengingDom
from utils.constans.enums import ScreenSize


@pytest.mark.parametrize("driver", [ScreenSize.DESKTOP], indirect=True)
def test_print_frames_name(driver, config):
    login_page = MainPage(driver, config)
    login_page.visit_page()
    frames_page = login_page.frames_click()
    nested_frame_page = frames_page.nested_frames_click()

    print(nested_frame_page.get_middle_frame_text())
    print(nested_frame_page.get_bottom_frame_text())
    print(nested_frame_page.get_left_frame_text())
    print(nested_frame_page.get_right_frame_text())


@pytest.mark.parametrize("driver", [ScreenSize.DESKTOP], indirect=True)
def test_wait_until_loaded(driver, config):
    dynamic_loading = DynamicLoading(driver, config)
    dynamic_loading.visit(1)
    dynamic_loading.start_button_click()
    dynamic_loading.wait_until_loading()
    print(dynamic_loading.get_finish_text())


@pytest.mark.parametrize("driver", [ScreenSize.DESKTOP], indirect=True)
def test_deal_with_table(driver, config):
    challenging_dom = ChallengingDom(driver, config)
    challenging_dom.visit()
    highlight_cell = (2, 5)
    challenging_dom.set_highlight_cell(*highlight_cell)
    time.sleep(2)
    challenging_dom.delete_highlight_cell(*highlight_cell)

    highlight_delete_link = 'Apeirian7'
    challenging_dom.set_highlight_delete_link_by_cell_name(highlight_delete_link)
    time.sleep(2)
    challenging_dom.delete_highlight_delete_link_by_cell_name(highlight_delete_link)

    highlight_edit_link = 'Apeirian2'
    challenging_dom.set_highlight_edit_link_by_cell_name(highlight_edit_link)
    time.sleep(2)
    challenging_dom.delete_highlight_edit_link_by_cell_name(highlight_edit_link)

    cell_name_1 = 'Definiebas7'
    challenging_dom.set_highlight_cell_by_name(cell_name_1)
    time.sleep(2)
    challenging_dom.delete_highlight_cell_by_name(cell_name_1)

    cell_name_2 = 'Iuvaret7'
    challenging_dom.set_highlight_cell_by_name(cell_name_2)
    time.sleep(2)
    challenging_dom.delete_highlight_cell_by_name(cell_name_2)

    time.sleep(4)