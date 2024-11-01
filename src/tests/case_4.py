from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from conftest import get_driver
import time

class TestSlider:
    def test_slider(self, get_driver):
        driver = get_driver
        driver.get('https://skillbox.ru/code/')
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR, '#employment').click()
        driver.find_element(By.CSS_SELECTOR, '[aria-label="Вернуться наверх страницы"]').click()
        #driver.find_element(By.XPATH, '(//label[contains(@value, "profession")])').click()
        """el = driver.find_element(By.XPATH, '//div[contains(@aria-valuetext, "1")]')
        action_chains = webdriver.ActionChains(driver)
        action_chains \
            .click_and_hold(el) \
            .move_by_offset(xoffset=5, yoffset=0) \
            .perform()
        action_chains.release().perform()"""
        """el = driver.find_element(By.XPATH, '//div[contains(@aria-valuetext, "24")]')
        action_chains = webdriver.ActionChains(driver)
        action_chains \
            .click_and_hold(el) \
            .move_by_offset(xoffset=-12, yoffset=0) \
            .perform()
        action_chains.release().perform()"""
        #driver.find_element(By.XPATH, '(//span[contains(text(), "Android")]/ancestor::label)').click()
        pass


