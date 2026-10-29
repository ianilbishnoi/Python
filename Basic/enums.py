from enum import Enum

# ENUMS
# gives names to fixed values

class State(Enum):
    INACTIVE = 0
    ACTIVE = 1

print(State.ACTIVE.value) # gets the value assigned to ACTIVE

# enum values are fixed and cannot be reassigned
print(State(1)) # returns State.ACTIVE
print(State['ACTIVE']) # gets the member using its name

# checking the members of State
print(list(State)) # shows all enum members
print(len(State)) # counts the members

# INPUT FUNCTION
age=input("What is your age? :")
print("your age is "+age) # displays the input given by the user

# CONTROL STATEMENTS
condition = True

if condition == False:
    print("The condition") # runs when the condition is false
    print("was true")

# code outside the if block runs after the condition is checked
else:
    print("The condition")
    print("was false")
