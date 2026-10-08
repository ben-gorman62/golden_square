# Grammar Checker Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

import datetime

def time_to_read(text):
    """ Function to check how long it will take to read a document, given an average reading speed of 200 wpm.

    Parameters: (list all parameters and their types)
        text - A string of a section of text or a whole document. This may work better as file parsing.

    Returns: (state the return value and its type)
        The reading time in minutes and seconds in the format "x minutes y seconds", where x and y are integers.

    Side effects: (state any side effects)
        None
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
20 words
"""
time_to_read(20 words) => "6 seconds."

"""
40 words
"""
time_to_read(40 words) => "12 seconds."

"""
600 words
"""
time_to_read(600 words) => "3 minutes 0 seconds."

"""
750 words
"""
time_to_read(600 words) => "3 minutes 45 seconds."

"""
Given an empty string
It returns an exception
"""
time_to_read("") => Exception("Text is empty.")

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Ensure all test function names are unique, otherwise pytest will ignore them!
