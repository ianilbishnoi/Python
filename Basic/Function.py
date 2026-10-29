# Functions
def hello(name="my friend"): # defining a function with a default value
    print("hello! "+name) # prints the message

hello("Beau") # calling the function
hello("Quincy")

# parameters are written when defining a function
# arguments are the values passed when calling it
# if no argument is given, the default value is used
hello() # prints hello! my friend

def hel(name, age):
    print("Hello "+name+ ",you are " + str(age) + " years old."  )

hel("Beart",39)

def change(value):
    value = 2

val =1 # changing value inside the function won't change the original integer
change(val)
print(val)

def change1(value):
    value["name"]="syd"

val1 ={"name": "beau"} # dictionaries can be changed inside a function
change1(val1)
print(val1)

def hello1(name1):
    if not name1:
        return
    print("Hello "+name1+'!')

hello1(False) # nothing gets printed because the function returns early

# global variable
age = 8

def test():
    print(age)

print(age) # 8
test() # 8

# local variable
def test2():
    age1= 8
    print(age1)

age1=7
print(age1) # prints the variable defined outside the function
# the age1 inside test2() is separate from the one outside
test2()

# nested function
def talk(phrase):
    def say(word): # this function is only used inside talk()
        print(word)

    words = phrase.split(' ')
    for word in words:
        say(word)

talk("I am Iron Man")

# nonlocal lets us change a variable from the outer function
def count(): # outer function
    count =0

    def increment():
        nonlocal count # uses count from the outer function
        count +=1
        print(count)

    increment()

count()

# closure
# the inner function can still access the outer variable after the outer function ends
def counter():
    count = 0

    def increment():
        nonlocal count
        count +=1
        return count

    return increment

increment=counter()

print(increment()) # 1
print(increment()) # 2
print(increment()) # 3, count is remembered between calls
