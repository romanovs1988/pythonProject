import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

class TestInput:
    def test_input_filter(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://github.com/microsoft/vscode/issues')
        el = driver.find_element(By.CSS_SELECTOR, '#query-builder-test').send_keys('in:title')
        driver.find_element(By.XPATH, '(//input[@id="query-builder-test"])').send_keys('bug' + Keys.ENTER)
        pass