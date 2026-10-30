"""
-functions and arguments
-positional and keyword arguments
-default arguments
-variable length arguments (*args and **kwargs)
-unpacking containers into function arguments
-local vs global variables
-how values are passed to functions
"""

#functions
def hello(name="my friend"):#default value is used if no argument is given
    print("hello! "+name)#function body

hello("Beau")#calling the function
hello("Quincy")

#parameters are written while defining a function
#arguments are passed when calling a function
#name="my friend" is the default argument
hello()#prints hello! my friend

def hel(name, age):
    print("Hello "+name+ ",you are " + str(age) + " years old."  )

hel("Beart",39)

def change(value):
    value = 2

val =1 #changing an integer inside the function doesn't change the original
change(val)
print(val)

def change1(value):
    value["name"]="syd"

val1 ={"name": "beau"}#dictionaries can be modified inside a function
change1(val1)
print(val1)

def hello1(name1):
    if not name1:
        return
    print("Hello "+name1+'!')

hello1(False)#returns without printing anything

#global variable
age = 8

def test():
    print(age)

print(age)#8
test()#8

#local variable
def test2():
    age1= 8
    print(age1)

age1=7
print(age1)#prints the global age1, not the one inside test2()
#local variables can only be accessed inside their function
test2()

#nested function
def talk(phrase):
    def say(word):#this function is only available inside talk()
        print(word)

    words = phrase.split(' ')
    for word in words:
        say(word)

talk("I am Iron Man")

#nonlocal lets an inner function change a variable from the outer function
def count():#outer function
    count =0

    def increment():
        nonlocal count#uses count from the outer function
        count +=1
        print(count)

    increment()

count()

#closure - the inner function remembers variables from the outer function
#even after the outer function has finished
def counter():
    count = 0

    def increment():
        nonlocal count
        count +=1
        return count

    return increment

increment=counter()

print(increment())#1
print(increment())#2
print(increment())#3, count is remembered between calls

#variable length arguments
def fool(a,b,*args,**kwargs):#args collects extra positional arguments, kwargs collects keyword arguments
    print(a,b)

    for arg in args:
        print(arg)

    for key in kwargs:
        print(key,kwargs[key])

fool(1,2,3,4,5, six=6, seven=7)

#keyword-only argument
def foo1(*args, last):#last must be passed using its name
    for arg in args:
        print(arg)

    print(last)

foo1(1,2,3,last=100)
