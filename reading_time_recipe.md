# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.
Reading speed = words per minute

## 2. Design the Function Signature

```python
 def reading_time(num_of_words, reading_speed):
    """
    function: to work out time to read given text
    parameters: number of words (int), reading speed (int)
    returns: minutes to read (float)
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
given a number of words and reading speed 
returns time to read it
"""
reading_time(num_of_words, reading_speed) => time
reading_time(2000, 200) => 10.0 minutes 
reading_time(10, 100) => 0.1 minutes

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

`

Ensure all test function names are unique, otherwise pytest will ignore them!
