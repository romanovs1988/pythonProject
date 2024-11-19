import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from conftest import get_driver


class TestCharts:
    def test_tool_bar(self, selenium):

        selenium.get('https://github.com/microsoft/vscode/graphs/commit-activity')
        action_chains = webdriver.ActionChains(selenium)
        time.sleep(13)
        action_chains.move_to_element(selenium.find_element(By.CSS_SELECTOR, '[y="0"]')).perform()
        pass
