# LAMBDA
multiply = lambda x, y: x*y # takes two arguments and multiplies them
print(multiply(2,3))

# map, filter and reduce are used to work with collections

# MAP
num=[1,2,3]

double = lambda x: x*2 # doubles the given number

# def double(a):
#     return a*2

result = map(lambda x: x*2, num) # applies the function to each element
print(list(result))

# FILTER
numbers =[4,5,6]

# def isEven(num):
#     return num % 2 == 0

result = filter(lambda n:n%2==0, numbers) # keeps only even numbers
print(list(result))

# REDUCE
from functools import reduce

expense=[('dinner',80),('Car repair',120)]

sum = reduce(lambda a, b: a[1] + b[1], expense) # adds the expense amounts

# for expense in expense:
#     sum += expense[1]

print(sum)
