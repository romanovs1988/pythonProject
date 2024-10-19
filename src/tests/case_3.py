import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from conftest import get_driver

class TestClick:
    def test_button_dropdown(self, get_driver):
        driver = get_driver
        driver.get('https://github.com/search/advanced')

        driver.find_element(By.CSS_SELECTOR, '[value="Python"]').click()
        driver.find_element(By.CSS_SELECTOR, '#search_stars').send_keys('>20000')
        driver.find_element(By.CSS_SELECTOR, '#search_filename').send_keys('environment.yml')

        driver.find_element(By.XPATH, '(//*[@class="btn flex-auto"])[2] ').click()
        pass




