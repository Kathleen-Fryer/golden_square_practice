from lib.high_value import * 

def test_first_value_higher():
    high_value = HighValue(2,1)
    result = high_value.get_highest()
    assert result == "First value is higher"

def test_second_value_higher():
    high_value = HighValue(1,2)
    result = high_value.get_highest()
    assert result == "Second value is higher"

def test_values_are_equal():
    high_value = HighValue(3,3)
    result = high_value.get_highest()
    assert result == "Values are equal"

def test_add_to_first_value():
    high_value = HighValue(2,2)
    high_value.add(2, "first")
    result = high_value.get_highest()
    assert result == "First value is higher"

def test_add_to_second_value():
    high_value = HighValue(20,20)
    high_value.add(5, "second")
    result = high_value.get_highest()
    assert result == "Second value is higher"

def test_add_to_both():
    high_value = HighValue(5,6)
    high_value.add(5, "first")
    high_value.add(4, "second")
    result = high_value.get_highest()
    assert result == "Values are equal"