#strings are ordered, immutable and used to represent text

greeting ="Hello"
name="Tom"
sentence = greeting + " " + name
print(sentence)

#looping through each character
for i in greeting:
    print(i)

#checking if a substring exists
if 'el' in greeting:
    print('yes')
else:
    print('no')

#.strip() removes whitespace from the beginning and end
#.upper() converts the string to uppercase
#.endswith() checks if the string ends with a given character or substring
#.find() returns the index of the first occurrence, or -1 if not found

str = 'how,are,you,doing?'
list1=str.split(",") #splits the string into a list
print(list1)

new_str=' '.join(list1) #joins list elements into a string with spaces
print(new_str)

#f-strings make it easy to insert variables into a string
var = 3.123
var2 = 6
str=f'the variable is{var} and {var2}'
print(str)
