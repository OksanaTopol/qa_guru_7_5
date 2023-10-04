import pytest
import os

from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


from utils import attach

PROJECT_ROOT_PATH = os.path.dirname(__file__)
print(PROJECT_ROOT_PATH)
RESOURCE_PATH = os.path.abspath(os.path.join(PROJECT_ROOT_PATH, 'resources'))

@pytest.fixture(scope="function", autouse=True)
def setup_browser():

    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = 1920
    browser.config.window_height = 1028


    yield


    browser.quit()
