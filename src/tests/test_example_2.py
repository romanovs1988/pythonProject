class TestExample:
    def test_example(self, set_up_browser):
        driver = set_up_browser
        driver.get("http://skillbox.ru")
        assert 'Skillbox ' == driver.title

    def test_example_2(self, set_up_browser):
        driver = set_up_browser
        driver.get("http://skillbox.ru")
        assert 'Skillbox ' == driver.title