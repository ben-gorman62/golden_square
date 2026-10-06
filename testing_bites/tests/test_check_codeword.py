from golden_square.testing_bites.lib.check_codeword import *

def test_check_correct_codeword():
    result = check_codeword("horse")
    assert result == "Correct! Come in."

# first letter correct, last letter wrong
def test_check_close_codeword_f():
    result = check_codeword("hound")
    assert result == "WRONG!"

# last letter correct, first letter wrong
def test_check_close_codeword_l():
    result = check_codeword("template")
    assert result == "WRONG!"

# end letter correct, wrong word
def test_check_super_close_codeword():
    result = check_codeword("house")
    assert result == "Close, but nope."

# wrong word entirely
def test_check_wrong_codeword():
    result = check_codeword("pylon")
    assert result == "WRONG!"