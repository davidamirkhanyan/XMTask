import pytest
from PageModels.MutantPage import MutantPage
from Utilities.date_time_utils import return_next_week, return_current_week, return_today, return_current_month, \
    return_next_month, return_tomorrow


# ######################## EXPECTED RESULTS #########################
expected_home_page_title = 'Forex & CFD Trading on Stocks, Indices, Oil, Gold by XM™'
expected_calendar_page_title = 'Real-Time Economic Calendar - provided by XM'
# ###################################################################


@pytest.mark.usefixtures("set_up")
class TestEconomicCalendar:
    
    def test_navigate_to_economic_calendar(self):
        ui = MutantPage(self.driver)
        ui.home.accept_all_cookies()
        actual_home_page_title = ui.home.return_page_title()
        ui.home.choose_navigation_item('research')
        ui.home.choose_research_dropdown_item('Economic Calendar')
        actual_calendar_page_title = ui.home.return_page_title()
        assert actual_home_page_title == expected_home_page_title, "Home Page Title Violation."
        assert actual_calendar_page_title == expected_calendar_page_title, "Calendar Page Title Violation."
        
    def test_calendar_slider_today(self):
        ui = MutantPage(self.driver)
        events_before = ui.economic_calendar.return_event_names()
        ui.economic_calendar.handle_calendar_slider('today')
        today_events = ui.economic_calendar.return_event_names()
        today_selected = ui.economic_calendar.return_selected_dates()
        expected_today = return_today()
        assert today_events != events_before, "Event List Violation After Slider's Today Update."
        assert today_selected == expected_today, "Calendar's Today's Selection Violation."
        
    def test_calendar_slider_tomorrow(self):
        ui = MutantPage(self.driver)
        events_before = ui.economic_calendar.return_event_names()
        ui.economic_calendar.handle_calendar_slider('tomorrow')
        tomorrow_events = ui.economic_calendar.return_event_names()
        tomorrow_selected = ui.economic_calendar.return_selected_dates()
        expected_tomorrow = return_tomorrow()
        assert tomorrow_events != events_before, "Event List Violation After Slider's Today Update."
        assert tomorrow_selected == expected_tomorrow, "Calendar's Today's Selection Violation."
        
    def test_calendar_slider_this_week(self):
        ui = MutantPage(self.driver)
        events_before = ui.economic_calendar.return_event_names()
        ui.economic_calendar.handle_calendar_slider('this week')
        this_week_events = ui.economic_calendar.return_event_names()
        this_week_selected = ui.economic_calendar.return_selected_dates()
        expected_this_week = return_current_week()
        assert this_week_events != events_before, "Event List Violation After Slider's This Week Update."
        assert this_week_selected == expected_this_week, "Calendar's This Week's Selection Violation."
        
    def test_calendar_slider_next_week(self):
        ui = MutantPage(self.driver)
        events_before = ui.economic_calendar.return_event_names()
        ui.economic_calendar.handle_calendar_slider('next week')
        next_week_events = ui.economic_calendar.return_event_names()
        next_week_selected = ui.economic_calendar.return_selected_dates()
        expected_next_week = return_next_week()
        assert next_week_events != events_before, "Event List Violation After Slider's Next Week Update."
        assert next_week_selected == expected_next_week, "Calendar's Next Week's Selection Violation."
        
    def test_calendar_slider_this_month(self):
        ui = MutantPage(self.driver)
        events_before = ui.economic_calendar.return_event_names()
        ui.economic_calendar.handle_calendar_slider('this month')
        this_month_events = ui.economic_calendar.return_event_names()
        this_month_selected = ui.economic_calendar.return_selected_dates()
        expected_this_month = return_current_month()
        assert this_month_events != events_before, "Event List Violation After Slider's This Month Update."
        assert this_month_selected == expected_this_month, "Calendar's This Month's Selection Violation."
        
    def test_calendar_slider_next_month(self):
        ui = MutantPage(self.driver)
        events_before = ui.economic_calendar.return_event_names()
        ui.economic_calendar.handle_calendar_slider('next month')
        next_month_events = ui.economic_calendar.return_event_names()
        next_month_selected = ui.economic_calendar.return_selected_dates()
        expected_next_month = return_next_month()
        assert next_month_events != events_before, "Event List Violation After Slider's Next Month Update."
        assert next_month_selected == expected_next_month, "Calendar's Next Month's Selection Violation."
        
    
