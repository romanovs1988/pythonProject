import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class TestInput:

    def test_send_keys(self, selenium):

        selenium.get('https://16nm9r.csb.app/demo/InputTextDemo.html')
        selenium.find_element(By.ID, 'username1').send_keys('basic text')

    def test_clear(self, selenium):

        selenium.get('https://16nm9r.csb.app/demo/InputTextDemo.html')
        el = selenium.find_element(By.ID, 'username1').send_keys('basic text')
        el.send_keys('basic text')
        el.clear()

    def test_copy_past(self, selenium):

        selenium.get('https://16nm9r.csb.app/demo/InputTextDemo.html')
        el = selenium.find_element(By.ID, 'username1').send_keys('basic text')
        el.send_keys('basic text')

        action_chains = webdriver.Action.Chains(selenium)
        action_chains.key_down(Keys.CONTROL).send.keys('a').perform()
        action_chains.key_down(Keys.CONTROL).send.keys('c').perform()
        el.clear()
        el.click()
        action_chains.key_down(Keys.CONTROL).send.keys('v').perform()

    def test_input_mask(self, selenium):

        selenium.get('https://jbns5d.csb.app/demo/InputMaskDemo.html')
        el = selenium.find_element(By.ID, 'basic').send_keys('12345678')
        value = '12345678'
        for c in value:
            el.send_keys(c)
            time.sleep(0.2)

    def test_input_filter(self, selenium):

        selenium.get('https://vypr70.csb.app/demo/InputFilterDemo.html')
        selenium.find_element(By.ID, 'alpha').send_keys('asd123qwe321')

    def test_input_tag(self, selenium):

        selenium.get('https://esy0bz.csb.app/demo/ChipsDemo.html')
        selenium.find_element(By.XPATH, '(//input[3])').send_keys('skillbox' + Keys.ENTER)
        selenium.find_element(By.XPATH, '(//input[3])').send_keys('python' + Keys.ENTER)
        selenium.find_element(By.XPATH, '(//input[3])').send_keys('pytest' + Keys.ENTER)
        pass
