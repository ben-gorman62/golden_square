from golden_square.testing_bites.lib.present import *
import pytest

def test_present():
    present = Present()
    assert present.contents == None
    present.wrap("Bike")
    assert present.contents == "Bike"
    present.unwrap()
    assert present.contents == "Bike"

def test_already_wrapped():
    present = Present()
    present.wrap("Bike")
    assert present.contents == "Bike"
    
    with pytest.raises(Exception) as err:
        present.wrap("Bike 2")
    message = str(err.value)
    assert message == "A contents has already been wrapped."
    
    present.unwrap()
    assert present.contents == "Bike"

def test_nothing_wrapped():
    present = Present()
    with pytest.raises(Exception) as err:
        present.unwrap()
    message = str(err.value)
    assert message == "No contents have been wrapped."