from selenium.webdriver.common.by import By
import allure
import time


def authorization(get_driver):
    with allure.step('Переход на страницу https://pizzeria.skillbox.cc/my-account/'):
        get_driver.get('https://pizzeria.skillbox.cc/my-account/')
        time.sleep(3)
    with allure.step('В поле "Имя пользователя" ввести "Andrey7"'):
        get_driver.find_element(By.CSS_SELECTOR, '#username').send_keys('Andrey7')
        time.sleep(3)
    with allure.step('В поле "Пароль" ввести "1Pizza7"'):
        get_driver.find_element(By.CSS_SELECTOR, '#password').send_keys('1Pizza7')
        time.sleep(3)
    with allure.step('Нажать "Войти"'):
        get_driver.find_element(By.XPATH, '(//p/button)[1]').click()
        time.sleep(3)
