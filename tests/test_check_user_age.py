from lib.check_user_age import *
import pytest


"""
Given an empty string, an exception is raised, "Date is not in the right format"
"""

def test_wrong_format():
    with pytest.raises(Exception) as e:
        check_user_age("")
    assert str(e.value) == "Date is not in the right format"


"""
Given a date of birth "1980-05-06", it should return string "Access Granted"
"""
def test_appropriate_age():
    assert check_user_age("1980-05-06") == "Access Granted"
# check_user_age("1980-05-06") => "Access Granted"

"""
Given a date of birth, "2015-08-12", it should return "Access Denied: Your age is 8 and the minimum age is 16"
"""

# check_user_age("2015-08-12") => "Access Denied: Your age is 8 and the minimum age is 16" 