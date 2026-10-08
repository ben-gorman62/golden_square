from lib.personal_diary import *
import pytest

# for make_snippet function

def test_empty_string():
    assert make_snippet("") == ""

def test_long_string():
    assert make_snippet("This is a very long string.") == "This is a very long..."
    assert make_snippet("Vialli's in Leamington Spa is a goated establishment.") == "Vialli's in Leamington Spa is..."

def test_short_string():
    assert make_snippet("This string is short.") == "This string is short."
    assert make_snippet("And this one.") == "And this one."

def test_exact_string():
    assert make_snippet("This string has five words.") == "This string has five words."
    assert make_snippet("As does this string here.") == "As does this string here."

# for count_words function

def test_count_words():
    assert count_words("This is a very long string.") == 6
    assert count_words("Vialli's in Leamington Spa is a goated establishment.") == 8
    assert count_words("Three word string.") == 3
    assert count_words("") == 0