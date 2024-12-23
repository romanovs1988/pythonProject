import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestCharts:
    def test_tool_bar(self, get_driver):

        get_driver.get('https://github.com/microsoft/vscode/graphs/commit-activity')
        action_chains = webdriver.ActionChains(get_driver)
        time.sleep(13)
        action_chains.move_to_element(get_driver.find_element(By.CSS_SELECTOR, '[y="0"]')).perform()
        pass
