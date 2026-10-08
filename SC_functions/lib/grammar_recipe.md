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

def grammar_checker(text):
    """ Function to verify whether or not a string starts with a capital letter and ends with a suitable punctuation mark.

    Parameters: (list all parameters and their types)
        text - A string of a section of text.

    Returns: (state the return value and its type)
        Bool: True or False depending on whether the sentence is grammatically correct or not.

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
correct sentence
"""
grammar_checker("Big Michael loves you.") => True

"""
Only capital letter at start
"""
grammar_checker("Big Michael may love you") => False

"""
Only punctuation at end
"""
grammar_checker("big Michael kinda loves you.") => False

"""
Capital letter at end rather than start
"""
grammar_checker("big Michael does not love yoU") => False

"""
punctionation at start rather than end
"""
grammar_checker("! What ! Michael is not interested") => False

"""
Nothing at either end
"""
grammar_checker("michael says you're boring") => False

"""
No text at all
"""
grammar_checker("") => Exception("Text is empty.")

"""
Not text
"""
grammar_checker(30) => Exception("Text is not a string.")

"""
Not text
"""
grammar_checker(True) => Exception("Text is not a string.")

"""
Not text
"""
grammar_checker(None) => Exception("Text is not a string.")

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Ensure all test function names are unique, otherwise pytest will ignore them!
