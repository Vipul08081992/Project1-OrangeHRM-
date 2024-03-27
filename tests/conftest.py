import time
from selenium import webdriver
import pytest
from resourses.constants.urls_portal import login_page_url
@pytest.fixture()
def open_website():
    driver = webdriver.Chrome()
    driver.get(login_page_url())
    driver.maximize_window()
    time.sleep(3)
    return driver
