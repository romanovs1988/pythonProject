from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import element_attribute_to_include


class TestValidate:
    def test_is_selected(self, selenium):

        expected_value = 'skillbox'

        selenium.get('https://m1vcki.csb.app/')
        name_field = selenium.find_element(By.ID, 'name')
        name_field.send_keys(expected_value)

        assert name_field.get_attribute('value') == 'skillbox'
        pass

    def test_checkbox(self, selenium):

        selenium.get('https://mkunc5.csb.app/')
        checkbox = selenium.find_element(By.CSS_SELECTOR, 'input')
        checkbox.click()

        assert checkbox.is_selected() is True
        pass

    def test_button(self, selenium):

        selenium.get('https://f05jg8.csb.app/')

        assert element_attribute_to_include(
            locator=(By.CSS_SELECTOR, '[aria-label="Disabled"]'),
            atribute_='disabled'
        )(selenium) is True
        pass
