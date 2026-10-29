# Docstring
"""DOG module
This module does ... bla bla bla and provides the following classes:
-Dog"""

class Dog:
    def __init__(self, name, age): # constructor
        """sets the name and age of the dog"""
        self.name = name
        self.age = age

    def bark(self): # self refers to the current object
        """makes the dog bark"""
        print("Woof")

print(help(Dog)) # shows information about the class

# Annotations
"""def increment(n:int)-> int: # specifies the types
    return n+1
count: int = 0"""

# Exceptions
try:
    result=2/0
    # code that might cause an error
except ZeroDivisionError:
    print("You can't divide by zero")
    # runs if division by zero occurs

# except <ERROR2>:
    # handles another error
# else:
    # runs if no error occurs
finally:
    result = 1
    # runs whether an error occurs or not

print(result)
