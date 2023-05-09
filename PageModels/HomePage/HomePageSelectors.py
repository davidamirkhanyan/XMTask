from selenium.webdriver.common.by import By

flexible_navigation = (By.CLASS_NAME, 'main_nav_{0}')
accept_all_cookies_button = (By.XPATH, '//button[text() = "ACCEPT ALL"]')
research_dropdown_handler = (By.XPATH, "//li/a[normalize-space(text())='{0}']")
cookie_modal = (By.ID, 'cookieModal')
