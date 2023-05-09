from selenium.webdriver.common.by import By

calendar_iframe = (By.XPATH, "//div[contains(@class,'rp-trading-central-widget')]/iframe")
slider = (By.XPATH, '//mat-slider')
slider_thumb = (By.CLASS_NAME, 'mat-slider-thumb')
event_row = (By.TAG_NAME, 'tc-economic-calendar-row')
selected_dates = (By.XPATH, '//button[@aria-pressed="true"]')
event_name = (By.XPATH, "//*[@class='tc-calendar-event-detail-event']")

