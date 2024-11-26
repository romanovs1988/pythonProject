import time
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from conftest import get_driver


class TestClick:
    def test_button_dropdown(self, selenium):

        selenium.get('https://github.com/search/advanced')
        time.sleep(5)
        selenium.find_element(By.CSS_SELECTOR, '[value="Python"]').click()
        time.sleep(5)
        selenium.find_element(By.CSS_SELECTOR, '#search_stars').send_keys('>20000')
        selenium.find_element(By.CSS_SELECTOR, '#search_filename').send_keys('environment.yml')
        selenium.find_element(By.XPATH, '//div[contains(@class, "form-group flattened")]/descendant::button').click()
        pass
