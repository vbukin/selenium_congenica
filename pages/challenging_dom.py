from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ChallengingDom(BasePage):
    def __init__(self, driver, config):
        self.driver = driver
        self.config = config
        self.path = 'challenging_dom'
        super().__init__(driver, config)

    def visit(self):
        self.visit_page(self.path)

    def get_rows(self):
        return self.find_elements('tbody tr')

    def get_row_by_diceret(self, diceret):
        rows = self.get_rows()

        result = None
        for row in rows:
            cells = row.find_elements(By.CSS_SELECTOR, 'td')
            if cells and cells[5].text == diceret:
                result = row
                break

        return result

    def get_cell(self, row_index, column_index):
        row = self.get_rows()[row_index]
        return row.find_elements(By.CSS_SELECTOR, 'td')[column_index]

    def set_highlight_cell(self, row_index, column_index):
        element = self.get_cell(row_index, column_index)
        self.set_background_color(element, 'yellow')

    def delete_highlight_cell(self, row_index, column_index):
        element = self.get_cell(row_index, column_index)
        self.set_background_color(element)

    def get_row_by_name(self, name):
        rows = self.get_rows()

        result = None
        for row in rows:
            cells = row.find_elements(By.CSS_SELECTOR, 'td')
            for cell in cells:
                if cell.text == name:
                    result = row
                    break

        return result

    def get_cell_by_name(self, name):
        rows = self.get_rows()

        for row in rows:
            cells = row.find_elements(By.CSS_SELECTOR, 'td')
            for cell in cells:
                if cell.text == name:
                    return cell

        return False

    def set_highlight_delete_link_by_cell_name(self, value):
        delete_action = self.get_delete_link_in_row(value)
        self.set_background_color(delete_action, 'yellow')

    def delete_highlight_delete_link_by_cell_name(self, value):
        delete_action = self.get_delete_link_in_row(value)
        self.set_background_color(delete_action)

    def set_highlight_edit_link_by_cell_name(self, value):
        edit_action = self.get_edit_link_in_row(value)
        self.set_background_color(edit_action, 'yellow')

    def delete_highlight_edit_link_by_cell_name(self, value):
        edit_action = self.get_edit_link_in_row(value)
        self.set_background_color(edit_action)

    def set_highlight_cell_by_name(self, value):
        cell = self.get_cell_by_name(value)
        self.set_background_color(cell, 'yellow')

    def delete_highlight_cell_by_name(self, value):
        cell = self.get_cell_by_name(value)
        self.set_background_color(cell)

    def get_delete_link_in_row(self, element):
        actions = self.get_row_by_name(element).find_elements(By.CSS_SELECTOR, 'td')[-1]
        return actions.find_elements(By.CSS_SELECTOR, 'a')[1]

    def get_edit_link_in_row(self, element):
        actions = self.get_row_by_name(element).find_elements(By.CSS_SELECTOR, 'td')[-1]
        return actions.find_elements(By.CSS_SELECTOR, 'a')[0]