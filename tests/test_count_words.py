from lib.count_words import *

def test_count_two_words():
    expected = "This string contains 2 words"
    actual = count_words("Hello there")
    assert expected == actual 

def test_count_three_words():
    expected = "This string contains 3 words"
    actual = count_words("execute order 66")
    assert expected == actual 

def test_empty_string():
    expected = "Empty string, nothing to count"
    actual = count_words("")
    assert expected == actual 

def test_count_one_word():
    expected = "This string contains 1 word"
    actual = count_words("Farewell")
    assert expected == actual 