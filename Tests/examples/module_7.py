import allure
import time


class TestValidate:
    @allure.title('Проверка загрузки страницы')
    def test_1(self, page):
        with allure.step('Открытие страницы https://github.com/microsoft/vscode/issues'):
            page.goto("https://github.com/microsoft/vscode/issues")
        with allure.step('Введите в поиск фильтр in:title.'):
            search_input = page.locator('#repository-input')
            page.wait_for_timeout(3000)
            search_input.fill("in:title")
        with allure.step('Введите в поиск ключевое слово "bug".'):
            search_input.fill("bug")
        with allure.step('Нажмите на Enter.'):
            search_input.press("Enter")
        with allure.step('Получите все названия задач.'):
            issue_titles = page.locator("a[data-hovercard-type='issue']").all_inner_texts()
        with allure.step('Проверьте, что каждая из задач содержит в названии слово "bug".'):
            for title in issue_titles:
                assert "bug" in title.lower(), f"'{title}' не содержит слово 'bug'"
        pass

    def test_2(self, page):
        with allure.step('Переход на страницу https://github.com/microsoft/vscode/issues'):
            page.goto('https://github.com/microsoft/vscode/issues')
        with allure.step('Нажмите на кнопку Author'):
            author_button = page.locator('[aria-label="Filter by author"]')
            author_button.click()
        with allure.step('Введите в поиск имя bpasero'):
            search_input = page.locator('//*[contains(@class,\n'
                                        ' "UnstyledTextInput__ToggledUnstyledTextInput-sc-14ypya-0 jkNcAv")]')
            search_input.fill("bpasero")
        with allure.step('Дождитесь появления в списке нужного автора'):
            page.wait_for_selector('//*[contains(@class,\n'
                                   ' "UnstyledTextInput__ToggledUnstyledTextInput-sc-14ypya-0 jkNcAv")]')
        with allure.step('Выберите в выпадающем списке элемент с названием "bpasero"'):
            author_selection = page.locator("a[aria-label='bpasero']")
            author_selection.click()
        with allure.step('Получите все задачи'):
            issue_authors = page.locator("a[data-hovercard-type='user']").all_inner_texts()
        with allure.step('Проверьте, что автор всех задач введён в поиск ("bpasero").'):
            for author in issue_authors:
                assert author.lower() == "bpasero", f"Автор '{author}' не совпадает с 'bpasero'"

        pass

    def test_3(self, page):
        # Шаг 1: Откройте страницу Advanced search на GitHub.
        page.goto("https://github.com/search/advanced")

        # Шаг 2: В поле языка, на котором написан код, выберите Python.
        language_selector = page.locator('//select[@id="search_language"]')
        language_selector.select_option("Python")

        # Шаг 3: В поле количества звёзд у репозитория выберите >20000.
        star_field = page.locator('#search_stars')
        star_field.fill(">20000")

        # Шаг 4: В поле с названием файла выберите environment.yml.
        filename_field = page.locator('#search_filename')
        filename_field.fill("environment.yml")

        # Шаг 5: Нажмите на кнопку поиска.
        search_button = page.locator('//div[contains(@class, "form-group flattened")]/descendant::button')
        search_button.click()

        # Шаг 6: Соберите информацию по всем репозиториям.
        repo_list = page.locator("ul.repo-list li").all_inner_texts()

        # Шаг 7: Проверьте, что в списке отображаются репозитории с количеством звёзд >20000.
        for repo in repo_list:
            # Для получения информации о звёздах необходимо правильно распарсить текст
            if " " in repo:
                parts = repo.split(" ")
                stars = parts[0]  # Пример формата: "21k stars"
                stars_count = int(stars[:-1]) * (1000 if stars.endswith('k') else 1)

                # Проверяем, что звёзд больше 20000
                assert stars_count > 20000, f"Репозиторий '{repo}' имеет звёзд: {stars_count}"
        pass

    def test_4(self, page, go_to_url, x=0, y=0):
        # Шаг 1: Перейдите на сайт Skillbox
        go_to_url('https://skillbox.ru/code/')

        # Шаг 2: Выбор радиокнопки "Профессия" в разделе "Тип обучения на платформе"
        profession_radio = page.locator('(//*[contains\
            (@class, "ui-radio-field__value ui-radio-field__value--small")])[2]')
        profession_radio.check()

        """slider_handle_1 = page.locator('(//*[@class="ui-range__dot"])[1]')  # Замените на селектор вашего ползунка
        slider_handle_1.hover()
        slider_handle_1.click()  # Если нужно кликнуть
        page.mouse.down()
        page.mouse.move(100, 0) # Зафиксируем движение
        page.mouse.up()
        time.sleep(5)"""

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

        # Подождите немного, чтобы видеть результат
        # time.sleep(2)

        # Шаг 4: Выбор любого чекбокса в тематике
        page.click('//*[@id="#app"]/main/div[1]/div[2]/div/div[1]/div[1]/div[6]/button')
        page.click('(//*[contains(@class, "filter-checkboxes-list__value")])[28]')

        # Шаг 5: Проверка, что курсы соответствуют ожиданиям
        # Обычно это делается с помощью конкретных курсов, которые вы ожидаете увидеть.
        # Например, этим мы можем проверить текст заголовков курсов.
        time.sleep(5)
        expected_courses = ["DevOps-инженер", "DevOps-инженер"]  # Пример ожидаемых курсов, замените на реальные
        courses = page.locator('//*[@class="ui-product-card-main__wrap"]').all_inner_texts()

        for expected in expected_courses:
            assert expected in courses, f"Ожидалось увидеть курс '{expected}', но он не найден."
        pass

    def test_5(self, page):
        # Шаг 1: Откройте страницу Commit Activity · microsoft/vscode на GitHub

        page.goto('https://github.com/microsoft/vscode/graphs/commit-activity')

        # Шаг 2: Найдите график активности коммитов
        graph = page.locator('(//*[@class="viz"])[1]')

        # Шаг 3: Наведите мышку на график (на определенную область)
        # Поскольку график представляет собой SVG, выберем координаты для наведения.
        # Например, выбираем центр первого прямоугольника на графике.
        first_bar = graph.locator('rect').nth(0)
        first_bar.hover()

        # Даем время для появления тултипа
        time.sleep(1)

        # Шаг 4: Получите текст тултипа
        tooltip_locator = page.locator('//div[@class="svg-tip n"]')
        tooltip_text = tooltip_locator.inner_text()

        # Ожидаемые вами значения в тултипе
        expected_values = "8 commits the week of Dec 24"  # Замените на ваши ожидаемые значения

        # Проверка содержимого тултипа
        assert expected_values in tooltip_text, (f"Тултип не содержит ожидаемое\n"
                                                 f" значение: {expected_values}. Найдено: {tooltip_text}")
