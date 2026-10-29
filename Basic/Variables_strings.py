from operator import truediv

name= "Beau"
age = 39

# valid variable names
# name1, HEIGHT, my_name, _name

# invalid variable names
# 123, test!, % and python keywords like if

# expression - code that gives a value, like 1+1
# statement - an instruction that python executes
# a program is made up of statements, comments are ignored

name =" Beau" # semicolons can separate statements on the same line
print(type(name)==str) # checks if name is a string

# type() and isinstance() can be used to check data types
print(isinstance(name, str))

age = 2
print(isinstance(age, int))

age=float(2) # converting int to float
print(isinstance(age, float))

age= int("20") # converting a string to int
print(isinstance(age, int))

number = "20" # type conversion is also called casting
age = int(number)
print(isinstance(age, int))

# operators
age = 20 # assigning a value

# arithmetic operators
1+1
2-1
2*2
4/2
4%3
4**2
4//2 # gives the quotient without the decimal part

# + can also join strings
print("Scamp"+"is a good dog")

age=8
age+=8 # same as age = age + 8
print(age)

# comparison operators
a=1
b=2
a==b
a!=b
a>b
a<=b

con1= true
con2= false

not con1
con1 and con2
con1 or con2

# or returns the first truthy value, or the last value if none are truthy
print(0 or 1)
print(False or "hey")
print('hi'or 'hey')
print([] or False) # empty lists are considered false
print(False or [])

# and returns the first falsy value, otherwise the last value
print(0 and 1)
print(False and "hey")
print('hi' and 'hey')
print([] and False)
print(False and [])

# bitwise operators
# & does binary AND
# | does binary OR
# ^ does binary XOR
# ~ does binary NOT
# << shifts bits to the left
# >> shifts bits to the right

# is checks whether two variables refer to the same object

# ternary operator - writing if else in one line
def is_adult2(age):
    return True if age >= 18 else False

# strings
"BEAU"
('BEAU')

name= "Beau"
name+='is my name'
age= str(39)

print(age)
print(name)

# string methods
print("Beau".lower())
print("BeAu".upper())
print("beAu".title())

islower()
isaplha()
isalnum()
isdecimal()
lower()
islower()
upper()
isupper()
title()
startswith()
endswith()
replace()
split()
strip()
join()
find() # these methods return values without changing the original string

name ="Be\nau" # \n moves the text to a new line
print(name)

name = "Be\\au" # \\ is used to print a backslash

# indexing and slicing
name = "Beau"
print(name[1:2]) # gets the character at index 1
