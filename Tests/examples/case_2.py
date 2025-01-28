import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class TestClick:
    def test_click(self, get_driver):

        get_driver.get('https://github.com/microsoft/vscode/issues')
        get_driver.find_element(By.CSS_SELECTOR, '[aria-label="Filter by author"]').click()
        get_driver.find_element(By.XPATH, '//*[contains(@class, "UnstyledTextInput-sc-14ypya-0 kbCLEG")]')\
            .send_keys('bpasero')
        time.sleep(10)
        get_driver.find_element(By.XPATH, '//*[contains(@class, "UnstyledTextInput-sc-14ypya-0 kbCLEG")]')\
            .send_keys(Keys.ENTER)
        pass
