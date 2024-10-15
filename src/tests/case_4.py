from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class TestSlider:
    def test_slider(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://skillbox.ru/code/')
        driver.find_element(By.XPATH, '//label/span[contains(text(), "Профессия")]').click()
        el = driver.find_element(By.XPATH, '(//*[contains(@class, "ui-range__dot")])[1]')
        action_chains = webdriver.ActionChains(driver)
        action_chains \
            .click_and_hold(el) \
            .move_by_offset(xoffset=5, yoffset=0) \
            .perform()
        action_chains.release().perform()
        el = driver.find_element(By.XPATH, '(//*[contains(@class, "ui-range__dot")])[2]')
        action_chains = webdriver.ActionChains(driver)
        action_chains \
            .click_and_hold(el) \
            .move_by_offset(xoffset=-12, yoffset=0) \
            .perform()
        action_chains.release().perform()
        driver.find_element(By.XPATH, '(//*[contains(@class, "filter-checkboxes-list__value")])[2]').click()
        pass


