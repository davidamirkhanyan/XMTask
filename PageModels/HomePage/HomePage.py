import time

from selenium.webdriver.common.keys import Keys
from PageModels.BasePage import BasePage
from PageModels.HomePage.HomePageSelectors import *
from PageModels.EconomicCaldendarPage.EconomicCalendarPageSelectors import *
from selenium.webdriver.common.action_chains import ActionChains


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    def accept_all_cookies(self):
        self.click_on(accept_all_cookies_button)
        time.sleep(0.5)
        return 1
    
    def choose_navigation_item(self, item: str):
        """
        :param item: Can be one of [home, trading, platforms, research, promotions, about, partners]
        """
        selector = (flexible_navigation[0], flexible_navigation[1].format(item))
        self.click_on(selector)
        return 1
    
    def choose_research_dropdown_item(self, item: str):
        """
        :param item:
            Research Items: [Markets Overview, Discover, XM Research, Trade Ideas, Technical Summaries,
                             Economic Calendar, XM TV, Podcast]
            Learning Center: [XM Live, Live Education, Live Education Schedule, Educational Videos,
                              Forex & CFDs Webinars, Platform Tutorials, Forex & CFDs Seminars]
            Tools: [Trading Tools, MQL5, Forex Calculators]
        """
        selector = (research_dropdown_handler[0], research_dropdown_handler[1].format(item))
        self.click_on(selector)
        self.wait_page_fully_loaded()
        return 1