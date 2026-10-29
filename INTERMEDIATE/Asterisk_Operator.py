# * sign in python - multiplication, power, args, kwargs and unpacking
result = 2**4
print(result)

zeros=[0]*5 # repeats the value 5 times
print(zeros)

def fool(a,b,*args,**kwargs): # *args takes extra positional args and **kwargs takes keyword args
    print(a,b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key,kwargs[key])

fool(1,2,3,hun=100)

# unpacking a dictionary
def fool1(a,b,c):
    print(a,b,c)

dict={'a':1,'b':2,'c':3}
fool(**dict) # passes dictionary values as keyword arguments

# unpacking elements
numbers=[1,2,3,4,5]
*beginning,last=numbers # *beginning collects the remaining elements into a list
print(beginning) # prints all elements except the last
print(last) # prints the last element
