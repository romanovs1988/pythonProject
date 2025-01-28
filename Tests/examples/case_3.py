import time

from selenium.webdriver.common.by import By


class TestClick:
    def test_button_dropdown(self, get_driver):

        get_driver.get('https://github.com/search/advanced')
        time.sleep(5)
        get_driver.find_element(By.CSS_SELECTOR, '[value="Python"]').click()
        time.sleep(5)
        get_driver.find_element(By.CSS_SELECTOR, '#search_stars').send_keys('>20000')
        get_driver.find_element(By.CSS_SELECTOR, '#search_filename').send_keys('environment.yml')
        get_driver.find_element(By.XPATH, '//div[contains(@class, "form-group flattened")]/descendant::button').click()
        pass
