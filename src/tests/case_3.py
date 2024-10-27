import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from conftest import get_driver

class TestClick:
    def test_button_dropdown(self, get_driver):
        driver = get_driver
        driver.get('https://github.com/search/advanced')
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR, '[value="Python"]').click()
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR, '#search_stars').send_keys('>20000')
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR, '#search_filename').send_keys('environment.yml')
        time.sleep(5)

        driver.find_element(By.XPATH, '//div[contains(@class, "d-flex d-md-block flex-shrink-0 pt-2 pt-md-0")]/child::button').click()
        #time.sleep(5)

        #action_chains = webdriver.ActionChains(driver)
        #time.sleep(13)
        #action_chains.move_to_element(driver.find_element(By.XPATH, '//div[contains(@class, "d-flex d-md-block flex-shrink-0 pt-2 pt-md-0")]/child::button')).perform()

        pass




