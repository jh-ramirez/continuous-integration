from modules.echo import statement

class TestModule():

    def test_statement(self):
        expected_value = 'Hello World'
        test_value = statement('Hello World')
        assert test_value == expected_value