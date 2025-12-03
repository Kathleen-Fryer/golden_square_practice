from lib.make_snippet import * 

def test_return_5_words():
    expected = "all five words are returned"
    actual = make_snippet("all five words are returned")
    assert expected == actual 

def test_shorten_phrase_over_5_words():
    expected = "this phrase is too long..."
    actual = make_snippet("this phrase is too long in all honesty")
    assert expected == actual 