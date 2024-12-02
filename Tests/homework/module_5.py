import time
import logging

import allure
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import wait

@allure.feature('Full Accounts')
@allure.story('Waiting page load')
class TestValidate:
    @allure.title('Проверка загрузки страницы')
    def test_1(self, get_driver, new_fixture):
        driver = get_driver
        expected_value = ' bug' or ' Bug'
        with allure.step('Открытие страницы https://github.com/microsoft/vscode/issues'):
            driver.get('https://github.com/microsoft/vscode/issues')
            time.sleep(5)
        with allure.step('Заполнение формы данными'):
            driver.find_element(By.CSS_SELECTOR, '#repository-input').send_keys('in:title')
            time.sleep(5)
        with allure.step('Клик по кнопке ENTER'):
            field = driver.find_element(By.CSS_SELECTOR, '#repository-input')
            field.send_keys(expected_value + Keys.ENTER)
            time.sleep(5)
        assert field.get_attribute('value') == ' bug' or ' Bug'
        pass

    def test_2(self, get_driver):

        expected_value = 'bpasero'
        with allure.step('Переход на страницу https://github.com/microsoft/vscode/issues'):
            get_driver.get('https://github.com/microsoft/vscode/issues')
        with allure.step('Клик по найденному элементу'):
            get_driver.find_element(By.CSS_SELECTOR, '[aria-label="Filter by author"]').click()
        with allure.step('Заполнение формы данными'):
            field = get_driver.find_element(By.XPATH, '//*[contains(@class, "UnstyledTextInput-sc-14ypya-0 kbCLEG")]')
            field.send_keys(expected_value + Keys.ENTER)
        assert field.get_attribute('value') == 'bpasero'

        pass

    def test_3(self, get_driver):

        with allure.step('Переход на страницу https://github.com/search/advanced'):
            get_driver.get('https://github.com/search/advanced')
        expected_value = '>20000'
        time.sleep(5)
        with allure.step('Клик по найденному элементу'):
            get_driver.find_element(By.CSS_SELECTOR, '[value="Python"]').click()
            time.sleep(5)
        with allure.step('Заполнение формы данными'):
            field = get_driver.find_element(By.CSS_SELECTOR, '#search_stars')
            field.send_keys(expected_value)
        assert field.get_attribute('value') == '>20000'
        with allure.step('Заполнение формы данными'):
            get_driver.find_element(By.CSS_SELECTOR, '#search_filename').send_keys('environment.yml')
        # driver.find_element(By.XPATH, '//div[contains(@class, "form-group flattened")]/descendant::button').click()
        pass

    def test_4(self, get_driver):

        with allure.step('Переход на страницу https://skillbox.ru/code/'):
            get_driver.get('https://skillbox.ru/code/')
        with allure.step('Клик по найденному элементу'):
            get_driver.find_element(By.XPATH, '(//*[contains\
            (@class, "ui-radio-field__value ui-radio-field__value--small")])[2]').click()
        with allure.step('Переместить slider_1'):
            slider_1 = get_driver.find_element(By.XPATH, '(//*[contains(@class, "ui-range__dot")])[1]')
            action_chains = webdriver.ActionChains(get_driver)
            action_chains.click_and_hold(slider_1).move_by_offset(100, 0).perform()
        with allure.step('Переместить slider_2'):
            slider_2 = get_driver.find_element(By.XPATH, '(//*[contains(@class, "ui-range__dot")])[2]')
            action_chains = webdriver.ActionChains(get_driver)
            action_chains.click_and_hold(slider_2).move_by_offset(100, 0).perform()
        with allure.step('Клик по найденному элементу'):
            get_driver.find_element(By.XPATH, '//*[@id="#app"]/main/div[1]/div[2]/div/div[1]/div[1]/div[6]/button').click()
        with allure.step('Клик по чекбоксу'):
            checkbox = get_driver.find_element(By.XPATH, '(//*[contains(@class, "filter-checkboxes-list__value")])[28]')
            checkbox.click()
        assert checkbox.is_selected() is True
        pass

    def test_5(self, get_driver):
        with allure.step('Переход на страницу https://github.com/microsoft/vscode/graphs/commit-activity'):
            get_driver.get('https://github.com/microsoft/vscode/graphs/commit-activity')
        action_chains = webdriver.ActionChains(get_driver)
        time.sleep(5)
        with allure.step('Переместить курсор на выбранный элемент'):
            action_chains.move_to_element(get_driver.find_element(By.ID, 'commit-activity-master')).perform()
            action_chains.move_by_offset(-100, 0).perform()
        with allure.step('Переместить курсор на выбранный элемент'):
            tooltip = get_driver.find_element(By.XPATH, '//div[@class="svg-tip n"]')
        tooltip_text = '380 commits the week of Mar 17'
        assert tooltip_text in tooltip.text == '380 commits the week of Mar 17'
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[transform="translate(280, 0)"]')))
        pass
