import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class TestInput:
    def test_input_filter(self, get_driver):

        get_driver.get('https://github.com/microsoft/vscode/issues')
        time.sleep(5)
        get_driver.find_element(By.CSS_SELECTOR, '#repository-input').send_keys('in:title')
        time.sleep(5)
        get_driver.find_element(By.CSS_SELECTOR, '#repository-input').send_keys(' bug' + Keys.ENTER)
        time.sleep(5)
        pass
