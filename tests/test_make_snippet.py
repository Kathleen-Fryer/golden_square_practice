from lib.make_snippet import * 

def test_return_5_words():
    expected = "all five words are returned"
    actual = make_snippet("all five words are returned")
    assert expected == actual 

def test_shorten_phrase_over_5_words():
    expected = "this phrase is too long..."
    actual = make_snippet("this phrase is too long in all honesty")
    assert expected == actual 

def test_less_than_5_words():
    expected = "Hello"
    actual = make_snippet("Hello")
    assert expected == actual

def test_empty_string():
    expected = ""
    actual = make_snippet("")
    assert expected == actual 