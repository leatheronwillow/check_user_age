# {{PROBLEM}} Function Design Recipe

## 1. Describe the Problem

As an admin
So that I can determine whether a user is old enough
I want to allow them to enter their date of birth as a string in the format `YYYY-MM-DD`.

As an admin
So that under-age users can be denied entry
I want to send a message to any user under the age of 16 saying their access is denied, telling them their current age and the required age (16).

As an admin
So that old enough users can be granted access
I want to send a message to any user aged 16 or older to say that access has been granted.

As an admin
So that invalid entries are rejected
I want to generate an exception when the date of birth isn't the right type or format.


## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def check_user_age(date_of_birth):
    # Parameters:
        # A string containing date of birth in the format `YYYY-MM-DD`
    # Returns:
    #     String saying either access granted or access denied
    pass

```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE
"""
Given an empty string, an exception is raised, "Date is not in the right format"
"""
check_user_age("") => Exception("Date is not in the right format")

"""
Given a date of birth "1980-05-06", it should return string "Access Granted"
"""
check_user_age("1980-05-06") => "Access Granted"

"""
Given a date of birth, "2015-08-12", it should return "Access Denied: Your age is 8 and the minimum age is 16"
"""

check_user_age("2015-08-12") => "Access Denied: Your age is 8 and the minimum age is 16"




```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
```

Ensure all test function names are unique, otherwise pytest will ignore them!
