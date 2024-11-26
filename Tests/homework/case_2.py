import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from conftest import get_driver


class TestClick:
    def test_click(self, selenium):

        selenium.get('https://github.com/microsoft/vscode/issues')
        selenium.find_element(By.CSS_SELECTOR, '[aria-label="Filter by author"]').click()
        selenium.find_element(By.XPATH, '//*[contains(@class, "UnstyledTextInput-sc-14ypya-0 kbCLEG")]')\
            .send_keys('bpasero')
        time.sleep(10)
        selenium.find_element(By.XPATH, '//*[contains(@class, "UnstyledTextInput-sc-14ypya-0 kbCLEG")]')\
            .send_keys(Keys.ENTER)
        pass
