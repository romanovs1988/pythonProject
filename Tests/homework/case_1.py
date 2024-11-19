import time
from telnetlib import EC

from requests import request
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from conftest import get_driver


class TestInput:
    def test_input_filter(self, selenium):

        selenium.get('https://github.com/microsoft/vscode/issues')
        time.sleep(5)
        selenium.find_element(By.CSS_SELECTOR, '#repository-input').send_keys('in:title')
        time.sleep(5)
        selenium.find_element(By.CSS_SELECTOR, '#repository-input').send_keys(' bug' + Keys.ENTER)
        time.sleep(5)
        pass
