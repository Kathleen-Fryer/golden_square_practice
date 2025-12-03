from lib.todo import * 

def test_includes_todo():
    expected = True
    result = includes_todo("#TODO buy milk")
    assert result == expected

def test_doesnt_include_todo():
    expected = False
    result = includes_todo("hello world")
    assert result == expected

def test_returns_false_empty_string():
    expected = False
    result = includes_todo("")
    assert result == expected    