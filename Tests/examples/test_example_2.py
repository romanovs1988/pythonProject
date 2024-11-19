class TestExample:
    def test_example(self, selenium):

        selenium.get("http://skillbox.ru")
        assert 'Skillbox ' == selenium.title

    def test_example_2(self, selenium):

        selenium.get("http://skillbox.ru")
        assert 'Skillbox ' == selenium.title
