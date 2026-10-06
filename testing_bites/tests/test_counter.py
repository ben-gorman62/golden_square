from golden_square.testing_bites.lib.counter import *

def test_add_positive_number():
    counter = Counter()
    counter.add(5)
    assert counter.count == 5
    counter.add(17)
    assert counter.count == 22
    counter.add(1987298729872)
    assert counter.count == 1987298729894

def test_add_negative_number():
    counter = Counter()
    counter.add(-1)
    assert counter.count == -1
    counter.add(-19)
    assert counter.count == -20

# adds both positive and negative integers
def test_add_both_number():
    counter = Counter()
    counter.add(10)
    assert counter.count == 10
    counter.add(-5)
    assert counter.count == 5
    counter.add(0)
    assert counter.count == 5

def test_report_function():
    counter = Counter()
    counter.add(10)
    assert counter.report() == "Counted to 10 so far."
    counter.add(-5)
    assert counter.report() == "Counted to 5 so far."
    counter.add(0)
    assert counter.report() == "Counted to 5 so far."