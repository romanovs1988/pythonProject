from telnetlib import EC

from selenium.webdriver.support import wait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.expected_conditions import element_attribute_to_include
from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import Keys
from conftest import get_driver
from selenium import webdriver

class TestValidate:
    def test_1(self, get_driver):
        driver = get_driver
        expected_value = ' bug' or ' Bug'

        driver.get('https://github.com/microsoft/vscode/issues')
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR, '#repository-input').send_keys('in:title')
        time.sleep(5)
        field = driver.find_element(By.CSS_SELECTOR, '#repository-input')
        field.send_keys(expected_value + Keys.ENTER)
        time.sleep(5)
        assert field.get_attribute('value') == ' bug' or ' Bug'
        pass

    def test_2(self, get_driver):
        driver = get_driver
        expected_value = 'bpasero'
        driver.get('https://github.com/microsoft/vscode/issues')
        driver.find_element(By.CSS_SELECTOR, '[aria-label="Filter by author"]').click()
        field = driver.find_element(By.XPATH, '//*[contains(@class, "UnstyledTextInput-sc-14ypya-0 kbCLEG")]')
        field.send_keys(expected_value + Keys.ENTER)
        assert field.get_attribute('value') == 'bpasero'

        #time.sleep(10)
        #driver.find_element(By.XPATH, '//*[contains(@class, "UnstyledTextInput-sc-14ypya-0 kbCLEG")]').send_keys(Keys.ENTER)

        pass

    def test_3(self, get_driver):
        driver = get_driver
        driver.get('https://github.com/search/advanced')
        expected_value = '>20000'
        time.sleep(5)
        driver.find_element(By.CSS_SELECTOR, '[value="Python"]').click()
        time.sleep(5)
        field = driver.find_element(By.CSS_SELECTOR, '#search_stars')
        field.send_keys(expected_value)
        assert field.get_attribute('value') == '>20000'

        driver.find_element(By.CSS_SELECTOR, '#search_filename').send_keys('environment.yml')

        #driver.find_element(By.XPATH, '//div[contains(@class, "form-group flattened")]/descendant::button').click()
        pass


    def test_4(self, get_driver):
        driver = get_driver
        driver.get('https://skillbox.ru/code/')

        radio = driver.find_element(By.XPATH, '(//*[contains(@class, "ui-radio-field__value ui-radio-field__value--small")])[2]').click()
        slider_1 = driver.find_element(By.XPATH, '(//*[contains(@class, "ui-range__dot")])[1]')
        action_chains = webdriver.ActionChains(driver)
        action_chains.click_and_hold(slider_1).move_by_offset(100, 0).perform()
        slider_2 = driver.find_element(By.XPATH, '(//*[contains(@class, "ui-range__dot")])[2]')
        action_chains = webdriver.ActionChains(driver)
        action_chains.click_and_hold(slider_2).move_by_offset(100, 0).perform()
        fullbox = driver.find_element(By.XPATH, '//*[@id="#app"]/main/div[1]/div[2]/div/div[1]/div[1]/div[6]/button').click()
        checkbox = driver.find_element(By.XPATH, '(//*[contains(@class, "filter-checkboxes-list__value")])[28]')
        checkbox.click()

        assert checkbox.is_selected() is True
        pass




    def test_5(self, get_driver):
        driver = get_driver
        driver.get('https://github.com/microsoft/vscode/graphs/commit-activity')
        action_chains = webdriver.ActionChains(driver)
        time.sleep(5)

        action_chains.move_to_element(driver.find_element(By.ID, 'commit-activity-master')).perform()
        action_chains.move_by_offset(-100, 0).perform()
        #wait.until(EC.visibility_of_element_located(By.CSS_SELECTOR, '[y="0"]'))
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[transform="translate(280, 0)"]')))

       # assert bar.is_selected() is True
        pass







