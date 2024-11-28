import pytest


class AccontsBase:
    @pytest.fixture()
    def go_to_github(self, get_driver):
        get_driver.get('https://github.com')
