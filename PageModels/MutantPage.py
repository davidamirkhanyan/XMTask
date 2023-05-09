from PageModels.HomePage.HomePage import HomePage
from PageModels.EconomicCaldendarPage.EconomicCalendarPage import EconomicCalendar


class MutantPage:
    def __init__(self, driver):
        self.home = HomePage(driver)
        self.economic_calendar = EconomicCalendar(driver)
        