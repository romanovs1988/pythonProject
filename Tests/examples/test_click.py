from selenium import webdriver
from selenium.webdriver.common.by import By


class TestClick:
    def test_click(self, selenium):

        selenium.get('https://h8xf8u.csb.app/demo/ButtonDemo.html')
        selenium.find_element(By.XPATH, '//button/span[contains(text(), "Primary")]').click()

    def test_failed_click(self, selenium):

        selenium.get('https://h8xf8u.csb.app/demo/ButtonDemo.html')
        selenium.find_element(By.XPATH, '//button').click()

    def test_double_click(self, selenium):

        selenium.get('https://18c7w2.csb.app/demo/ButtonDemo.html')
        action_chains = webdriver.ActionChains(selenium)
        action_chains.double_click(selenium.find_element(By.XPATH, '//button/span[contains(text(), "Primary")]'))\
            .perform()

    def test_checkbox(self, selenium):

        selenium.get('https://bn6oef.csb.app/demo/ButtonDemo.html')
        selenium.find_element(By.CSS_SELECTOR, '[for="city1"]').click()
        selenium.find_element(By.CSS_SELECTOR, '[for="city2"]').click()

    def test_radio(self, selenium):

        selenium.get('https://349skk.csb.app/demo/ButtonDemo.html')
        selenium.find_element(By.CSS_SELECTOR, '[for="A"]').click()

    def test_modal(self, selenium):

        selenium.get('https://ghw76z.csb.app/demo/ButtonDemo.html')
        selenium.find_element(By.XPATH, '//button/span[contains(text(), "Confirm")])[2]').click()
        selenium.find_element(By.CSS_SELECTOR, '[aria-label="Yes"]').click()

    def test_button_dropdown(self, selenium):

        selenium.get('https://8sunho.csb.app/demo/ButtonDemo.html')
        selenium.find_element(By.CSS_SELECTOR, '[aria-owns="pr_id_2_overlay"]').click()
        selenium.find_element(By.LINK_TEXT, 'Delete').click()

    def test_calendar(self, selenium):

        selenium.get('https://jpy5dz.csb.app/demo/ButtonDemo.html')
        selenium.find_element(By.CSS_SELECTOR, '#range > input').click()
        selenium.find_element(By.XPATH, '//span[contains(text(), "18")])[2]').click()
        selenium.find_element(By.XPATH, '//span[contains(text(), "22")])[2]').click()
        pass
