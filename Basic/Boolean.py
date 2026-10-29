# Booleans
# done = True  # T should be capital
# done = False # F should be capital

done="Beau" # this is a string
# 0 is false, other numbers are true
# empty strings are false, non-empty strings are true

print(type(done)==bool) # checks if done is a boolean

if done:
    print("yes")
else:
    print("no")

book_1_read = True
book_2_read = False

read_any_book = any([book_1_read, book_2_read]) # true if any one is true
read_any_book1 = all([book_1_read, book_2_read]) # true if both are true

# Number Datatypes
# int for whole numbers
# float for decimal numbers
# complex for real and imaginary numbers

num= complex(2,3)

print(num.real, num.imag) # prints real and imaginary parts

# BUILT-IN FUNCTIONS

abs((5.5)) # gives the positive value
print(round(5.49,1)) # rounds to 1 decimal place
