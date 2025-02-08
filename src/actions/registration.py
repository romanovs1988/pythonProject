from selenium.webdriver.common.by import By
import allure
import time


def registration(self, get_driver):
    with allure.step('Переход на страницу https://pizzeria.skillbox.cc/'):
        get_driver.get('https://pizzeria.skillbox.cc/')
        time.sleep(3)
    with allure.step('Перейти во вкладку «Мой аккаунт».'):
        get_driver.find_element(By.XPATH, '(//ul/li/a)[10]').click()
        time.sleep(3)
    with allure.step('Нажать на кнопку «Зарегистрироваться».'):
        get_driver.find_element(By.CSS_SELECTOR, '.custom-register-button').click()
        time.sleep(3)
    with allure.step('В поле "Имя пользователя" ввести "Andrey5"'):
        get_driver.find_element(By.CSS_SELECTOR, '#reg_username').send_keys('Andrey5')
        time.sleep(3)
    with allure.step('В поле "Адрес почты" ввести "andrey5@pizza.ru"'):
        get_driver.find_element(By.CSS_SELECTOR, '#reg_email').send_keys('andrey5@pizza.ru')
        time.sleep(3)
    with allure.step('В поле "Пароль" ввести "1Pizza5"'):
        get_driver.find_element(By.CSS_SELECTOR, '#reg_password').send_keys('1Pizza5')
        time.sleep(3)
    with allure.step('Нажать "Зарегистрироваться"'):
        get_driver.find_element(By.XPATH,
                                '//*[@class="woocommerce-Button woocommerce-button\n'
                                ' button woocommerce-form-register__submit"]').click()
        time.sleep(3)
