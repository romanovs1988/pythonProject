import re
import time
from lib2to3.pgen2 import driver
from winreg import DeleteValue
import requests
from urllib3.util import proxy
from selenium.webdriver.common.alert import Alert
from src.actions.adds import add_pizza
from src.actions.authorization import authorization
from src.actions.forms import fill_forms
from src.actions.registration import registration
import allure
import pytest
from selenium import webdriver
from playwright.sync_api import expect
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import wait
from selenium.webdriver.common.keys import Keys
from browsermobproxy import Server


@allure.feature('Full Accounts')
@allure.story('Waiting page load')
class TestValidate:
    @allure.title('Проверка загрузки страницы')
    def test_1(self, get_driver):
        with allure.step('Переход на сайт https://pizzeria.skillbox.cc/'):
            get_driver.get('https://pizzeria.skillbox.cc/')
            time.sleep(5)
        with allure.step('Добавить пиццу "Как у бабушки" «В корзину».'):
            get_driver.find_element(By.XPATH, '(//*[contains(@data-product_id, "423")])[2]').click()
            time.sleep(5)
        with allure.step('Добавить пиццу "Рай" «В корзину».'):
            get_driver.find_element(By.XPATH, '(//*[contains(@data-product_id, "421")])[2]').click()
            time.sleep(5)
        with allure.step('Переключить слайдер вправо.'):
            get_driver.find_element(By.XPATH, '//*[contains(@class, "slick-next")]').click()
            time.sleep(5)
        with allure.step('Проверить, что при переключении слайдера вправо пицца "Пепперони" появляется в слайдере.'):
            expected_pizza = get_driver.find_element(By.XPATH, '(//a/h3)[9]')
            assert 'ПИЦЦА «ПЕППЕРОНИ»' in expected_pizza.text
        with allure.step('Добавить пиццу "Пепперони" «В корзину».'):
            get_driver.find_element(By.XPATH, '(//*[contains(@data-product_id, "417")])[2]').click()
            time.sleep(5)
        with allure.step('Переключить слайдер влево.'):
            get_driver.find_element(By.XPATH, '//*[contains(@class, "slick-prev")]').click()
            time.sleep(5)


        pass

    def test_2(self, get_driver):
        with allure.step('Переход на сайт https://pizzeria.skillbox.cc/'):
            get_driver.get('https://pizzeria.skillbox.cc/')
            time.sleep(3)
        with allure.step('Нажать на картинку пиццы «4 в 1» в слайдере.'):
            get_driver.find_element(By.XPATH, '(//*[contains(@title, "Пицца «4 в 1»")])[1]').click()
            time.sleep(3)
        with allure.step('Выбрать дополнительную опцию в выпадающем списке "Выбор борта для пиццы" (сырный борт, пицца «4 в 1»)'):
            get_driver.find_element(By.CSS_SELECTOR, '#board_pack').click()
            time.sleep(3)
            get_driver.find_element(By.XPATH, '//*[contains(@value, "55.00")]').click()
            time.sleep(3)
        with allure.step('Нажать на кнопку «В корзину».'):
            get_driver.find_element(By.XPATH, '(//*[contains(@type, "submit")])[2]').click()
            time.sleep(3)
        with allure.step('Проверить, что пицца "4 в 1 дополнительно: сырный борт" добавлена в корзину.'):
            get_driver.find_element(By.XPATH, '//*[@class="cart-contents wcmenucart-contents"]').click()
            time.sleep(3)
            cheese_board = get_driver.find_element(By.XPATH, '(//*[@class="variation-"])[2]')
            assert 'Сырный борт' in cheese_board.text
        pass

    def test_3(self, get_driver):
        with allure.step('Переход на сайт https://pizzeria.skillbox.cc/'):
            get_driver.get('https://pizzeria.skillbox.cc/')
            time.sleep(3)
        with allure.step('Добавить пиццу "Рай" «В корзину».'):
            get_driver.find_element(By.XPATH, '(//*[contains(@data-product_id, "421")])[2]').click()
            time.sleep(3)
        with allure.step('Нажать «Корзина».'):
            get_driver.find_element(By.XPATH, '//*[@class="cart-contents wcmenucart-contents"]').click()
            time.sleep(3)
        with allure.step('Нажать на кнопку "Кол-во" и увеличить на +1.'):
            expected_value = '2'
            el = get_driver.find_element(By.XPATH, '(//div/input)[1]')
            el.clear()
            time.sleep(3)
            el.send_keys(expected_value)
        with allure.step('Нажать на кнопку «Обновить корзину».'):
            get_driver.find_element(By.XPATH, '(//*[@class="button"])[2]').click()
            time.sleep(3)
        with allure.step('Проверить, что количество пиццы "Рай" в "Корзине" = 2.'):
            el_2 = get_driver.find_element(By.XPATH, '//*[@value="2"]')
            assert el_2.get_attribute('value') == '2'

        pass

    def test_4(self, get_driver):
        with allure.step('Переход на страницу https://pizzeria.skillbox.cc/'):
            get_driver.get('https://pizzeria.skillbox.cc/')
            time.sleep(3)
        with allure.step('Добавить пиццу "Ветчина и грибы" в "Корзину"'):
            get_driver.find_element(By.XPATH, '(//*[contains(@data-product_id, "419")])[2]').click()
            time.sleep(3)
        with allure.step('Перейти в "Корзину"'):
            get_driver.find_element(By.XPATH, '//*[@class="cart-contents wcmenucart-contents"]').click()
            time.sleep(3)
        with allure.step('Нажать "Удалить" пиццу "Ветчина и грибы" из "Корзина"'):
            get_driver.find_element(By.XPATH, '//*[@class="remove"]').click()
            time.sleep(3)
        with allure.step('Проверить, что "Корзина пуста"'):
            cart = get_driver.find_element(By.XPATH, '//*[@class="cart-empty woocommerce-info"]')
            assert 'Корзина пуста.' in cart.text

        pass

    def test_5(self, get_driver):
        with allure.step('Переход на страницу https://pizzeria.skillbox.cc/'):
            get_driver.get('https://pizzeria.skillbox.cc/')
            time.sleep(3)
        with allure.step('Нажать на раздел "Меню"'):
            get_driver.find_element(By.XPATH, '(//ul/li/a)[2]').click()
            time.sleep(3)
        with allure.step('Выбрать в выпадающем списке раздел «Десерты».'):
            get_driver.find_element(By.XPATH, '(//*[contains(text(), "Десерты")])[2]').click()
            time.sleep(3)
        with allure.step('В блоке "Фильтровать по цене" сместить правую кнопку фильтра влево на отметку 130.'):
            el = get_driver.find_element(By.XPATH, '(//*[@class="ui-slider-handle ui-state-default ui-corner-all"])[2]')
            action_chains = webdriver.ActionChains(get_driver)
            action_chains \
                .click_and_hold(el) \
                .move_by_offset(xoffset=-200, yoffset=0) \
                .perform()
            action_chains.release().perform()
            time.sleep(3)
        with allure.step('Нажать "Применить"'):
            get_driver.find_element(By.XPATH, '(//div/div/button)[2]').click()
            time.sleep(3)
        with allure.step('Добавить "В корзину" десерт «Булочка с корицей»'):
            get_driver.find_element(By.XPATH, '(//div/div/a)[9]').click()
            time.sleep(3)
        with allure.step('Проверить, что в списке цена за товар не превышает 130 рублей'):
            price = get_driver.find_element(By.XPATH, '//*[@class="to"]')
            assert '130₽' in price.text

        pass

    def test_6(self, get_driver):
        with allure.step('Переход на страницу https://pizzeria.skillbox.cc/'):
            get_driver.get('https://pizzeria.skillbox.cc/')
            time.sleep(3)
        with allure.step('Добавить пиццу "Ветчина и грибы" в "Корзину"'):
            get_driver.find_element(By.XPATH, '(//*[contains(@data-product_id, "419")])[2]').click()
            time.sleep(3)
        with allure.step('Перейти в "Корзину"'):
            get_driver.find_element(By.XPATH, '//*[@class="cart-contents wcmenucart-contents"]').click()
            time.sleep(3)
        with allure.step('Нажать на кнопку «Перейти к оплате».'):
            get_driver.find_element(By.XPATH, '//*[contains(text(), "ПЕРЕЙТИ К ОПЛАТЕ")]').click()
            time.sleep(3)
        with allure.step('Проверить, что отображается надпись "Авторизуйтесь."'):
            aut = get_driver.find_element(By.CSS_SELECTOR, '.showlogin')
            assert 'Авторизуйтесь' in aut.text

        pass

    def test_7(self, get_driver):
        with allure.step('Зарегистрироваться на сайте'):
            registration(self, get_driver)
        with allure.step('Перейти во вкладку «Мой аккаунт».'):
            get_driver.find_element(By.XPATH, '(//ul/li/a)[10]').click()
            time.sleep(3)
        with allure.step('Проверить, что на странице "Мой аккаунт" отображается информация "Привет Andrey5"'):
            user_name = get_driver.find_element(By.XPATH, '(//div/p/strong)[1]')
            assert 'Andrey5' in user_name.text

        pass

    def test_8(self, get_driver):
        with allure.step('Авторизоваться на сайте'):
            authorization(get_driver)
            time.sleep(3)
        with allure.step('Перейти в "Корзину"'):
            get_driver.find_element(By.XPATH, '//*[@class="cart-contents wcmenucart-contents"]').click()
            time.sleep(3)
        with allure.step('Заполнение форм данными'):
            fill_forms(get_driver)
        with allure.step('В поле "Дата заказа" выбрать "На завтра"'):
            get_driver.find_element(By.CSS_SELECTOR, '#order_date').send_keys('14.01.2025')
            time.sleep(3)
        with allure.step('Нажать radio-button "Оплата при доставке"'):
            get_driver.find_element(By.CSS_SELECTOR, '#payment_method_cod').click()
            time.sleep(3)
        with allure.step('Нажать чек-бокс "I have read and agree to the website terms and conditions"'):
            get_driver.find_element(By.CSS_SELECTOR, '#terms').click()
            time.sleep(3)
        with allure.step('Нажать "Оформить заказ"'):
            get_driver.find_element(By.CSS_SELECTOR, '#place_order').click()
            time.sleep(3)
        with allure.step('Проверить, что на странице "Заказ получен" отображаются веденные данные'):
            address_check = get_driver.find_element(By.XPATH, '//section/address')
            assert ('Андрей Андреев\n'
                'ул. Пушкина 13, кв. 47\n'
                'Москва\n'
                'Московская\n'
                '108811\n'
                '+79971234567\n'
                'andrey5@pizza.ru') in address_check.text

        pass

    def test_apply_promo_code_1(self, get_driver):
        with allure.step('Переход на страницу https://pizzeria.skillbox.cc/'):
            get_driver.get('https://pizzeria.skillbox.cc/')
            time.sleep(3)
        with allure.step('Добавить пиццу "Ветчина и грибы" в "Корзину"'):
            add_pizza(get_driver)
            time.sleep(3)
        with allure.step('Перейдите в окно оформления товаров.'):
            get_driver.find_element(By.XPATH, '//*[@class="cart-contents wcmenucart-contents"]').click()
            time.sleep(3)
        with allure.step('Примените промокод GIVEMEHALYAVA.'):
            get_driver.find_element(By.CSS_SELECTOR, '#coupon_code').send_keys('GIVEMEHALYAVA')
            time.sleep(3)
        with allure.step('Нажать "Применить купон"'):
            get_driver.find_element(By.XPATH, '//*[@value="Применить купон"]').click()
            time.sleep(3)
        with allure.step('Убедитесь, что конечная сумма заказа уменьшилась на 10%.'):
            price = get_driver.find_element(By.XPATH, '(//span/bdi)[4]')
            assert '405,00' in price.text

        pass

    def test_apply_promo_code_2(self, get_driver):
        with allure.step('Переход на страницу https://pizzeria.skillbox.cc/'):
            get_driver.get('https://pizzeria.skillbox.cc/')
            time.sleep(3)
        with allure.step('Добавить пиццу "Ветчина и грибы" в "Корзину"'):
            add_pizza(get_driver)
            time.sleep(3)
        with allure.step('Перейдите в окно оформления товаров.'):
            get_driver.find_element(By.XPATH, '//*[@class="cart-contents wcmenucart-contents"]').click()
            time.sleep(3)
        with allure.step('Примените промокод DC120.'):
            get_driver.find_element(By.CSS_SELECTOR, '#coupon_code').send_keys('DC120')
            time.sleep(3)
        with allure.step('Нажать "Применить купон"'):
            get_driver.find_element(By.XPATH, '//*[@value="Применить купон"]').click()
            time.sleep(3)
        with allure.step('Убедитесь, что конечная сумма заказа НЕ уменьшилась на 10%.'):
            price = get_driver.find_element(By.XPATH, '(//span/bdi)[4]')
            assert '450,00' in price.text

        pass

    def test_apply_promo_code_3(self, get_driver, send_500_response):
        with allure.step('Переход на страницу https://pizzeria.skillbox.cc/'):

            get_driver.get('https://pizzeria.skillbox.cc/')
            time.sleep(3)
        with allure.step('Добавить пиццу "Ветчина и грибы" в "Корзину"'):
            get_driver.find_element(By.XPATH, '(//*[contains(@data-product_id, "419")])[2]').click()
            time.sleep(3)
        with allure.step('Перейдите в окно оформления товаров.'):
            get_driver.find_element(By.XPATH, '//*[@class="cart-contents wcmenucart-contents"]').click()
            time.sleep(3)
        with allure.step('Примените промокод GIVEMEHALYAVA.'):
            get_driver.find_element(By.CSS_SELECTOR, '#coupon_code').send_keys('GIVEMEHALYAVA')
            time.sleep(3)
            get_driver.find_element(By.XPATH, '//*[@name="apply_coupon"]').click()

        with allure.step('Перехватите запрос, уходящий с веба на сервер, и заблокируйте его. Вернуть ответ с ошибкой (500).'):
            send_500_response(get_driver)

        pass

    def test_apply_promo_code_4(self, get_driver):
        with allure.step('Авторизоваться на сайте'):
            authorization(get_driver)
            time.sleep(3)
        with allure.step('Добавить пиццу "Ветчина и грибы" в "Корзину"'):
            add_pizza(get_driver)
            time.sleep(3)
        with allure.step('Примените промокод GIVEMEHALYAVA.'):
            get_driver.find_element(By.CSS_SELECTOR, '#coupon_code').send_keys('GIVEMEHALYAVA')
            time.sleep(3)
        with allure.step('Нажать "Применить купон"'):
            get_driver.find_element(By.XPATH, '//*[@value="Применить купон"]').click()
            time.sleep(3)
        with allure.step('Нажать "Прейти к оплате"'):
            get_driver.find_element(By.XPATH, '//*[@class="checkout-button button alt wc-forward"]').click()
            time.sleep(3)
        with allure.step('Нажать чек-бокс "I have read and agree to the website terms and conditions"'):
            get_driver.find_element(By.XPATH, '//*[@id="terms"]').click()
            time.sleep(3)
        with allure.step('Нажать "Оформить заказ"'):
            get_driver.find_element(By.CSS_SELECTOR, '#place_order').click()
            time.sleep(3)
        with allure.step('Добавить пиццу "Ветчина и грибы" в "Корзину"'):
            add_pizza(get_driver)
            time.sleep(3)
        with allure.step('Очистить поле "Промокод"'):
            el = get_driver.find_element(By.CSS_SELECTOR, '#coupon_code')
            el.clear()
            time.sleep(3)
        with allure.step('Примените промокод GIVEMEHALYAVA.'):
            get_driver.find_element(By.CSS_SELECTOR, '#coupon_code').send_keys('GIVEMEHALYAVA')
            time.sleep(3)
        with allure.step('Нажать "Применить купон"'):
            get_driver.find_element(By.XPATH, '//*[@value="Применить купон"]').click()
            time.sleep(3)
        with allure.step('Проверить, что второй раз промокод уже не срабатывает для пользователя.'):
            coupon = get_driver.find_element(By.XPATH, '//*[@role="alert"]')
            assert 'Coupon code already applied!' in coupon.text

        pass

    def test_bonus_program_1(self, get_driver):
        with allure.step('Перейдите на страницу бонусной программы: https://pizzeria.skillbox.cc/bonus/'):
            get_driver.get('https://pizzeria.skillbox.cc/bonus/')
            time.sleep(3)
        with allure.step('Ввести "Андрей" в поле "Имя"'):
            get_driver.find_element(By.CSS_SELECTOR, '#bonus_username').send_keys('Андрей')
            time.sleep(3)
        with allure.step('Ввести +79971234567 в поле "Телефон"'):
            get_driver.find_element(By.CSS_SELECTOR, '#bonus_phone').send_keys('+79971234567')
            time.sleep(3)
        with allure.step('Нажать "Оформить карту"'):
            get_driver.find_element(By.XPATH, '//*[@style="cursor:pointer;"]').click()
            time.sleep(3)
            alert = Alert(get_driver)
            alert.accept()
            time.sleep(3)
        with allure.step('Убедиться в успешной активации данных.'):
            bonus = get_driver.find_element(By.XPATH, '//div/div/h3')
            assert 'Ваша карта оформлена!' in bonus.text

        pass

    def test_bonus_program_2(self, get_driver):
        with allure.step('Перейдите на страницу бонусной программы: https://pizzeria.skillbox.cc/bonus/'):
            get_driver.get('https://pizzeria.skillbox.cc/bonus/')
            time.sleep(3)
        with allure.step('Ввести "1" в поле "Имя"'):
            get_driver.find_element(By.CSS_SELECTOR, '#bonus_username').send_keys('1')
            time.sleep(3)
        with allure.step('Ввести +79971234567 в поле "Телефон"'):
            get_driver.find_element(By.CSS_SELECTOR, '#bonus_phone').send_keys('+79971234567')
            time.sleep(3)
        with allure.step('Нажать "Оформить карту"'):
            get_driver.find_element(By.XPATH, '//*[@style="cursor:pointer;"]').click()
            time.sleep(3)
        with allure.step('Убедиться, что отображается надпись "Введен неверный формат имени'):
            name_field = get_driver.find_element(By.XPATH, '//*[@id="bonus_content"]')
            assert 'Введен неверный формат имени' in name_field.text

        pass

    def test_bonus_program_3(self, get_driver):
        with allure.step('Перейдите на страницу бонусной программы: https://pizzeria.skillbox.cc/bonus/'):
            get_driver.get('https://pizzeria.skillbox.cc/bonus/')
            time.sleep(3)
        with allure.step('Ввести "Андрей" в поле "Имя"'):
            get_driver.find_element(By.CSS_SELECTOR, '#bonus_username').send_keys('Андрей')
            time.sleep(3)
        with allure.step('Ввести +7 в поле "Телефон"'):
            get_driver.find_element(By.CSS_SELECTOR, '#bonus_phone').send_keys('+7')
            time.sleep(3)
        with allure.step('Нажать "Оформить карту"'):
            get_driver.find_element(By.XPATH, '//*[@style="cursor:pointer;"]').click()
            time.sleep(3)
        with allure.step('Убедиться, что отображается надпись "Введен неверный формат телефона'):
            name_field = get_driver.find_element(By.XPATH, '//*[@id="bonus_content"]')
            assert 'Введен неверный формат телефона' in name_field.text

        pass









