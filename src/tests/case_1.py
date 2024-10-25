import time

from requests import request
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from conftest import get_driver


class TestInput:
    def test_input_filter(self, get_driver):
        driver = get_driver
        driver.get('https://github.com/microsoft/vscode/issues')
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR, '[data-target="qbsearch-input.inputButton"]').send_keys('in:title')

        #value = 'in:title'
        #for el in value:
            #time.sleep(0.2)


        driver.find_element(By.CSS_SELECTOR, '[data-target="qbsearch-input.inputButton"]').send_keys('bug' + Keys.ENTER)
        time.sleep(5)

        pass