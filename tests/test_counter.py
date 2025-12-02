from lib.counter import * 

def test_count_to_five():
    counter = Counter()
    counter.add(5)
    result = counter.report()
    assert result == "Counted to 5 so far." 

def test_count_to_three():
    counter = Counter()
    counter.add(3)
    result = counter.report()
    assert result == "Counted to 3 so far."

def test_no_count():
    counter = Counter()
    counter.add(0)
    result = counter.report()
    assert result == "Counted to 0 so far."