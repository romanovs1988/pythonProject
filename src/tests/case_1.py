import time
from telnetlib import EC

from requests import request
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from conftest import get_driver


class TestInput:
    def test_input_filter(self, get_driver):
        driver = get_driver
        driver.get('https://github.com/microsoft/vscode/issues')
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR, '#repository-input').send_keys('in:title')
        #WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#qb-input-query'))).send_keys('in:title')
        #value = 'in:title'
        #for el in value:
            #time.sleep(0.2)
        time.sleep(5)


        driver.find_element(By.CSS_SELECTOR, '#repository-input').send_keys(' bug' + Keys.ENTER)
        time.sleep(5)

        pass