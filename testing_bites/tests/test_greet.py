from golden_square.testing_bites.lib.greet import *

def test_greet_person_with_given_name():
    result = greet("Andrew")
    assert result == "Hello, Andrew!"