import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

class TestClick:
    def test_button_dropdown(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://github.com/search/advanced')
        driver.find_element(By.CSS_SELECTOR, '#search_language').click()
        driver.find_element(By.CSS_SELECTOR, '[value="Python"]').click()
        el = driver.find_element(By.CSS_SELECTOR, '#search_stars').send_keys('>20000')
        el_2 = driver.find_element(By.CSS_SELECTOR, '#search_filename').send_keys('environment.yml')
        driver.find_element(By.XPATH, '(//*[@class="btn flex-auto"])[2] ').click()
        pass




