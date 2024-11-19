import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from conftest import get_driver


class TestClick:
    def test_click(self, selenium):

        selenium.get('https://github.com/microsoft/vscode/issues')
        selenium.find_element(By.CSS_SELECTOR, '[aria-label="Filter by author"]').click()
        selenium.find_element(By.XPATH, '//*[contains(@class, "UnstyledTextInput-sc-14ypya-0 kbCLEG")]').send_keys('bpasero')
        # action_chains = webdriver.ActionChains(driver)
        time.sleep(10)
        # action_chains.move_to_element(driver.find_element(By.XPATH, '//*[contains(@class, "Group__StyledGroup-sc-1s2aw76-0 fSVUAg")]')).click()
        selenium.find_element(By.XPATH, '//*[contains(@class, "UnstyledTextInput-sc-14ypya-0 kbCLEG")]').send_keys(Keys.ENTER)
        pass


