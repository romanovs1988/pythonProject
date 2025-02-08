from selenium.webdriver.common.by import By
import allure
import time


def fill_forms(get_driver):
    with allure.step('Нажать на кнопку «Перейти к оплате».'):
        get_driver.find_element(By.CSS_SELECTOR, '.wc-proceed-to-checkout').click()
        time.sleep(3)
    with allure.step('В поле "Имя" ввести "Андрей"'):
        get_driver.find_element(By.CSS_SELECTOR, '#billing_first_name').send_keys('Андрей')
        time.sleep(3)
    with allure.step('В поле "Фамилия" ввести "Андреев"'):
        get_driver.find_element(By.CSS_SELECTOR, '#billing_last_name').send_keys('Андреев')
        time.sleep(3)
    with allure.step('В поле "Адрес" ввести "ул. Пушкина 13, кв. 47"'):
        get_driver.find_element(By.XPATH, '(//*[@id="billing_address_1"])[1]').send_keys('ул. Пушкина 13, кв. 47')
        time.sleep(3)
    with allure.step('В поле "Город / Населенный пункт" ввести "Москва"'):
        get_driver.find_element(By.XPATH, '(//*[@id="billing_city"])[1]').send_keys('Москва')
        time.sleep(3)
    with allure.step('В поле "Область " ввести "Московская"'):
        get_driver.find_element(By.XPATH, '(//*[@id="billing_state"])[1]').send_keys('Московская')
        time.sleep(3)
    with allure.step('В поле "Почтовый индекс " ввести "108811"'):
        get_driver.find_element(By.XPATH, '(//*[@id="billing_postcode"])[1]').send_keys('108811')
        time.sleep(3)
    with allure.step('В поле "Телефон" ввести "+79971234567"'):
        get_driver.find_element(By.XPATH, '(//*[@id="billing_phone"])[1]').send_keys('+79971234567')
        time.sleep(3)
    # with allure.step('В поле "Адрес почты " ввести "andrey5@pizza.ru"'):
    #     get_driver.find_element(By.XPATH, '(//*[@id="billing_phone"])[1]').send_keys('andrey5@pizza.ru')
    #     time.sleep(3)
