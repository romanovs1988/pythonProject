import logging
import pytest
from selenium import webdriver
from selenium.webdriver import Remote
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def selenium(pytestconfig):
    service = Service(executable_path=ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    browser_name = pytestconfig.getini("browser_name")
    logging.info(f'Prepare {browser_name} browser...')
    if pytestconfig.getini("headless") == 'True' and browser_name == "chrome":
        options.add_argument("--headless")
    driver = webdriver.Chrome(service=service, options=options)
    pytestconfig.cls.driver = driver
    options.page_load_strategy = 'normal'
    driver = Remote(
        desired_capabilities={
            "browserName": pytestconfig.getini("browser_name"),
            "browserVersion": pytestconfig.getini("browser_version")
        },
        command_executor=pytestconfig.getini("selenium_url"),
        options=options
    )
    logging.info(f'Browser {browser_name} has been started...')
    yield driver
    driver.quit()
