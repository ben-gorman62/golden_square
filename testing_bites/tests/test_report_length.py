from golden_square.testing_bites.lib.report_length import *

def test_length_of_string():
    assert report_length("Michael") == "This string was 7 characters long."
    assert report_length("   spaces") == "This string was 9 characters long."
    assert report_length("string time") == "This string was 11 characters long."
    assert report_length("") == "This string was 0 characters long."
    assert report_length(" ") == "This string was 1 characters long."