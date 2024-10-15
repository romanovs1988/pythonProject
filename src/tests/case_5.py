import time

from selenium import webdriver
from selenium.webdriver.common.by import By

class TestCharts:
    def test_tool_bar(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://github.com/microsoft/vscode/graphs/commit-activity')
        action_chains = webdriver.ActionChains(driver)
        time.sleep(13)
        action_chains.move_to_element(driver.find_element(By.XPATH, '//*[@class="bar mini active"]')).perform()
        pass