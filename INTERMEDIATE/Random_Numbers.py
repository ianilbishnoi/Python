#generating random numbers
import random #generates pseudo-random numbers

a=random.random() #generates a random float between 0 and 1
print(a)

b=random.randint(1,10) #includes both 1 and 10
print(b)

c=random.randrange(1,10) #does not include 10
print(c)

d= random.normalvariate(0,1) #generates a value from a normal distribution with mean 0 and std 1
print(d)

list1=list("ABCDEFGH")
random.shuffle(list1) #shuffles the list
e=random.choice(list1) #picks one random element
f=random.sample(list1,3) #picks 3 unique elements from the list

print(e)
print(f)
print(list1)

random.seed(1) #same seed gives the same sequence of random values
print(random.random())
print(random.randint(1,10))

random.seed(2)
print(random.random())
print(random.randint(1,10))

#importing secrets for more secure random values
import secrets

a=secrets.randbits(4) #generates a random 4-bit integer
print(a)

b=secrets.randbelow(10) #generates an integer from 0 to 9
print(b)
