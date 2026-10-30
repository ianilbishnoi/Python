#decorators - adds extra behaviour to a function without changing its code
def logtime(func):#takes a function as an argument
    def wrapper():#runs extra code before and after the function
        print("before")
        val=func()
        print("after")
        return val
    return wrapper

@logtime#applies the decorator to hello()
def hello():
    print("Hello")

hello()
