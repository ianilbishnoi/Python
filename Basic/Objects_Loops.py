# Objects
age = 48
print(age.real) # real part of the number
print(age.imag) # imaginary part
print(age.bit_length()) # number of bits needed to represent the integer

items=[1,2]
items.append(3)
items.pop()
print(id(items)) # shows the object's id in memory

# mutable objects can be changed, immutable ones cannot
# int, tuple, str, bool, float, frozenset are immutable
# list, dict, set are mutable

age1=8
age= age1 +1 # creates a new integer object
print(age)
print(age1)

# Loops
# while and for loops

condition = True # runs until the condition becomes false
while condition == True:
    print("The condition is true")
    condition = False

count = 0
while count<10:
    print("The condition is true")
    count += 1

print("After the loop")

items=[1,2,3,4] # can also use names here
for index,item in enumerate((items)): # gives both index and item
    print(index,item) # prints the index and item on each line

items1=[1,2,3,4]
for item in items1:
    if item == 2:
        continue # skips 2 and moves to the next item
    elif item == 3:
        break # stops the loop when item is 3
    print(item)
