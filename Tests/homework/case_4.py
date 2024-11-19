from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from conftest import get_driver
import time


class TestSlider:
    def test_slider(self, selenium):

        selenium.get('https://skillbox.ru/code/')

        radio = selenium.find_element(By.XPATH, '(//*[contains(@class, "ui-radio-field__value ui-radio-field__value--small")])[2]').click()
        slider_1 = selenium.find_element(By.XPATH, '(//*[contains(@class, "ui-range__dot")])[1]')
        action_chains = webdriver.ActionChains(selenium)
        action_chains.click_and_hold(slider_1).move_by_offset(100, 0).perform()
        slider_2 = selenium.find_element(By.XPATH, '(//*[contains(@class, "ui-range__dot")])[2]')
        action_chains = webdriver.ActionChains(selenium)
        action_chains.click_and_hold(slider_2).move_by_offset(100, 0).perform()
        fullbox = selenium.find_element(By.XPATH, '//*[@id="#app"]/main/div[1]/div[2]/div/div[1]/div[1]/div[6]/button').click()
        checkbox = selenium.find_element(By.XPATH, '(//*[contains(@class, "filter-checkboxes-list__value")])[28]').click()
        pass

