from selenium import webdriver
from selenium.webdriver.common.by import By


class TestSlider:
    def test_slider(self, selenium):

        selenium.get('https://xyssqf.csb.app/demo/InputTextDemo.html')
        el = selenium.find_element(By.XPATH, '(//*[contains(@class, "p-slider-handle")])[4]')
        action_chains = webdriver.ActionChains(selenium)
        action_chains\
            .click_and_hold(el)\
            .move_by_offset(xoffset=50, yoffset=0)\
            .perform()
        action_chains.release().perform()

    def test_splitter(self, selenium):

        selenium.get('https://rzb0if.csb.app/demo/InputTextDemo.html')
        el = selenium.find_element(By.XPATH, '(//*[@class="p-splitter-gutter-handle")][1]')
        action_chains = webdriver.ActionChains(selenium)
        action_chains\
            .click_and_hold(el)\
            .move_by_offset(xoffset=-350, yoffset=0)\
            .perform()
        action_chains.release().perform()

    def test_switch(self, selenium):

        selenium.get('https://hrkdkc.csb.app/demo/InputTextDemo.html')
        selenium.find_element(By.XPATH, '(//span)[2]').click()
        pass
