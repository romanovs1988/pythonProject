import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

class TestClick:
    def test_click(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://github.com/microsoft/vscode/issues')
        driver.find_element(By.XPATH, '//button[@id=":r3h:"]').click()
        driver.find_element(By.XPATH, '//*[contains(@class, "UnstyledTextInput-sc-14ypya-0 kbCLEG")]').send_keys('bpasero')
        driver.find_element(By.CSS_SELECTOR, '#__primer_id_10021').click()
        pass



