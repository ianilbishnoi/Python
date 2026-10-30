tuple1 = ("max",29 ,"Boston")
print(tuple1)

#tuples are immutable
mytuple = tuple(["Max",28,"Boston"])
print(mytuple)

#accessing an item using its index
item = mytuple[-2]
print(item)

#looping through a tuple
for x in mytuple:
    print(x)

#checking if an item exists
if "Boston" in mytuple:
    print(mytuple)
else:
    print(mytuple)

#counting how many times an item appears
tuple2 =('a','p','p','l','e')
print(tuple2.count('p'))

#finding the index of an item
print(tuple2.index('l'))

#converting a tuple to a list and back
tuple3 = list(tuple2)
tuple4 = tuple(tuple3)
print(tuple4)

#slicing a tuple
a=(1,2,3,4,5,6,7)
b=a[2::2]
b=a[::-1] #reverses the tuple
print(b)

#unpacking tuple values
tuple5=[0,1,2,3,4]
i1, *i2, i3 = tuple5
print(i1)
print(i2) #the middle values are stored together in a list
print(i3)

import sys #used to check memory size

my_list = [0,1,2,"hello", True]
my_tuple = (0,1,2,"hello", True) #tuples can use less memory than lists
print(sys.getsizeof(my_list),"bytes")
print(sys.getsizeof(my_tuple),"bytes")

#comparing the time taken to create a list and a tuple
import timeit

print(timeit.timeit("my_tuple = [0,1,2,3,4]",number=10000))
print(timeit.timeit("my_tuple = (0,1,2,3,4)",number=10000))
