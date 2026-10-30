def generator():
    yield 1
    yield 3
    yield 2

g=generator()

#returns a generator that gives one value at a time
#saves memory because values are generated when needed

"""value=next(g)
print(value)
value=next(g)
print(value)
value=next(g)
print(value)"""

n=sorted(g)
print(n)

#example
def countdown(num):
    print("Starting")
    while num>0:
        yield num
        num-=1
    cd = countdown(4)

    value = next(cd)
    print(value)

    print(next(cd))
    print(next(cd))
    print(next(cd))
    print(next(cd))
