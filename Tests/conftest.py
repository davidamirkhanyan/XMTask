import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="Prod")
    parser.addoption("--browser", action="store", default="Chrome")
    parser.addoption("--headless", action="store", default="yes")


def pytest_configure(config):
    if config.getoption('env') == "Prod":
        url = "https://www.xm.com/"
    else:
        url = "https://www.xm.com/"  # Here can be stored Dev Environment URL
    os.environ['url'] = url
    os.environ['browser'] = config.getoption('browser')
    os.environ["headless"] = config.getoption('headless')


@pytest.fixture(scope="class")
def set_up(request):
    driver = None
    if os.environ['browser'] == "Chrome":
        options = webdriver.ChromeOptions()
        if os.environ["headless"] == 'yes':
            options.add_argument("--headless")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    elif os.environ['browser'] == "Firefox":
        options = webdriver.FirefoxOptions()
        if os.environ["headless"] == 'yes':
            options.headless = True
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
    driver.maximize_window()
    driver.get(os.environ['url'])
    request.cls.driver = driver
    yield driver
    driver.quit()
