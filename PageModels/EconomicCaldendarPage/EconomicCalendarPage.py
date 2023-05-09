import time

from selenium.webdriver.common.keys import Keys
from PageModels.BasePage import BasePage
from PageModels.EconomicCaldendarPage.EconomicCalendarPageSelectors import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


def use_calendar_iframe(func):
    def wrapper(self, *args, **kwargs):
        iframe = self.wait_element_to_be_loaded(calendar_iframe)
        self.driver.switch_to.frame(iframe)
        result = func(self, *args, **kwargs)
        self.driver.switch_to.default_content()
        return result
    return wrapper


class EconomicCalendar(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    @use_calendar_iframe
    def handle_calendar_slider(self, mode: str):
        actions = ActionChains(self.driver)
        self.wait_element_to_be_loaded(event_row)
        """
        :param mode: [recent, today, tomorrow, this week, next week, this month, next month]
        """
        numeric_values = {'recent': 0, 'today': 1, 'tomorrow': 2, 'this week': 3, 'next week': 4, 'this month': 5,
                          'next month': 6}
        current_position = int(self.get_attribute_value(slider, 'aria-valuenow'))
        difference = numeric_values[mode] - current_position
        iterations = abs(difference)
        if difference < 0:
            direction = Keys.LEFT
        else:
            direction = Keys.RIGHT
        self.click_on(slider_thumb)
        while iterations:
            actions.send_keys(direction).perform()
            iterations -= 1
        return 1
    
    @use_calendar_iframe
    def return_calendar_events_count(self):
        overall_event_rows = self.return_elements(event_row)
        event_count_actual = self.get_element_text(event_count)
        return event_count_actual, len(overall_event_rows)
    
    @use_calendar_iframe
    def return_selected_dates(self):
        selected = self.return_elements(selected_dates)
        dates = [elem.get_attribute('aria-label') for elem in selected]
        return dates
    
    @use_calendar_iframe
    def return_event_names(self):
        self.wait_element_to_be_loaded(event_row)
        events = self.return_elements(event_name)
        names = [elem.text for elem in events]
        return names
        
        
        
        
        

