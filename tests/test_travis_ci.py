from modules.echo import statement

class TestModule():

    def test_statement(self):
        expected_value = 'Hello World'
        test_value = statement('Hello World')
        assert test_value == expected_value

    def test_statement_alternative(self):
        expected_value = 'Hello World Two'
        test_value = statement('Hello World Two')
        assert test_value == expected_value