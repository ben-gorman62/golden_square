from golden_square.testing_bites.lib.password_checker import *
import pytest

def test_check_valid_password():
    checker = PasswordChecker()
    assert checker.check("password") == True
    assert checker.check("Michaelbox73") == True
    assert checker.check("!!!!!!!!") == True 

def test_invalid_password():
    checker = PasswordChecker()
    with pytest.raises(Exception) as err:
        checker.check("Passwor")
    message = str(err.value)
    assert message == "Invalid password, must be 8+ characters."
    
    with pytest.raises(Exception) as err:
            checker.check("Inv4l1d")
    message = str(err.value)
    assert message == "Invalid password, must be 8+ characters."