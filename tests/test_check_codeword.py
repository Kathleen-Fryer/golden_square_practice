from lib.check_codeword import *

def test_check_codeword_horse():
    result = check_codeword("horse")
    assert result == "Correct! Come in."

def test_check_codeword_horde():
    result = check_codeword("horde")
    assert result == "Close, but nope!"

def test_check_codeword_hat():
    result = check_codeword("hat")
    assert result == "WRONG!"

def test_check_codeword_horse_upper():
    result = check_codeword("HORSE")
    assert result == "Correct! Come in."
