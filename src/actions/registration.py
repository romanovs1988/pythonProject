from selenium.webdriver.common.by import By
import allure
import time


def registration(get_driver):
    with allure.step('Переход на страницу https://pizzeria.skillbox.cc/'):
        get_driver.get('https://pizzeria.skillbox.cc/')
        time.sleep(3)
    with allure.step('Перейти во вкладку «Мой аккаунт».'):
        get_driver.find_element(By.XPATH, '(//ul/li/a)[10]').click()
        time.sleep(3)
    with allure.step('Нажать на кнопку «Зарегистрироваться».'):
        get_driver.find_element(By.CSS_SELECTOR, '.custom-register-button').click()
        time.sleep(3)
    with allure.step('В поле "Имя пользователя" ввести "Andrey7"'):
        get_driver.find_element(By.CSS_SELECTOR, '#reg_username').send_keys('Andrey7')
        time.sleep(3)
    with allure.step('В поле "Адрес почты" ввести "andrey7@pizza.ru"'):
        get_driver.find_element(By.CSS_SELECTOR, '#reg_email').send_keys('andrey7@pizza.ru')
        time.sleep(3)
    with allure.step('В поле "Пароль" ввести "1Pizza7"'):
        get_driver.find_element(By.CSS_SELECTOR, '#reg_password').send_keys('1Pizza7')
        time.sleep(3)
    with allure.step('Нажать "Зарегистрироваться"'):
        get_driver.find_element(By.XPATH, '//p/button').click()
        time.sleep(3)
