import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestCharts:

    def test_tooltip(self, selenium):
        selenium.get('https://6uvr8r.csb.app/demo/TooltipDemo.html')
        el = selenium.find_element(By.XPATH, '//button/span[contain(text(), "Save")]')
        action_chains = webdriver.ActionChains(selenium)
        action_chains.move_to_element(el).perform()
        selenium.find_element(By.XPATH, '//span[contains(@class, "plus")]/parent::button').click()
        selenium.find_element(By.XPATH, '//span[contains(@class, "plus")]/parent::button').click()
        pass

    def test_pie(self, selenium):

        selenium.get('https://no1n471n5j.csb.app/')
        action_chains = webdriver.ActionChains(selenium)
        time.sleep(13)
        action_chains.move_to_element(selenium.find_element(By.CSS_SELECTOR, '.highcharts-point.highcharts-color-2'))\
            .perform()
        pass

    def test_table(self, selenium):

        selenium.get('https://rz7b08.csb.app/demo/DataTableDemo.html')
        selenium.find_element(By.CSS_SELECTOR, '[placeholder="Keyword Search"]').send_keys('Egypt')
        selenium.find_element(By.XPATH, '//td[contains(text(), "Simona")]\
        /preceding-sibling::td/descendant::div[@role="checkbox"]').click()
        selenium.find_element(By.XPATH, '//span[contains(text(), "Name")]').click()
        pass
