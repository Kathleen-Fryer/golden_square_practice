from lib.reading_time import * 

def test_twothousand_words_twohundred_words_per_minute():
    expected = 10.0
    actual = reading_time(2000, 200)
    assert expected == actual 

def test_ten_words_onehundred_words_per_minute():
    expected = 0.1
    actual = reading_time(10, 100)
    assert expected == actual 