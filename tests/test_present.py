from lib.present import * 
import pytest

def test_wrap_and_unwrap():
    """
    test function works with an item
    """
    present = Present()
    present.wrap("item")
    result = present.unwrap()
    assert result == "item" 


def test_contents_already_wrapped():
    """
    test exception contents wrapped
    """
    present = Present()
    present.contents = "item"
    with pytest.raises(Exception) as e:
        present.wrap(present.contents)
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."

def test_unwrap_empty():
    """
    test exception no contents wrapped
    """
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."
    