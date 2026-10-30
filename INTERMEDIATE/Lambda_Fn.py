#lambda expressions and built-in functions

multiply = lambda x, y: x*y #can take more than one argument
print(multiply(2,3))

#map, filter and reduce are commonly used with functions

#map
num=[1,2,3]
double = lambda x: x*2 #can use lambda directly without storing it in a variable

#def double(a):
    #return a*2 #used to apply a function to each value

result = map(lambda x: x*2, num)
print(list(result))

points2D =[(1,2),(3,4),(5,6)]
points2D_sorted = sorted(points2D, key=lambda x:x[0]+x[1])
print(points2D)
print(points2D_sorted)

#map, filter and reduce are commonly used with functions

#map
num=[1,2,3]
double = lambda x: x*2 #can use lambda directly without storing it in a variable

#def double(a):
    #return a*2 #used to apply a function to each value

result = map(lambda x: x*2, num)
print(list(result))

#filter
numbers =[4,5,6]

#def isEven(num):
    #return num % 2 == 0

result = filter(lambda n:n%2==0, numbers) #keeps only values that match the condition
print(list(result))

#reduce
from functools import reduce

expense=[('dinner',80),('Car repair',120)]
sum = reduce(lambda a, b: a[1] + b[1], expense) #adds the expense values without a separate loop

#for expense in expense:
   # sum += expense[1]

print(sum)
