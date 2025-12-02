from lib.add_five import * 
def test_add_five_returns_8_for_3():
    result = add_five(3)
    assert result == 8 

def test_add_five_returns_5_for_0():
    result = add_five(0)
    assert result == 5
