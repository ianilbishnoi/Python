# TUPLES
# similar to lists, but we cannot change their elements

names=("Roger","syd") # creating a tuple
names[0] # gets the element at index 0
names.index("Roger") # finds the index of Roger
names[-1] # gets the last element
len(names) # returns the number of elements

print("Roger" in names) # checks if Roger is present

names[0:2] # gets elements from index 0 to 1
sorted(names) # sorts the elements but doesn't change the tuple

newTuple = names + ("Tina","Quincy") # joins two tuples


# DICTIONARY
# stores data as key-value pairs

dog ={ "name":"Roger", "age":22 ,"Race":"Indian"}

print(dog['name']) # gets the value of name

dog['name'] = "syd" # changes the value of name
print(dog)

print(dog.get("name")) # gets the value using the key
print(dog.get("color", "brown")) # returns brown if color is missing

print(dog.pop("name")) # removes name and returns its value
print(dog) # shows the dictionary after removal

print(dog.popitem()) # removes and returns the last key-value pair
print(dog)

print(dog.keys()) # shows all keys
print(dog.values()) # shows all values
print(dog.items()) # shows all key-value pairs

print(list(dog.items())) # converts the pairs into a list

dog["favourite_color"] = "blue" # adds a new key-value pair
del dog['favourite_color'] # removes the key

dogCopy = dog.copy() # creates a copy of the dictionary

print(dog)
print(dog)
