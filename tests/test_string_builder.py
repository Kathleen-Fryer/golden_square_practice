from lib.string_builder import *

def test_add_string():
    stringbuilder = StringBuilder()
    stringbuilder.add("hi")
    result = stringbuilder.output()
    assert result == "hi"

def test_size_of_string():
    stringbuilder = StringBuilder()  
    stringbuilder.add("hello")
    result = stringbuilder.size()
    assert result == 5
