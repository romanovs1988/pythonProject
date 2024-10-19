import pytest
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(autouse=True)
def get_driver(request):
    service = Service(executable_path=ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    request.cls.driver = driver
    yield driver
    driver.quit()