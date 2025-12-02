from lib.greet import * 

def test_greet_bob():
    result = greet("Bob")
    assert result == "Hello, Bob!"

def test_greet_babs():
    result = greet("Babs")
    assert result == "Hello, Babs!"

def test_greet_empty():
    result = greet("")
    assert result == "Hello!"