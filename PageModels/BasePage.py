from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.short_wait = WebDriverWait(driver, 5)
        self.long_wait = WebDriverWait(driver, 15)
    
    def return_element(self, locator: tuple):
        element = self.long_wait.until(EC.visibility_of_element_located(locator))
        return element
    
    def wait_element_to_be_loaded(self, locator: tuple):
        element = self.long_wait.until(EC.presence_of_element_located(locator))
        return element
    
    def click_on(self, locator: tuple):
        self.short_wait.until(EC.visibility_of_element_located(locator)).click()
        return 1
    
    def clear_input(self, locator: tuple):
        self.short_wait.until(EC.visibility_of_element_located(locator)).clear()
        return 1
    
    def write_in(self, locator: tuple, text):
        self.short_wait.until(EC.visibility_of_element_located(locator)).send_keys(text)
        return 1
    
    def get_element_text(self, locator: tuple):
        element = self.short_wait.until(EC.visibility_of_element_located(locator))
        return element.text
    
    def get_attribute_value(self, locator: tuple, attr):
        element = self.short_wait.until(EC.visibility_of_element_located(locator))
        if attr == 'text':
            return element.text
        value = element.get_attribute(attr)
        return value
    
    def wait_page_fully_loaded(self):
        self.long_wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        return 1
    
    def return_elements(self, locator):
        elements = self.driver.find_elements(*locator)
        return elements
    
    def return_page_title(self):
        title = self.driver.title
        return title
    
    def wait_element_to_be_invisible(self, locator):
        flag = True
        while flag:
            flag = self.return_elements(locator)
        return 1
    