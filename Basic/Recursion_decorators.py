# recursion
# 3! = 3 * 2 * 1

def factorial(n):
    if n==1:return 1 # stops when n becomes 1
    return n*factorial(n-1) # calls the same function with n-1

print(factorial(3))

# Decorators
# a decorator adds extra behaviour to a function without changing its code

def logtime(func): # takes another function as input
    def wrapper(): # runs extra code before and after the function
        print("before")
        val=func()
        print("after")
        return val
    return wrapper

@logtime # applies the decorator to hello()
def hello():
    print("Hello")

hello()
