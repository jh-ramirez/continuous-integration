from modules.echo import statement

class test_statement():
    expected_value = 'Hello World'
    test_value = statement('Hello World')

    assert test_value == expected_value