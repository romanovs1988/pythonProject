import pytest
from selenium.webdriver.common.by import By


@pytest.fixture()
class TestExample:
    def test_find_elements(self, selenium):

        selenium.get("https://the-internet.herokuapp.com/login")
        selenium.find_element_by_name('username')  # -> [name="username"] or //*[@name="username"]
        selenium.find_elements_by_id('username')  # -> [id="username"] or #username or //*[@id="username"]
        selenium.find_elements_by_class_name('username')  \
            # -> [class="subheader"] or .subheader or //*[@class="subheader"]

        selenium.find_element_by_xpath('//form/descendant::input[@id="password"]')
        selenium.find_element_by_css_selector('form input#password')

        selenium.find_element_by_xpath('//input')
        selenium.find_element_by_css_selector('input')
        selenium.find_element_by_tag_name('input')

        selenium.get("https://the-internet.herokuapp.com")
        selenium.find_elements_by_partial_link_text('Auth')

        selenium.get("https://the-internet.herokuapp.com")
        selenium.find_element_by_link_text('checkboxes')

        selenium.find_element_by_name(By.ID, 'username')

        h_text = selenium.find_element(By.TAG_NAME, 'h4')
        assert 'tomsmith' in h_text.text
        pass
