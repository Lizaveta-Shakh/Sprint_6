import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions


@pytest.fixture(scope="function")
def driver():
    options = FirefoxOptions()

    driver = webdriver.Firefox(options=options)
    yield driver
    driver.quit()