import time

import allure
from selenium import webdriver
from playwright.sync_api import expect
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import wait


class Python:
    pass


@allure.feature('Full Accounts')
@allure.story('Waiting page load')
class TestValidate:
    @allure.title('Проверка загрузки страницы')
    def test_1(self, page):

        with allure.step('Открытие страницы https://github.com/microsoft/vscode/issues'):
            page.goto('https://github.com/microsoft/vscode/issues')
            #time.sleep(5)
        with allure.step('Заполнение формы данными'):
            page.fill('#repository-input', "in:title bug or Bug") #('#repository-input', "in:title") ('#repository-input').send_keys('in:title')
            #time.sleep(5)
        with allure.step('Клик по кнопке ENTER'):
            page.press('#repository-input', "Enter")
        pass

    def test_2(self, page):

        expected_value = 'bpasero'
        with allure.step('Переход на страницу https://github.com/microsoft/vscode/issues'):
            page.goto('https://github.com/microsoft/vscode/issues')
        with allure.step('Клик по найденному элементу'):
            page.click('[aria-label="Filter by author"]')
            # wait for 1 second
            #page.wait_for_timeout(3000)
        with allure.step('Заполнение формы данными'):
            page.fill('//*[contains(@class, "UnstyledTextInput__ToggledUnstyledTextInput-sc-14ypya-0 jkNcAv")]', "bpasero")
            page.wait_for_timeout(3000)
        with allure.step('Клик по кнопке ENTER'):
            page.press('//*[contains(@class, "UnstyledTextInput__ToggledUnstyledTextInput-sc-14ypya-0 jkNcAv")]', "Enter")
       #expect(page.locator('//input[@id="repository-input"]')).to_contain_text('bpasero')
       # assert expected_value.evaluate("node => node.innerText") == "bpasero"
       # locator = page.locator('//input[@id="repository-input"]')
       # expect(locator).to_have_attribute("type", "bpasero")
        pass

    def test_3(self, page):

        with allure.step('Переход на страницу https://github.com/search/advanced'):
            page.goto('https://github.com/search/advanced')
        expected_value = '>20000'
        #time.sleep(5)
        with allure.step('Клик по найденному элементу'):
            #page.click('[value="Python"]')
            page.click('//select[@id="search_language"]')
            page.wait_for_timeout(3000)
            for i in range(19):
                page.keyboard.press("ArrowDown")
            page.wait_for_timeout(3000)
            page.keyboard.press("Enter")
            #page.click('//*[@id="search_language"]/optgroup[1]/option[19]')

        with allure.step('Заполнение формы данными'):
            page.fill('#search_stars', ">20000")
            # field.send_keys(expected_value)
        #assert field.get_attribute('value') == '>20000'
        with allure.step('Заполнение формы данными'):
            page.fill('#search_filename', "environment.yml")
        # driver.find_element(By.XPATH, '//div[contains(@class, "form-group flattened")]/descendant::button').click()
        with allure.step('Нажать "Поиск"'):
            page.click('//div[contains(@class, "form-group flattened")]/descendant::button')
        pass

    def test_4(self, page, go_to_url):

        with allure.step('Переход на страницу https://skillbox.ru/code/'):
            go_to_url('https://skillbox.ru/code/')
        with allure.step('Клик по найденному элементу'):
            page.click('(//*[contains\
            (@class, "ui-radio-field__value ui-radio-field__value--small")])[2]')
            page.wait_for_timeout(3000)
        with allure.step('Переместить slider_1'):
            page.drag_and_drop('//*[contains(@aria-valuetext, "1")]', '//*[contains(@aria-valuetext, "6")]')
            page.wait_for_timeout(3000)
        with allure.step('Переместить slider_2'):
            page.drag_and_drop('//*[contains(@aria-valuetext, "24")]', '//*[contains(@aria-valuetext, "12")]')
        with allure.step('Клик по найденному элементу'):
            page.click('//*[@id="#app"]/main/div[1]/div[2]/div/div[1]/div[1]/div[6]/button')
        with allure.step('Клик по чекбоксу'):
            checkbox = page.click('(//*[contains(@class, "filter-checkboxes-list__value")])[28]')
        #assert checkbox is True
        pass

    def test_5(self, page):
        with allure.step('Переход на страницу https://github.com/microsoft/vscode/graphs/commit-activity'):
            page.goto('https://github.com/microsoft/vscode/graphs/commit-activity')

        with allure.step('Переместить курсор на выбранный элемент'):
            element = page.locator('//div[@class="svg-tip n"]')
            page.wait_for_timeout(1000)
            #element.wait_for('//div[@class="svg-tip n"]', "380 commits the week of Mar 17")
            #action_chains.move_to_element(get_driver.find_element(By.ID, 'commit-activity-master')).perform()
            #action_chains.move_by_offset(-100, 0).perform()
        with allure.step('Переместить курсор на выбранный элемент'):
            page.mouse.move(-100, 0)
            #tooltip = get_driver.find_element(By.XPATH, '//div[@class="svg-tip n"]')
        #tooltip_text = '380 commits the week of Mar 17'
        #assert tooltip_text in tooltip.text == '380 commits the week of Mar 17'
        #wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[transform="translate(280, 0)"]')))
        pass
