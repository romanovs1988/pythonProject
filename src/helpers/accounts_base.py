import pytest


class AccontsBase:
    @pytest.fixture()
    def go_to_github(self, selenium):
        selenium.get('https://github.com')
