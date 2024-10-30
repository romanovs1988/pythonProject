import time
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from conftest import get_driver

class TestClick:
    def test_button_dropdown(self, get_driver):
        driver = get_driver
        driver.get('https://github.com/search/advanced')
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR, '[value="Python"]').click()
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR, '#search_stars').send_keys('>1000')

        driver.find_element(By.CSS_SELECTOR, '#search_filename').send_keys('environment.yml')

        driver.find_element(By.XPATH, '//div[contains(@class, "form-group flattened")]/descendant::button').click()

        #time.sleep(5)
        #driver.find_element(By.XPATH, '//*[contains(@class, "form-control input-block search-page-input js-advanced-search-input js-advanced-search-prefix")]').send_keys(Keys.ENTER)
        #action_chains = webdriver.ActionChains(driver)
        #time.sleep(13)
        #action_chains.move_to_element(driver.find_element(By.XPATH, '//div[contains(@class, "d-flex d-md-block flex-shrink-0 pt-2 pt-md-0")]/child::button')).perform()

        pass




