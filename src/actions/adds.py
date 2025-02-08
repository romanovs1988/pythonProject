from selenium.webdriver.common.by import By
import time


def add_pizza(get_driver):
    get_driver.find_element(By.CSS_SELECTOR, '#menu-item-26').click()
    time.sleep(3)
    get_driver.find_element(By.XPATH, '(//*[contains(@data-product_id, "419")])[2]').click()
    time.sleep(3)
    get_driver.find_element(By.XPATH, '//*[@class="cart-contents wcmenucart-contents"]').click()
    time.sleep(3)
