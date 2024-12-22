import re
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
        with allure.step('Заполнение формы данными'):
            page.fill('#repository-input', "in:title bug or Bug")
        with allure.step('Клик по кнопке ENTER'):
            page.press('#repository-input', "Enter")
        with allure.step('Получите все названия задач.'):
            issue_titles = page.locator("a[data-hovercard-type='issue']").all_inner_texts()
        with allure.step('Проверьте, что каждая из задач содержит в названии слово "bug".'):
            for title in issue_titles:
                assert "bug" in title.lower(), f"'{title}' не содержит слово 'bug'"
        pass

    def test_2(self, page):
        with allure.step('Переход на страницу https://github.com/microsoft/vscode/issues'):
            page.goto('https://github.com/microsoft/vscode/issues')
        with allure.step('Клик по найденному элементу'):
            page.click('[aria-label="Filter by author"]')
        with allure.step('Заполнение формы данными'):
            page.fill('//*[contains(@class, "UnstyledTextInput__ToggledUnstyledTextInput-sc-14ypya-0 jkNcAv")]', "bpasero")
            page.wait_for_timeout(3000)
        with allure.step('Клик по кнопке ENTER'):
            page.press('//*[contains(@class, "UnstyledTextInput__ToggledUnstyledTextInput-sc-14ypya-0 jkNcAv")]', "Enter")
        with allure.step('Получите все задачи'):
            issue_authors = page.locator("a[data-hovercard-type='user']").all_inner_texts()
        with allure.step('Проверьте, что автор всех задач введён в поиск ("bpasero").'):
            for author in issue_authors:
                assert author.lower() == "bpasero", f"Автор '{author}' не совпадает с 'bpasero'"
        pass

    def test_3(self, page):

        with allure.step('Переход на страницу Advanced search на GitHub.'):
            page.goto('https://github.com/search/advanced')
        with allure.step('В поле языка, на котором написан код, выберите Python.'):
            language_selector = page.locator('//select[@id="search_language"]')
            language_selector.select_option("Python")

        with allure.step('В поле количества звёзд у репозитория выберите >20000.'):
            page.fill('#search_stars', ">20000")

        with allure.step('В поле с названием файла выберите environment.yml.'):
            page.fill('#search_filename', "environment.yml")

        with allure.step('Нажать "Поиск"'):
            page.click('//div[contains(@class, "form-group flattened")]/descendant::button')
        with allure.step('Соберите информацию по всем репозиториям.'):
            repo_list = page.locator("ul.repo-list li").all_inner_texts()
        with allure.step('Проверьте, что в списке отображаются репозитории с количеством звёзд >20000.'):
            for repo in repo_list:
                if " " in repo:
                    parts = repo.split(" ")
                    stars = parts[0]
                    stars_count = int(stars[:-1]) * (1000 if stars.endswith('k') else 1)
                    assert stars_count > 20000, f"Репозиторий '{repo}' имеет звёзд: {stars_count}"
        pass

    def test_4(self, page, go_to_url):

        with allure.step('Перейдите на сайт Skillbox'):
            go_to_url('https://skillbox.ru/code/')
        with allure.step('Выбор радиокнопки "Профессия" в разделе "Тип обучения на платформе"'):
            page.click('(//*[contains\
            (@class, "ui-radio-field__value ui-radio-field__value--small")])[2]')
            page.wait_for_timeout(3000)
        with allure.step('Переместить slider_handle_1, slider_handle_2'):
            slider_handle_1 = page.locator('(//*[@class="ui-range__dot"])[1]')  # Замените на селектор вашего ползунка
            slider_handle_1.hover()
            slider_handle_1.click()  # Если нужно кликнуть
            page.mouse.down()
            page.mouse.move(100, 0)  # Зафиксируем движение
            page.mouse.up()
            time.sleep(5)

            slider_handle_2 = page.locator('(//*[@class="ui-range__dot"])[2]')
            slider_handle_2.hover()
            slider_handle_2.click()  # Если нужно кликнуть
            page.mouse.down()
            page.mouse.move(0, 0)  # Зафиксируем движение
            page.mouse.up()
            time.sleep(5)

            slider_handle_1 = page.locator('(//*[@class="ui-range__dot"])[1]')  # Замените на селектор вашего ползунка
            slider_handle_1.hover()
            slider_handle_1.click()  # Если нужно кликнуть
            page.mouse.down()
            page.mouse.move(100, 0)  # Зафиксируем движение
            page.mouse.up()
            time.sleep(5)
        with allure.step('Клик по найденному элементу'):
            page.click('//*[@id="#app"]/main/div[1]/div[2]/div/div[1]/div[1]/div[6]/button')
        with allure.step('Клик по чекбоксу'):
            page.click('(//*[contains(@class, "filter-checkboxes-list__value")])[28]')
        with allure.step('Проверка, что курсы соответствуют ожиданиям'):
            expected_courses = ["DevOps-инженер", "DevOps-инженер"]
            course_titles = page.locator(".courses-section__grid").all_inner_texts()
            for expected_course in expected_courses:
                assert expected_course in course_titles, f"DevOps-инженер '{expected_course}' не найден в списке."
        pass

    def test_5(self, page):
        with allure.step('Переход на страницу https://github.com/microsoft/vscode/graphs/commit-activity'):
            page.goto('https://github.com/microsoft/vscode/graphs/commit-activity')

        with allure.step('Найдите график активности коммитов'):
            graph = page.locator('(//*[@class="viz"])[1]')
        with allure.step('Наведите мышку на график (на определенную область)'):
            first_bar = graph.locator('rect').nth(0)
            first_bar.hover()
            time.sleep(1)
        with allure.step('Получите текст тултипа'):
            tooltip_locator = page.locator('//div[@class="svg-tip n"]')
            tooltip_text = tooltip_locator.inner_text()
        with allure.step('Проверка содержимого тултипа'):
            expected_values = "8 commits the week of Dec 24"

            assert expected_values in tooltip_text, f"Тултип не содержит ожидаемое значение: {expected_values}. Найдено: {tooltip_text}"
        pass
