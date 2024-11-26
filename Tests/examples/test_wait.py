from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestWait:
    def test_wait_page_load(self, selenium):

        selenium.get("http://github.com")
        selenium.find_element(By.XPATH, '//*[contains(text(), "Where the world builds software")]')
        pass

    def test_wait_types(self, selenium):

        selenium.get("http://github.com")
        WebDriverWait(selenium, timeout=3).until(
            lambda d: d.find_element(By.XPATH, '//*[contains(text(), "Where the world builds software")]')
        )

    def test_wait_dialog(self, selenium):

        selenium.get("http://github.com")
        WebDriverWait(selenium, timeout=3).until(lambda d: d.find_element(By.ID, 'name'))
        selenium.find_element(By.ID, 'name').send_keys('skillbox')
        selenium.find_element(By.ID, 'email').send_keys('skillbox@mail.ru')
        selenium.find_element(By.NAME, 'password').send_keys('skillbox')
        selenium.execute_script('document.activeElement.blur()')
        selenium.find_element(By.CSS_SELECTOR, '[role="checkbox"]').click()
        selenium.find_element(By.XPATH, '//button/span[contains(text(), "Submit")]').click()
        WebDriverWait(selenium, timeout=5).until(
            lambda d: d.find_element(By.XPATH, '//button/span[contains(text(), "OK")]')
        )
        selenium.find_element(By.XPATH, '//button/span[contains(text(), "OK")]').click()
        pass
