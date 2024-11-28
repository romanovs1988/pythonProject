import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


import logging.config
from os import path

lof_file_path = path.join(path.dirname(path.abspath(__file__)), 'logging.ini')
logging.config.fileConfig(lof_file_path)

pytest_plugins = [
    "src.fixtures"
]


def pytest_addoption(parser):
    parser.addini("get_driver_url", "Get_driver Hub url")
    parser.addini("browser_name", "Browser name for tests")
    parser.addini("browser_version", "Browser version for tests")
    parser.addini("headless", "Run browser in headless mode")


"""@pytest.fixture(autouse=True)
def get_driver(request):
    service = Service(executable_path=ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    request.cls.driver = driver
    yield driver
    driver.quit()"""
